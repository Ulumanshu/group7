# Identity operators 	is, is not
# Logical operators 	and, or, not
# Membership operators 	in, not in
# a = list()
# b = list()
# c = a
#
# print(a == b)
# print(a is b)
#
# print(a == c)
# print(a is c)
# print(a == c)
#
# print(a == b and a is b)
#
d = [1, 2, 3, 4, 5, 33, 66]
# print(2 in d, 2 not in d, 6 in d, 6 not in d)

print(False and False and True)

target_element = 7
element_of_d = d and len(d) >= target_element and d[target_element - 1] or 0

print(element_of_d)

element_of_d2 = 0
if d and len(d) >= target_element:
    element_of_d2 = d[target_element - 1]

print(element_of_d2)
