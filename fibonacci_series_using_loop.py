def get_fibonacci_series(n:int):
    
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]

    else:
        fib = [0, 1]
        prev2 = 0
        prev1 = 1
        for _ in range(2, n):
            new_fib = prev1 + prev2
            fib.append(new_fib)
            prev2 = prev1
            prev1 = new_fib

        return fib

n = int(input("Enter the number of terms: "))
print(get_fibonacci_series(n))
        
    