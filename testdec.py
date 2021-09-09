
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"you called {func.__name__}({args}, {kwargs})")
        value = func(*args, **kwargs)
        print(f"it return {value}")
        return value
    return wrapper

@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)

print(func(1,2,3,5,6,9,6,6,0, a=4))
    
print('ali in test2 remote')
pritn('ali2')
