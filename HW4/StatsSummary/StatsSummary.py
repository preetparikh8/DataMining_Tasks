
import pandas as pd
import numpy as np


data = pd.read_csv('UCI_Space_Data.csv', sep=',',header=None)

#StatsSummary
a = data.iloc[:,[2]]
print "The mean for column", np.mean(a)
print "The STD for column", np.std(a)
print "The median for column 2", np.median(a)
arr = np.ma.array(a).compressed()
med = np.median(arr)
print "The MAD for column 2", np.median(np.abs(arr - med))
print "The Maximum for column ", np.amax(a)
print "The Minimum for column ", np.amin(a)