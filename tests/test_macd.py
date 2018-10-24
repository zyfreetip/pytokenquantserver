# Run Command
# catalyst run --start 2017-1-1 --end 2017-11-1 -o talib_simple.pickle \
#   -f talib_simple.py -x poloniex
#
# Description
# Simple TALib Example showing how to use various indicators
# in you strategy. Based loosly on
# https://github.com/mellertson/talib-macd-example/blob/master/talib-macd-matplotlib-example.py

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import talib as ta
from logbook import Logger
from matplotlib.dates import date2num
from mpl_finance import candlestick_ohlc

from catalyst import run_algorithm
from catalyst.api import (
    order,
    order_target_percent,
    symbol,
)
from catalyst.exchange.utils.stats_utils import get_pretty_stats

algo_namespace = 'talib_sample'
log = Logger(algo_namespace)


def initialize(context):
    log.info('Starting TALib macd')

    context.ASSET_NAME = 'BTC_USD'
    context.asset = symbol(context.ASSET_NAME)

    context.ORDER_SIZE = 10
    context.SLIPPAGE_ALLOWED = 0.05

    context.errors = []

    # Bars to look at per iteration should be bigger than SMA_SLOW
    context.BARS = 365
    context.COUNT = 0
    
    context.macds = pd.Series()
    context.macdSignals = pd.Series()
    context.macdHists = pd.Series()

    # Technical Analysis Settings
    context.MACD_FAST = 12
    context.MACD_SLOW = 26
    context.MACD_SIGNAL = 9

    pass


def _handle_data(context, data):
    # Get price, open, high, low, close
    prices = data.history(
        context.asset,
        bar_count=context.BARS,
        fields=['price', 'open', 'high', 'low', 'close'],
        frequency='15m')

    # Create a analysis data frame
    analysis = pd.DataFrame(index=prices.index)

    # MACD, MACD Signal, MACD Histogram
    analysis['macd'], analysis['macdSignal'], analysis['macdHist'] = ta.MACD(
        prices.close.as_matrix(), fastperiod=context.MACD_FAST,
        slowperiod=context.MACD_SLOW, signalperiod=context.MACD_SIGNAL)

    # MACD over Signal Crossover
    analysis['macd_test'] = np.where((analysis.macd > analysis.macdSignal), 1,
                                     0)
    # Save the prices and analysis to send to analyze
    context.prices = prices
    context.analysis = analysis
    context.macds = context.macds.append(analysis['macd'])
    context.macds.drop_duplicates(keep='first',inplace=True)
    context.macdSignals = context.macdSignals.append(analysis['macdSignal'])
    context.macdSignals.drop_duplicates(keep='first', inplace=True)
    context.macdHists = context.macdHists.append(analysis['macdHist'])
    context.macdHists.drop_duplicates(keep='first', inplace=True)
    context.price = data.current(context.asset, 'price')
    makeOrders(context, analysis)

    # Log the values of this bar
    logAnalysis(analysis)


def handle_data(context, data):
    log.info('handling bar {}'.format(data.current_dt))
    try:
        _handle_data(context, data)
    except Exception as e:
        log.warn('aborting the bar on error {}'.format(e))
        context.errors.append(e)

    log.info('completed bar {}, total execution errors {}'.format(
        data.current_dt,
        len(context.errors)
    ))

    if len(context.errors) > 0:
        log.info('the errors:\n{}'.format(context.errors))


def analyze(context, results):
    # Save results in CSV file
    filename = os.path.splitext(os.path.basename('talib_simple'))[0]
    results.to_csv(filename + '.csv')

    log.info('the daily stats:\n{}'.format(get_pretty_stats(results)))
    chart(context, context.prices, context.analysis, results)
    pass


def makeOrders(context, analysis):
    if context.asset in context.portfolio.positions:

        # Current position
        position = context.portfolio.positions[context.asset]

        if (position == 0):
            log.info('Position Zero')
            return

        # Cost Basis
        cost_basis = position.cost_basis

        log.info(
            'Holdings: {amount} @ {cost_basis}'.format(
                amount=position.amount,
                cost_basis=cost_basis
            )
        )

        # Sell when holding and got sell singnal
        if isSell(context, analysis):
            profit = (context.price * position.amount) - (
                cost_basis * position.amount)
            order_target_percent(
                asset=context.asset,
                target=0,
                limit_price=context.price * (1 - context.SLIPPAGE_ALLOWED),
            )
            log.info(
                'Sold {amount} @ {price} Profit: {profit}'.format(
                    amount=position.amount,
                    price=context.price,
                    profit=profit
                )
            )
        else:
            log.info('no buy or sell opportunity found')
    else:
        # Buy when not holding and got buy signal
        if isBuy(context, analysis):
            order(
                asset=context.asset,
                amount=context.ORDER_SIZE,
                limit_price=context.price * (1 + context.SLIPPAGE_ALLOWED)
            )
            log.info(
                'Bought {amount} @ {price}'.format(
                    amount=context.ORDER_SIZE,
                    price=context.price
                )
            )


