import sys

# count the arguments
#arguments = len(sys.argv) - 1
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))


import pandas as pd

df = pd.read_excel (r'Geocoordinates.xls') #for an earlier version of Excel, you may need to use the file extension of 'xls'
print (df.head())

def find_nearest_location(latitude, longitude):
    min1=1000.0
    min2=1000.0 
    currlat=0.0
    currlong=0.0
    currLoc=""
    for i, j in df.iterrows(): 
        #print(i, j) 
        #print() 
        #print(type(j['Latitude']))
        #print(float(j['Latitude']))
        diff2 = float(latitude)
        #print(diff1)
        if(abs(j['Latitude']-latitude) + abs(j['Longitude']-longitude)<abs(min1)):
            min1=abs(j['Latitude']-latitude) + abs(j['Longitude']-longitude)
            currlat=j['Latitude']
            currlong=j['Longitude']
            currLoc=j['Location']
    print(currLoc, currlat, currlong)
            
latitude = float(sys.argv[1])
longitude = float(sys.argv[2])
find_nearest_location(latitude,longitude)

def main():
     print ("hello world!")