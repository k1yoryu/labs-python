def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, tp) in enumerate(zip(args, expected_types), start=1):
                if not isinstance(arg, tp):
                    raise TypeError(f"Аргумент #{i}: {arg} имеет тип {type(arg).__name__}, ожидался {tp.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(1, 2))
print(add("5", 3))