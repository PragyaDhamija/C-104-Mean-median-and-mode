import csv
with open('heightWeight.csv', newline = '') as f:
     #csv.reader method which reads and returns the current row and then moves on to the next.
    r= csv.reader(f) 
    fileData = list(r)
fileData.pop(0)

newData = []
for i in range(len(fileData)):
    num = fileData[i][1]
    #type casting to float or else the value after point will not be there
    newData.append( float(num) )
    
n = len(newData)
sum = 0
for i in newData:
    sum = sum+i
mean = sum/n
print("Your required mean/average is:" + str(mean))


import statistics

print( statistics.mean(newData ) )
print( statistics.median(newData))
print( statistics.mode(newData))