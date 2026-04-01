# summary: everything has freq of 2 except old maid, which has req of 1
from collections import Counter

n = int(input())
a = Counter(int(x) for x in input().split())
for k, v in a.items():
    if v == 1:
        print(k)
        break
