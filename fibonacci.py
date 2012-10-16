import sys, time
calls = 0

def fibonacci(n):
    globals()['calls']+=1
    if n<=0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def run_on_list(n = None):
    try:
        if n ==None:
            n = int(sys.argv[1])
        input_list = range(n)
        print(input_list)
        for i in input_list:
            result = fibonacci(i)
            print(result)
            print("in:%d, out:%d, %d function calls." % (i, result, calls))
    except ValueError:
        print("1st argument must be a number!")

def run(n = None):
    if n == None:
        n = int(sys.argv[1])
    result = fibonacci(n)
    print(result)

def find_time(t = None):
    """
    @param t: time in seconds
    @return: n for which the calculation is longer than t, the exact time of this calc.
    """
    if t == None:
        t = int(sys.argv[1])
    measured = 0
    n = 0
    while(measured < t):
        n+=1
        t1 = time.time()
        fibonacci(n)
        t2 = time.time()
        measured = t2-t1
    return n, measured

if __name__=="__main__":
    n, measured = find_time()
    
