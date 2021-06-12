# Function definition of greet_by_name (name)
a = 2


def greet_by_name(name, sk, name_prefix='Mr'):
    sk += 100
    print(f"Hello, {name_prefix}, {name}, {sk}")

    return sk


def greet_by_surename(surename, sk):
    sk += 100
    print(f"Hello, {surename}, {sk}")

    return sk


def greet_by_account(account, sk):
    sk += 100
    print(f"Hello, {account}, {sk}")

    return sk


# Call function greet_by_name (name) with "John" as the name argument
new_a = greet_by_name("John", a, name_prefix='Mrs')
a = new_a
new_a = greet_by_account('john@gmail.com', a)


def sum_function_args(*args):
    print(args)

    return sum(args)


def sum_function_kwargs(**kwargs):
    print(kwargs)
    for e in kwargs:
        print(e)

    # raktai = kwargs.keys()
    # reiksmes = kwargs.values()
    return sum(kwargs.values())


sum_list = [5, 5, 5, 5]
sum_dict = {
    'raktas1': 1,
    'raktas2': 2,
    'raktas3': 3,
}

sum1 = sum_function_args(*sum_list)
sum2 = sum_function_args(1, 2, 3)

sum3 = sum_function_kwargs(**sum_dict)
sum4 = sum_function_kwargs(raktas1=5, raktas2=4)

print(sum1, sum2)
print(sum3, sum4)
