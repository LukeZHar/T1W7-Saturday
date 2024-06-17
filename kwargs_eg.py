def personal_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} ---> {value}")

personal_details(name="Luke", age="30", address="Brisbane")

def myFunction(*onestar, **twostars):
    print("args: ", onestar)
    print("kwargs: ", twostars)

myFunction('I', 'Love', 'Coding', first = "I", second = "Love", third = "Coding")
