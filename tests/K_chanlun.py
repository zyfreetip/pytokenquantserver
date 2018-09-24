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
#import numpy as np




#C:\Users\wengyiming\Downloads\SAMPLE-binance-candle-data-push-2018-01-31\2018-01-31\BTCUSDT'

def date_to_num(dates):
    num_time = []
    for date in dates:
        #print(date)
        date_time = dt.datetime.strptime(date,'%Y/%m/%d %H:%M')
        num_date = mdates.date2num(date_time)
        num_time.append(num_date)
    return num_time

def readstkData(rootpath):
    filename=rootpath+'/BITFINEX_BTCUSD_20180801_5T.csv'
    try:
        rawdata = pd.read_csv(filename)
    except IOError:
        raise Exception('IoError when reading dayline data file: ' + filename)

    returndata = rawdata
    #print(returndata)



# Wash data
#    returndata = returndata.sort_index()
    #returndata.drop(['quote_volume','trade_num'],axis=1,inplace=True)
#    print(returndata)
#    returndata.columns = ['Open', 'High', 'Close', 'Low', 'Volume']
    returndata.columns=['Time','Open', 'High', 'Low', 'Close', 'Volume']
    returndata['Time'][1:]=date_to_num(returndata['Time'][1:])
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
    fig = plt.figure(facecolor='#07000d', figsize=(18, 12))

    ax1 = plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4)
    print(daysreshape.values[-SP:])
    candlestick_ohlc(ax1, daysreshape.values[-SP:], width=0.0014, colorup='#ff1717', colordown='#53c156')
    #Label1 = str(MA1) + ' SMA'
    #Label2 = str(MA2) + ' SMA'

    #ax1.plot(daysreshape.DateTime.values[-SP:], Av1[-SP:], '#e1edf9', label=Label1, linewidth=1.5)
    #ax1.plot(daysreshape.DateTime.values[-SP:], Av2[-SP:], '#4ee6fd', label=Label2, linewidth=1.5)
    ax1.grid(True, color='k',linestyle='--')
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(18))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H-%M'))
    ax1.yaxis.label.set_color("w")
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")
    ax1.tick_params(axis='y', colors='w')
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
    ax1.tick_params(axis='x', colors='w')
    plt.ylabel('Stock price and Volume')

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
    plt.show()

drawing_candle()


