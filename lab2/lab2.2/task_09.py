def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if any(not isinstance(arg, tp) for arg, tp in zip(args, expected_types)):
                raise TypeError("Несовпадение типов аргументов")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(1, 2))
print(add("5", 3))