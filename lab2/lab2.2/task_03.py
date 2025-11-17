import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args):
            current_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            line = f"{current_time} | {func.__name__} | {args}\n"
            with open(filename, "a") as f:
                f.write(line)
            return func(*args)
        return wrapper
    return decorator


@log_calls("log_calls.log")
def square(number):
    return number * number

@log_calls("log_calls.log")
def text_lower(text):
    return text.lower()

@log_calls("log_calls.log")
def show_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

@log_calls("log_calls.log")
def multiply(number1, number2):
    return number1 * number2


print(square(4))
print(text_lower("NONSTOP OBSESSION"))
print(show_time())
print(multiply(5, 9))
