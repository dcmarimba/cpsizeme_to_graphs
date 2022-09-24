# written to import a detailed cpsizeme and provide some form of visualsation of the data
# first attempt 040922 v0.1

#imports
import pandas as pd
import hvplot.pandas
import holoviews as hv
from datetime import datetime
from tarfile import TarFile
from pathlib import Path

import panel.template
from bokeh.models import HoverTool
from bokeh.themes.theme import Theme
from panel.template import DarkTheme
import matplotlib.pyplot as plt
import panel as pn

# vars
start_date = '2022-08-23'
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = '2022-08-24'
end_date = datetime.strptime(end_date, '%Y-%m-%d')
dfread_fullstats = {}
dfread_fullstats_whole = {}

# command options
pd.options.plotting.backend = 'holoviews'
pd.options.mode.chained_assignment = None
pn.extension(sizing_mode='stretch_width', template='material', theme='dark')

# Data reading functions

def ReadSomeDataSampled():
    dfread_fullstats_raw = pd.read_csv('fullstats.csv', index_col=False, parse_dates={'DateTime':[0, 1]}, skip_blank_lines=True)
    dfread_fullstats_raw = dfread_fullstats_raw.set_index(pd.DatetimeIndex(dfread_fullstats_raw["DateTime"])).drop("DateTime", axis=1)
    dfread_fullstats_raw = dfread_fullstats_raw.drop(['TPT/conn'], axis=1)
    dfread_fullstats_raw["Kernel"] = dfread_fullstats_raw["Kernel"].str.rstrip("%").astype("float")
    dfread_fullstats_raw["Avg. CPU: Total"] = dfread_fullstats_raw["Avg. CPU: Total"].str.rstrip("%").astype("float")
    dfread_fullstats_raw["max core sy+si+hi"] = dfread_fullstats_raw["max core sy+si+hi"].str.rstrip("%").astype("float")
    dataframe = dfread_fullstats_raw.resample('10min').mean()
    return dataframe

def ReadSomeData():
    dfread_fullstats_raw = pd.read_csv('fullstats.csv', index_col=False, parse_dates={'DateTime':[0, 1]}, skip_blank_lines=True)
    dfread_fullstats_raw = dfread_fullstats_raw.set_index(pd.DatetimeIndex(dfread_fullstats_raw["DateTime"])).drop("DateTime", axis=1)
    dfread_fullstats_raw = dfread_fullstats_raw.drop(['TPT/conn'], axis=1)
    dfread_fullstats_raw["Kernel"] = dfread_fullstats_raw["Kernel"].str.rstrip("%").astype("float")
    dfread_fullstats_raw["Avg. CPU: Total"] = dfread_fullstats_raw["Avg. CPU: Total"].str.rstrip("%").astype("float")
    dfread_fullstats_raw["max core sy+si+hi"] = dfread_fullstats_raw["max core sy+si+hi"].str.rstrip("%").astype("float")
    dataframe = dfread_fullstats_raw
    return dataframe

# file grabbing functions

def WhatFiles():
    filename = 'fullstats.csv'
    print("This tool will chart the data from 'fullstats.csv' from the cpsizeme file")
    print("Please upload the cpsizeme file below;")
    rawtarfilepath = input("Cpsizeme file location:")
    rawtarfile = Path(rawtarfilepath)
    with TarFile(rawtarfile) as tarObj:
        listOfFileNames = rawtarfile.getnames()
        print("The list of files are;")
        print(listOfFileNames)
        print('\n')
        print("Searching for fullstats.csv...")
        for fileName in listOfFileNames:
            if fileName in listOfFileNames:
                tarObj.read(filename, 'tempfiles')
            else:
                print("Whoops.. there's no file there called fullstats.csv!")




# Grab the data from the users


# grab the data, return the frame

dfread_fullstats = ReadSomeDataSampled()
dfread_fullstats_whole = ReadSomeData()

# function plots

def hvPlotLinePercent(dataframe, yaxis, colorvar, labelvar):
    ytickvar = list(range(0, 110, 10))
    ylimvar = (0,100)
    plot = dataframe.hvplot(y=yaxis, height=graphheight, width=graphwidth, grid=True, yticks=ytickvar, ylim=ylimvar, color=colorvar, yformatter='%d%%', label=labelvar, legend=legendvar)
    return plot

def hvPlotLine(dataframe, yaxis, colorvar, labelvar):
    val1 = str('@{')
    val2 = str('}{0,0}')
    val3 = val1+yaxis+val2
    hover = HoverTool(tooltips=[('DateTime', '@DateTime{%F %H:%M:%S}'),((yaxis), val3)], formatters={'@DateTime': 'datetime'})
    plot = dataframe.hvplot(y=yaxis, height=graphheight, width=graphwidth, grid=True, color=colorvar, label=labelvar, legend=legendvar)
    plot.opts(tools=[hover])
    return plot

