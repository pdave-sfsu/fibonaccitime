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

for x in range(1, 1000):
    memo = [None] * (x + 1)
    timestart = datetime.now()
    answer = fib(x, memo)
    timeend = datetime.now()
    totaltime = timeend - timestart
    print str(x) + " " + str(answer) + " " + str (totaltime)



# Only does up to 1000 because of CallStack error
