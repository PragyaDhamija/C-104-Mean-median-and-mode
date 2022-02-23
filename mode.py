import csv
from collections import Counter

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

data = Counter(newData)
modeDataRange = {
     "50-60": 0,
     "60-70": 0,
     "70-80": 0
}

for height, occurence in data.items():
    if 50 < float(height) < 60:
        modeDataRange["50-60"] += occurence
    elif 60 < float(height) < 70:
        modeDataRange["60-70"] +=occurence
    if 70 < float(height) < 80:
        modeDataRange["70-80"] +=occurence

print(modeDataRange)
print(modeDataRange.items())

modeRange, modeOccurence = 0,0
for range,occurence in modeDataRange.items():
    if(occurence>modeOccurence):
        modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
print(modeOccurence)
print(modeRange) # [ 60 , 70 ]

mode = float( (modeRange[0]+ modeRange[1])/2 )
print(mode)

print(f"\nCalculated Mode : { mode} ")