import json


fileHandle=open("stats/musicStatistics.json", "r")

fileContents=fileHandle.read() # read contents of file in a variable
fileHandle.close() #close the file
#print(fileContents) #print file contents
 

#exit()

#myJSONDetails='{"library":{"songs":[{"title":"Shape of You","duration":"2:30","numberOfTimeListened":"478"}]}}'

myJSONDetails=fileContents


myJSON=json.loads(myJSONDetails)
songs=myJSON["library"]["songs"]
#print(songs)
numberOfSongs=len(songs)
maxListenedTime=0

for songIndex in range(0,numberOfSongs):
    
    duration=songs[songIndex]["duration"]
    numberOfTimeListened=int(songs[songIndex]["numberOfTimeListened"])
    durationList=duration.split(":")
    #print(durationList)

    durationLength=len(durationList)

    if(durationLength==2):
    #print(durationList[0])
        minutes=int(durationList[0])
        seconds=int(durationList[1])
        hours=0

    if(durationLength==3):
        hours=int(durationList[0])
        minutes=int(durationList[1])
        seconds=int(durationList[2])
        
    if(maxListenedTime<numberOfTimeListened):
        maxListenedTime=numberOfTimeListened
        maxListenedSong=songs[songIndex]["title"]
        
    calculatedSeconds=hours*3600 +minutes*60 +seconds
    timeListened=numberOfTimeListened*calculatedSeconds 
    #print(calculatedSeconds)
    print(timeListened)

print(maxListenedSong)    
