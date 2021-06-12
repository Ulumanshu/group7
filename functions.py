# Function definition of greet_by_name (name)
a = 2


def greet_by_name(name, sk):
    sk += 100
    print(f"Hello, {name}, {sk}")

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
new_a = greet_by_name("John", a)
a = new_a
new_a = greet_by_account('john@gmail.com', a)
