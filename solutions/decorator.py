def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return wrapper


@decorator
def my_func():
    print("do work")


my_func()