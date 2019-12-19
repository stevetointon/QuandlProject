import quandl
import numpy as np
quandl.ApiConfig.api_key = 'i8yc8ATodMv8XZjRPCWo'



data = quandl.get("Wiki/TSLA", start_date="2017-01-01", end_date="2017-12-30", returns="numpy")

def calculatePercentChange(a,b):
    diff = a -b
    percentChange = diff/a
    return percentChange

yearHigh = data[1][11]
yearLow = data[1][11]
biggestPercentChange = -1
lowestPercentChange = 10
#interate through the adj. close column for each day
for i in range(1,np.size(data,0)-1):
    if data[i][11]> yearHigh:
        yearHigh = data[i][11]
    elif data[i][11]< yearLow:
        yearLow = data[i][11]
    percentChange = calculatePercentChange(data[i][11], data[i-1][11])
    if (percentChange >biggestPercentChange):
        biggestPercentChange = percentChange
    elif(percentChange < lowestPercentChange):
        lowestPercentChange = percentChange
   

print(biggestPercentChange)
print(lowestPercentChange)

print(yearHigh)
print(yearLow)


