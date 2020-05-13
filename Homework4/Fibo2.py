#Fibonacci Number

def fibo2(n):
    fibo = [1,1]
    if n == 1:
        return [1]
    elif n == 2:
        return fibo
    elif n > 2:
        x = 3
        while x <= n:
            y = fibo[x-2] + fibo[x-3]
            fibo.append(y)
            x = x + 1
        return fibo
    
    
n = input('Please input n for the Fibonacci Number:')

print fibo2(n)