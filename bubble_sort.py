from random import randint
from datetime import datetime

startTime = datetime.now() # find starttime

a = []
for x in range(1,101):
    a.append(randint(1,10001))

def bubble_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
       for i in range(n):
           if arr[i] > arr[i + 1]:
               arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print arr

bubble_sort(a)

print datetime.now() - startTime # find starttime/endtime difference
