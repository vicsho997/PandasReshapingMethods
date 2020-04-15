import pandas as pd
import numpy as np
"""
pandas has simple, powerful, and efficient functionality for performing
 resampling operations during frequency conversion (e.g., converting
 secondly data into 5-minutely data). This is extremely common in, 
 but not limited to, financial applications. See the Time Series 
 section.
"""
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

print(ts.resample('5Min').sum())

#Time zone representation

rng1 = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts1 = pd.Series(np.random.randn(len(rng)), rng)

print(ts1)

ts1_utc = ts1.tz_localize('UTC')
print(ts1_utc)

#Converting to another time zone:

ts1_utc.tz_convert('US/Eastern')

#Converting between time span representations:

rng2 = pd.date_range('1/1/2012', periods=5, freq='M')
ts2 = pd.Series(np.random.randn(len(rng2)), index=rng2)

print(ts2)

ps2 = ts2.to_period()
print(ps2)

print(ps2.to_timestamp())

"""
Converting between period and timestamp enables some convenient 
arithmetic functions to be used. In the following example, we 
convert a quarterly frequency with year ending in November to 
9am of the end of the month following the quarter end:
"""

prng3 = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts3 = pd.Series(np.random.randn(len(prng3)), prng3)
ts3.index = (prng3.asfreq('M', 'e') + 1).asfreq('H', 's') + 9

print(ts3.head())