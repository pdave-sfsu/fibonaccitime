from datetime import datetime, timedelta


def fib (n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for x in range(1, 100):
    timestart = datetime.now()
    answer = fib(x)
    timeend = datetime.now()
    totaltime = timeend - timestart
    print str(x) + " " + str(answer) + " " + str (totaltime)
