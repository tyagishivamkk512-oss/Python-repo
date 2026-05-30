def model(func):
    def wrapper(*args, **kwargs):
        print(f"your {args[0]} is 2025 model") # to choose first passed argument
        func(*args,**kwargs)
    return wrapper


def colour(hello):
    def wrapper(*args, **kwargs):
        print(f"you chose red {args[0]}")
        hello(*args, **kwargs) # to accept any no. of arguments and keywords
    return wrapper
    
@model
@colour
def buycar(company):
    print(f"Here is your {company}")

buycar("mustang")