def isBuy(context, analysis):
    # Bullish SMA Crossover
    # Bullish MACD
    if (getLast(analysis, 'macd_test') == 1):
        return True

    # # Bullish Stochastics
    # if(getLast(analysis, 'stoch_over_sold') == 1):
    #     return True

    # # Bullish RSI
    # if(getLast(analysis, 'rsi_over_sold') == 1):
    #     return True

    return False


def isSell(context, analysis):
    # Bearish SMA Crossover
    if (getLast(analysis, 'macd_test') == 0):
        return True

    # # Bearish Stochastics
    # if(getLast(analysis, 'stoch_over_bought') == 0):
    #     return True

    # # Bearish RSI
    # if(getLast(analysis, 'rsi_over_bought') == 0):
    #     return True

    return False


def chart(context, prices, analysis, results):
    results.portfolio_value.plot()

    # Data for matplotlib finance plot
    dates = date2num(prices.index.to_pydatetime())

    # Create the Open High Low Close Tuple
    prices_ohlc = [tuple([dates[i],
                          prices.open[i],
                          prices.high[i],
                          prices.low[i],
                          prices.close[i]]) for i in range(len(dates))]

    fig = plt.figure(figsize=(14, 18))

    # Draw the candle sticks
    ax1 = fig.add_subplot(411)
    ax1.set_ylabel(context.ASSET_NAME, size=20)
    candlestick_ohlc(ax1, prices_ohlc, width=0.4, colorup='g', colordown='r')
    # macd signal
    macd_point = []
    for date, row in analysis.macdHists.iteritems():
        if np.isnan(row):
            continue
        if len(macd_point) == 0:
            macd_point.append([date, row])
        if macd_point[-1][1] > 0 and row > 0:
            if macd_point[-1][1] > row:
                continue
            else:
                macd_point[-1] = [date, row]
        elif macd_point[-1][1] < 0 and row < 0:
            if macd_point[-1][1] < row:
                continue
            else:
                macd_point[-1] = [date, row]
        else:
            macd_point.append([date, row])
    import ipdb;ipdb.set_trace()
    
    macd_pd = pd.DataFrame(macd_point, columns=list('AB'))
    # Save results in CSV file
    filename = os.path.splitext(os.path.basename('macd_history'))[0]
    analysis.macdHist.to_csv(filename + '.csv')         
    filename = os.path.splitext(os.path.basename('macd'))[0]
    analysis.macd.to_csv(filename + '.csv')         
    filename = os.path.splitext(os.path.basename('macd_signal'))[0]
    analysis.macdSignal.to_csv(filename + '.csv')         
    filename = os.path.splitext(os.path.basename('macd_point'))[0]
    macd_pd.to_csv(filename + '.csv')         

    # Draw MACD computed with Talib
    ax3 = fig.add_subplot(414)
    ax3.set_ylabel('MACD: ' + str(context.MACD_FAST) + ', ' + str(
        context.MACD_SLOW) + ', ' + str(context.MACD_SIGNAL), size=12)
    analysis.macd.plot(ax=ax3, color='b', label='Macd')
    analysis.macdSignal.plot(ax=ax3, color='g', label='Signal')
    analysis.macdHist.plot(ax=ax3, color='r', label='Hist')
    ax3.axhline(0, lw=2, color='0')
    handles, labels = ax3.get_legend_handles_labels()
    ax3.legend(handles, labels)

    plt.show()


def logAnalysis(analysis):
    # Log only the last value in the array

    log.info('- macd:           {:.2f}'.format(getLast(analysis, 'macd')))
    log.info(
        '- macdSignal:     {:.2f}'.format(getLast(analysis, 'macdSignal')))
    log.info('- macdHist:       {:.2f}'.format(getLast(analysis, 'macdHist')))
    log.info('- macd_test:      {}'.format(getLast(analysis, 'macd_test')))

def getLast(arr, name):
    return arr[name][arr[name].index[-1]]


if __name__ == '__main__':
    run_algorithm(
        capital_base=10000,
        data_frequency='minute',
        initialize=initialize,
        handle_data=handle_data,
        analyze=analyze,
        exchange_name='bitfinex',
        quote_currency='usd',
        start=pd.to_datetime('2018-8-1', utc=True),
        end=pd.to_datetime('2018-8-31', utc=True),
    )