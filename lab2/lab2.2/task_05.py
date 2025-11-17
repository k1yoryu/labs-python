def cache(func):
    results = {}

    def wrapper(*args):
        if args in results:
            print(f"[КЭШ] {func.__name__}{args}")
            return results[args]
        result = func(*args)
        results[args] = result
        print(f"[ВЫЧИСЛЕНО] {func.__name__}{args}")
        return result
    return wrapper

@cache
def add_numbers(x, y):
    print("Считаем сумму: ")
    return x + y

@cache
def power(base, exp):
    print("Возводим в степень: ")
    return base ** exp

print(add_numbers(2, 3))
print(add_numbers(2, 3))
print(power(2, 5))
print(power(2, 5))
