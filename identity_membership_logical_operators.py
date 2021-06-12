# Identity operators 	is, is not
# Logical operators 	and, or, not
# Membership operators 	in, not in
a = list()
b = list()
c = a

print(a == b)
print(a is b)

print(a == c)
print(a is c)
print(a == c)

print(a == b and a is b)

d = [1, 2, 3, 4, 5]
print(2 in d, 2 not in d, 6 in d, 6 not in d)


