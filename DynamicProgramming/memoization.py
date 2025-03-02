#fibonacci series

fun_call = 0
def fib(n): # BigO -> O(2^n) very inefficient
    global fun_call
    fun_call += 1
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# n = 30

# print('Fib of', n,'=',fib(n))
# print("Total function calls: ", fun_call)

### Dynamic Programming ###

memo = [None]*100 #memoization

def fib_memo(n): # BigO -> O(n) efficient
    global fun_call
    fun_call += 1
    if memo[n] is not None:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1) + fib_memo(n-2)

    return memo[n]

n = 30

print('Fib of', n,'with memoization is: ',fib_memo(n))
print("Total function calls: ", fun_call)
