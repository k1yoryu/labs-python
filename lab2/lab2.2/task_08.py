import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} заняла {(time.time() - start) * 1000:.2f} ms")
        return result
    return wrapper

@timing
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

print(factorial(50))