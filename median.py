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

# floor division is shown by //
newData.sort()
if n% 2 == 0:
    m1 = float(newData[n//2]) 
    m2 = float(newData[n//2-1])
    median = (m1+m2)/2
else:
    median = newData[n//2]
print(median)