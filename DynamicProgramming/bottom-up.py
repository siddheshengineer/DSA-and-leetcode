count = 0

def fib(n):
    fib_list = [0,1]
    global count

    for index in range(2, n+1):
        count += 1
        nxt_fib = fib_list[index-1] + fib_list[index-2]
        fib_list.append(nxt_fib)

    return fib_list[n]

n = 30


print('Fib of', n,'with memoization is: ',fib(n))
print("Total function calls: ", count)