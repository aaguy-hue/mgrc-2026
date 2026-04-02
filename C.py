n = int(input())
statements = [int(x) for x in input().split()]

longestSegment = 0

segmentStart = 0
segmentEnd = 0
uniqueVals = {}
for i, statement in enumerate(statements):
    if -statement in uniqueVals:
        # contradictory segment, just keep sliding window
        segmentStart = uniqueVals[-statement] + 1
        break
    
    uniqueVals[statement] = i
    segmentEnd += 1
    longestSegment = max(longestSegment, segmentEnd - segmentStart)

print(longestSegment)