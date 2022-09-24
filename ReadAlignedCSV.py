# written to import a detailed cpsizeme and provide some form of visualsation of the data
# first attempt 040922 v0.1

#imports
import pandas as pd
import hvplot.pandas
from datetime import datetime
import panel as pn

# vars
start_date = '2022-08-23'
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = '2022-08-24'
end_date = datetime.strptime(end_date, '%Y-%m-%d')
dfread_aligned = {}

# command options
pd.options.mode.chained_assignment = None

dfread_aligned_raw = pd.read_csv('aligned2.csv', index_col=False, parse_dates={'DateTime':[0, 1]}, skip_blank_lines=True)
dfread_aligned_raw = dfread_aligned_raw.set_index(pd.DatetimeIndex(dfread_aligned_raw["DateTime"])).drop("DateTime", axis=1)
dfread_aligned_raw = dfread_aligned_raw.drop(['net:smears', 'Date (Year-m-d)', 'Time (24h:m:s)', 'Time (24h:m:s).1', 'top:smears'], axis=1)

# Filter out one day's data

# mask = (dfread_aligned_raw.index > start_date) & (dfread_aligned_raw.index <= end_date)
# dfread_aligned = dfread_aligned_raw.loc[mask]

# Split out CPU stats - can pivot later
dfread_aligned_cpu = dfread_aligned_raw.iloc[range(0, len(dfread_aligned_raw)),9:]

# Split the stats frame
dfread_aligned_stats = dfread_aligned_raw.iloc[range(0, len(dfread_aligned_raw)),0:9]

# grab the objects with a datatype of object
# objectdtypes = dfread_aligned.select_dtypes(object).columns.values.tolist()

# We can view all the data - but it makes plotting a fucking nightmare, so don't do that
# Select only one days data - don't do this, it can handle a full frame
# not currently using base frame - as I can graph from whole data
# mask = (dfread_aligned.index > start_date) & (dfread_aligned.index <= end_date)
# baseframe = dfread_aligned.loc[mask]
# baseframe = baseframe.resample('30min').mean()

