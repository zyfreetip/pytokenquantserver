'''
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY
from matplotlib.dates import MonthLocator,MONTHLY
import datetime as dt
import pylab
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import dates as mdates
from pandas import DataFrame,Series
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MinuteLocator,MONDAY,YEARLY
from matplotlib.dates import MonthLocator,MONTHLY
import matplotlib.patches as patches
import datetime as dt
import csv
import os
#import numpy as np


#C:\Users\wengyiming\Downloads\SAMPLE-binance-candle-data-push-2018-01-31\2018-01-31\BTCUSDT'

def date_to_num(dates):
    num_time = []
    for date in dates:
        #print(date)
        #date_time = dt.datetime.strptime(date,'%Y/%m/%d %H:%M')
        num_date = mdates.date2num(date)
        num_time.append(num_date)
    return num_time

def readstkData(rootpath):
    dir = '/Users/qiaoxiaofeng/Downloads/BTCUSDT/2018-8/'
    file_list = os.listdir(dir)
    dfs = []
    for file in file_list:
        if file.endswith('_15T.csv'):
            file_path = os.path.join(dir, file)
            df = pd.read_csv(file_path, skiprows=1) 
            dfs.append(df)
    df = [] 
    df = pd.concat(dfs)
    df['candle_begin_time'] = pd.to_datetime(df['candle_begin_time'])
    df.sort_values('candle_begin_time', inplace=True)
    df.to_csv('bitfinex-201808-15t.csv')
    returndata = df
    #print(returndata)


# Wash data
#    returndata = returndata.sort_index()
    #returndata.drop(['quote_volume','trade_num'],axis=1,inplace=True)
#    print(returndata)
#    returndata.columns = ['Open', 'High', 'Close', 'Low', 'Volume']
    returndata.columns=['Time','Open', 'High', 'Low', 'Close', 'Volume']
    returndata['Time']=date_to_num(returndata['Time'])
    return returndata

def drawing_candle():

    daylinefilepath = "."

    days = readstkData(daylinefilepath)

    # drop the date index from the dateframe & make a copy
    daysreshape = days.reset_index()
    # convert the datetime64 column in the dataframe to 'float days'
    #daysreshape['Time'] = mdates.date2num(daysreshape['Time'].astype(dt.date))
    # clean day data for candle view
    daysreshape.drop('Volume', axis=1, inplace=True)
    daysreshape = daysreshape.reindex(columns=['Time', 'Open', 'High', 'Low', 'Close'])

    #Av1 = movingaverage(daysreshape.Close.values, MA1)
    #Av2 = movingaverage(daysreshape.Close.values, MA2)
    MA2=5
    SP = len(daysreshape.Time.values[MA2 - 1:])
    print(SP)
    fig = plt.figure(facecolor='#07000d', figsize=(14, 18))
    ax1 = fig.add_subplot(211)
    #plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4)
    print(daysreshape.values[-SP:])
    candlestick_ohlc(ax1, daysreshape.values[-SP:], width=0.0014, colorup='#ff1717', colordown='#53c156')
    #Label1 = str(MA1) + ' SMA'
    #Label2 = str(MA2) + ' SMA'

    #ax1.plot(daysreshape.DateTime.values[-SP:], Av1[-SP:], '#e1edf9', label=Label1, linewidth=1.5)
    #ax1.plot(daysreshape.DateTime.values[-SP:], Av2[-SP:], '#4ee6fd', label=Label2, linewidth=1.5)
    ax1.grid(True, color='k',linestyle='--')
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(18))
    ticklabels = ['']*len(daysreshape)
    skip = len(daysreshape)//12
    daysreshape['Time'] = mdates.num2date(daysreshape['Time'])
    ticklabels[::skip] = daysreshape['Time'].iloc[::skip].dt.strftime('%Y-%m-%d')
    #ax1.xaxis.set_major_formatter(mticker.FixedFormatter(ticklabels))
    #plt.gcf().autofmt_xdate()
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    ax1.yaxis.label.set_color("w")
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")
    ax1.tick_params(axis='y', colors='w')
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
    ax1.tick_params(axis='x', colors='w')
    plt.ylabel('Stock price and Volume')
    plt.xticks(rotation=70)
    plt.xlabel('Date')
    
    x_axis = []
    y_axis = []
    with open('fenbi.csv', 'r') as f:
    	csv_reader = csv.reader(f)
    	for item in csv_reader:
    		if item[0] == 'candle_begin_time':
    			continue
    		x_axis.append(mdates.date2num(pd.to_datetime(item[0])))
    		y_value = item[1] if item[3]=='Y' else item[2]
    		y_axis.append(float(y_value))
    plt.plot(x_axis, y_axis)

    x2_axis = []
    y2_axis = []

    with open('xianduan.csv', 'r') as f:
    	csv_reader = csv.reader(f)
    	for item in csv_reader:
    		if item[0] == 'candle_begin_time':
    			continue
    		x2_axis.append(mdates.date2num(pd.to_datetime(item[0])))
    		y_value = item[1] if item[3]=='Y' else item[2]
    		y2_axis.append(float(y_value))

    plt.plot(x2_axis, y2_axis,'--')
    
    with open('zhongshu.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for item in csv_reader:
            if item[0] == 'begin_time':
                continue 
            ax1.add_patch(
                    patches.Rectangle(
                        (mdates.date2num(pd.to_datetime(item[0])), float(item[3])),
                        mdates.date2num(pd.to_datetime(item[1])) - mdates.date2num(pd.to_datetime(item[0])),
                        float(item[2])-float(item[3]),
                        edgecolor='r',
                        facecolor='none'
                        )
                )
    
    '''
    # Draw MACD computed with Talib
    macd = pd.read_csv('macd.csv')
    macd_signal = pd.read_csv('macd_history.csv')
    macd_hist = pd.read_csv('macd_signal.csv')
    ax3 = fig.add_subplot(212)
    ax3.set_ylabel('MACD: ' + str(12) + ', ' + str(26) + ', ' + str(9), size=12)
    macd.plot(ax=ax3, color='b', label='Macd')
    macd_signal.plot(ax=ax3, color='g', label='Signal')
    macd_hist.plot(ax=ax3, color='r', label='Hist')
    ax3.axhline(0, lw=2, color='0')
    handles, labels = ax3.get_legend_handles_labels()
    ax3.legend(handles, labels)
   # Draw MACD computed with Talib
    ax3 = fig.add_subplot(212)
    ax3.yaxis.label.set_color("w")
    ax3.set_ylabel('MACD: ' + str(12) + ', ' + str(26) + ', ' + str(9), size=12)
    # macd.plot(ax=ax3, color='b', label='Macd')
    # macd_signal.plot(ax=ax3, color='g', label='Signal')
    # macd_hist.plot(ax=ax3, color='r', label='Hist')
    ax3.axhline(0, lw=2, color='0')
    handles, labels = ax3.get_legend_handles_labels()
    ax3.legend(handles, labels)

    ax3.xaxis.set_major_locator(mticker.MaxNLocator(18))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.xticks(rotation=70)
    '''
    '''
    x4_axis = []
    y4_axis = []
    with open('macd.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for item in csv_reader:
            if item[0] == 'time':
                continue
            x4_axis.append(mdates.date2num(pd.to_datetime(item[0])))
            y4_axis.append(float(item[1]))
    plt.plot(x4_axis, y4_axis)

    x5_axis = []
    y5_axis = []
    with open('macd_history.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for item in csv_reader:
            if item[0] == 'time':
                continue
            x5_axis.append(mdates.date2num(pd.to_datetime(item[0])))
            y5_axis.append(float(item[1]))
    plt.plot(x5_axis, y5_axis)

    x6_axis = []
    y6_axis = []
    with open('macd_signal.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for item in csv_reader:
            if item[0] == 'time':
                continue
            x6_axis.append(mdates.date2num(pd.to_datetime(item[0])))
            y6_axis.append(float(item[1]))
    
    plt.plot(x6_axis, y6_axis)
    '''
    plt.ylabel('Stock price and Volume')
    plt.xticks(rotation=70)
    plt.xlabel('Date')
    plt.show()
    #fig.savefig('1.png')

drawing_candle()