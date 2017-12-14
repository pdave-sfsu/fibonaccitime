from datetime import datetime, timedelta


def fib (n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result
    return result

totalTimeStart = datetime.now()
for x in range(1, 1001):
    memo = [None] * (x + 1)
    timestart = datetime.now()
    answer = fib(x, memo)
    timeend = datetime.now()
    totaltime = timeend - timestart
    print str(x) + " " + str(answer) + " " + str (totaltime)
totalTimeEnd = datetime.now()
print "Total Time" + str(totalTimeEnd - totalTimeStart)



# Only does up to 1000 because of CallStack error
