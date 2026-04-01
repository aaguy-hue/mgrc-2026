import sys

maxStops = int(input()) # k
boardingStation = input() # b
destinationStation = input() # d
n = int(input())
s = [input() for _ in range(n)]

success = True
boardingStationVisited = False
destinationStationVisited = False
stopsCount = 0
for i in range(n):
    if s[i] == boardingStation:
        if boardingStationVisited:
            stopsCount += 1
            
            if stopsCount > maxStops:
                success = False
                break
        else:
            boardingStationVisited = True
    
    if s[i] == destinationStation:
        if not boardingStationVisited:
            success = False
            break
        else:
            destinationStationVisited = True
            break

if success and boardingStationVisited and destinationStationVisited and stopsCount <= maxStops:
    print("true")
else:
    print("false")