# Sanitize the data
dfread_aligned_cpu["Avg. CPU: User/Nice"] = dfread_aligned_cpu["Avg. CPU: User/Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Avg. CPU: Nice (priority)"] = dfread_aligned_cpu["Avg. CPU: Nice (priority)"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Avg. CPU: Kernel"] = dfread_aligned_cpu["Avg. CPU: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Avg. CPU: Idle"] = dfread_aligned_cpu["Avg. CPU: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Avg. CPU: Hard/IRQ"] = dfread_aligned_cpu["Avg. CPU: Hard/IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Avg. CPU: Soft-IRQ"] = dfread_aligned_cpu["Avg. CPU: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Avg. CPU: I/O Wait"] = dfread_aligned_cpu["Avg. CPU: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Avg. CPU: Steal (Virtual)"] = dfread_aligned_cpu["Avg. CPU: Steal (Virtual)"].str.rstrip("%").astype("float")

dfread_aligned_cpu["Max. CPU: User"] = dfread_aligned_cpu["Max. CPU: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Max. CPU: Nice"] = dfread_aligned_cpu["Max. CPU: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Max. CPU: Kernel"] = dfread_aligned_cpu["Max. CPU: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Max. CPU: Idle"] = dfread_aligned_cpu["Max. CPU: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Max. CPU: IRQ"] = dfread_aligned_cpu["Max. CPU: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Max. CPU: Soft-IRQ"] = dfread_aligned_cpu["Max. CPU: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Max. CPU: I/O Wait"] = dfread_aligned_cpu["Max. CPU: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["Max. CPU: Steal (Virtual)"] = dfread_aligned_cpu["Max. CPU: Steal (Virtual)"].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU0: User"] = dfread_aligned_cpu["CPU0: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU0: Nice."] = dfread_aligned_cpu["CPU0: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU0: Kernel"] = dfread_aligned_cpu["CPU0: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU0: Idle"] = dfread_aligned_cpu["CPU0: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU0: IRQ"] = dfread_aligned_cpu["CPU0: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU0: Soft-IRQ"] = dfread_aligned_cpu["CPU0: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU0: I/O Wait"] = dfread_aligned_cpu["CPU0: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU0: St."] = dfread_aligned_cpu["CPU0: St."].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU1: User"] = dfread_aligned_cpu["CPU1: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU1: Nice."] = dfread_aligned_cpu["CPU1: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU1: Kernel"] = dfread_aligned_cpu["CPU1: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU1: Idle"] = dfread_aligned_cpu["CPU1: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU1: IRQ"] = dfread_aligned_cpu["CPU1: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU1: Soft-IRQ"] = dfread_aligned_cpu["CPU1: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU1: I/O Wait"] = dfread_aligned_cpu["CPU1: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU1: St."] = dfread_aligned_cpu["CPU1: St."].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU2: User"] = dfread_aligned_cpu["CPU2: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU2: Nice."] = dfread_aligned_cpu["CPU2: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU2: Kernel"] = dfread_aligned_cpu["CPU2: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU2: Idle"] = dfread_aligned_cpu["CPU2: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU2: IRQ"] = dfread_aligned_cpu["CPU2: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU2: Soft-IRQ"] = dfread_aligned_cpu["CPU2: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU2: I/O Wait"] = dfread_aligned_cpu["CPU2: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU2: St."] = dfread_aligned_cpu["CPU2: St."].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU3: User"] = dfread_aligned_cpu["CPU3: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU3: Nice."] = dfread_aligned_cpu["CPU3: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU3: Kernel"] = dfread_aligned_cpu["CPU3: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU3: Idle"] = dfread_aligned_cpu["CPU3: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU3: IRQ"] = dfread_aligned_cpu["CPU3: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU3: Soft-IRQ"] = dfread_aligned_cpu["CPU3: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU3: I/O Wait"] = dfread_aligned_cpu["CPU3: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU3: St."] = dfread_aligned_cpu["CPU3: St."].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU4: User"] = dfread_aligned_cpu["CPU4: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU4: Nice."] = dfread_aligned_cpu["CPU4: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU4: Kernel"] = dfread_aligned_cpu["CPU4: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU4: Idle"] = dfread_aligned_cpu["CPU4: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU4: IRQ"] = dfread_aligned_cpu["CPU4: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU4: Soft-IRQ"] = dfread_aligned_cpu["CPU4: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU4: I/O Wait"] = dfread_aligned_cpu["CPU4: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU4: St."] = dfread_aligned_cpu["CPU4: St."].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU5: User"] = dfread_aligned_cpu["CPU5: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU5: Nice."] = dfread_aligned_cpu["CPU5: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU5: Kernel"] = dfread_aligned_cpu["CPU5: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU5: Idle"] = dfread_aligned_cpu["CPU5: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU5: IRQ"] = dfread_aligned_cpu["CPU5: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU5: Soft-IRQ"] = dfread_aligned_cpu["CPU5: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU5: I/O Wait"] = dfread_aligned_cpu["CPU5: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU5: St."] = dfread_aligned_cpu["CPU5: St."].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU6: User"] = dfread_aligned_cpu["CPU6: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU6: Nice."] = dfread_aligned_cpu["CPU6: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU6: Kernel"] = dfread_aligned_cpu["CPU6: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU6: Idle"] = dfread_aligned_cpu["CPU6: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU6: IRQ"] = dfread_aligned_cpu["CPU6: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU6: Soft-IRQ"] = dfread_aligned_cpu["CPU6: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU6: I/O Wait"] = dfread_aligned_cpu["CPU6: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU6: St."] = dfread_aligned_cpu["CPU6: St."].str.rstrip("%").astype("float")

dfread_aligned_cpu["CPU7: User"] = dfread_aligned_cpu["CPU7: User"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU7: Nice."] = dfread_aligned_cpu["CPU7: Nice"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU7: Kernel"] = dfread_aligned_cpu["CPU7: Kernel"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU7: Idle"] = dfread_aligned_cpu["CPU7: Idle"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU7: IRQ"] = dfread_aligned_cpu["CPU7: IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU7: Soft-IRQ"] = dfread_aligned_cpu["CPU7: Soft-IRQ"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU7: I/O Wait"] = dfread_aligned_cpu["CPU7: I/O Wait"].str.rstrip("%").astype("float")
dfread_aligned_cpu["CPU7: St."] = dfread_aligned_cpu["CPU7: St."].str.rstrip("%").astype("float")
dfread_aligned_cpu = dfread_aligned_cpu.resample('5min').mean()
dfread_aligned_stats = dfread_aligned_stats.resample('5min').mean()

# just putting this here for reference
# hv_obj = baseframe.hvplot(x=baseframe.index, y=['RX+TX Drops', '5 minutes', 'Hard/IRQ', 'Soft-IRQ', 'I/O Wait'], kind='scatter')

hv_obj = hvplot.explorer(dfread_aligned_stats)
pn.panel(hv_obj).show()

# amazingly - this works! but I think some of my numbers are being mangled. So I need to check them and see how plot handles %'s
# It's to do with how you're handling decimals - don't divide them by 100. Then pass the values to hvplot as ".apply.transform(columns=percent)
# df.hvplot.scatter(x='lat', y='lon', xlim=(6, 8), ylim=(45, 47))
# https://holoviews.org/user_guide/Customizing_Plots.html
# https://holoviews.org/user_guide/Plotting_with_Bokeh.html
#
#
