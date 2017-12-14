from datetime import datetime, timedelta


def fib (n):
    if n == 1 or n == 2:
        return 1
    bottomUpArray = [None] * (n + 1)
    bottomUpArray[1] = 1
    bottomUpArray[2] = 1
    for x in range (3, (n + 1)):
        bottomUpArray[x] = bottomUpArray[x-1] + bottomUpArray[x-2]
    return bottomUpArray[n]

totalTimeStart = datetime.now()
for x in range(1, 1001):
    timestart = datetime.now()
    answer = fib(x)
    timeend = datetime.now()
    totaltime = timeend - timestart
    print str(x) + " " + str(answer) + " " + str (totaltime)
totalTimeEnd = datetime.now()
print "Total Time" + str(totalTimeEnd - totalTimeStart)