def hvPlotArea(dataframe, yaxis, colorvar, labelvar):
    ytickvar = list(range(0, 110, 10))
    ylimvar = (0,100)
    plot = dataframe.hvplot.area(y=yaxis, height=graphheight, width=graphwidth, grid=True, yticks=ytickvar, ylim=ylimvar, color=colorvar, yformatter='%d%%', label=labelvar)
    return plot

def hvPlotBarH(dataframe, val1, labelvar):
    plot = dataframe.hvplot.barh(val1, stacked=True, height=graphheight, width=graphwidth, grid=True, label=labelvar)
    return plot

def hvPlotHeatMap(dataframe, mapval, labelvar):
    plot = dataframe.hvplot.heatmap(x='index.day', y='index.hour', C=mapval, height=800, width=1000, cmap=["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"], colorbar=True, label=labelvar)
    return plot

def PlotPie(dataframe, FirstVal):
    explode = (0.05, 0.05, 0.05)
    plot = dataframe.index.day.sum().plot(kind='pie', y=FirstVal, autopct='%1.0f%%', explode=explode)
    return plot

groupbyvar = 'index.day'
graphwidth = 1750
graphheight = 550
legendvar = 'bottom_right'
column0 = 'DateTime'
column1 = 'max core sy+si+hi'
column2 = 'Handled Conns'
column3 = 'Max. RX/TX (Mbps)'
column4 = 'Avg. CPU: Total'
column5 = 'Kernel'
column6 = 'Created Conns/Sec '
column7 = 'kernel moving avg.'
column8 = 'Total drops (~)'
column9 = '1st max core #'

#% Plots
MaxCoreSysSiHiPlot = hvPlotLinePercent(dfread_fullstats, column1, 'red', labelvar='Max CPU across SYS/SI/HI')
AvgCPUTotPlot = hvPlotLinePercent(dfread_fullstats, column4, 'brown', labelvar='AVG CPU')
KernelCPUTotPlot = hvPlotLinePercent(dfread_fullstats, column5, 'orange', labelvar='Kernel CPU')
KernelMovAvgPlot = hvPlotLinePercent(dfread_fullstats, column7, 'yellow', labelvar='Kernel Moving Average')

#Val Plots
HandledConnsPlot = hvPlotLine(dfread_fullstats, column2, 'green', labelvar='Total Connections Handled')
ThroughputPlot = hvPlotLine(dfread_fullstats, column3, 'blue', labelvar='System Throughput in Mbps')
CreatedConnsPlot = hvPlotLine(dfread_fullstats, column6, 'purple', labelvar='No. Created Conns')
TotalDropsPlot = hvPlotLine(dfread_fullstats, column8, 'pink', labelvar='No. Total Drops')
MaxCorePlot = hvPlotLine(dfread_fullstats, column9, 'white', labelvar='Core # with highest %')

#Barh Plots
MaxCoreBarHPlot = hvPlotBarH(dfread_fullstats, column9, labelvar='something')

#Heat Maps
MaxCoreBarHeatMap = hvPlotHeatMap(dfread_fullstats_whole, column9, labelvar='Busiest Core Heatmap')

# Pie Plot

#Create a group
collapsedlayoutgroup1 = (MaxCoreSysSiHiPlot * AvgCPUTotPlot * KernelCPUTotPlot * KernelMovAvgPlot)
collapsedlayoutgroup2 = (HandledConnsPlot * ThroughputPlot * CreatedConnsPlot)

# Try and create a tabbed view

tabs = pn.Tabs(('Collapsed CPU Stats', collapsedlayoutgroup1))
tabs.extend([
    ('Max CPU across SYS/SI/HI', pn.panel(MaxCoreSysSiHiPlot, theme="dark_minimal")),
    ('AVG CPU', pn.panel(AvgCPUTotPlot, theme="dark_minimal")),
    ('Kernel CPU', pn.panel(KernelCPUTotPlot, theme="dark_minimal")),
    ('Kernel Moving Average', pn.panel(KernelMovAvgPlot, theme="dark_minimal")),
])
tabs

# Just an attempt to make it prettier

prettierView = (
    pn.Column(
        '# Collapsed CPU Stats',
        (tabs),
        pn.layout.Divider(),
    pn.Column(
        '# Individual Stats',
        (HandledConnsPlot), (CreatedConnsPlot), (ThroughputPlot), (TotalDropsPlot)),
        pn.layout.Divider(),
    pn.Column(
        '# Busiest Core Heat Map',
        (MaxCoreBarHeatMap)),
    )
)

# Show the data through Panel.

pn.panel(prettierView).show()
