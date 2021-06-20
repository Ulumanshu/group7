import copy

data_dict = {
    'key1': 'data1',
    'key2': 2,
    'key3': ('a', 'b'),
}

list1 = [data_dict]
# list2 = [data_dict]
list2 = copy.deepcopy(list1)


list1[0]['key1'] = 100
list2[0]['key1'] = 200

print(list1[0], list2[0])


class Animal:
    def __init__(self, name="Rex", age=2):
        self.name = name
        self.__age = age


dog_a = Animal()
dog_b = dog_a
print(dog_a.name)  # Display "Rex"
print(dog_b.name)  # Display "Rex"

dog_a.name = "Pongo"
print(dog_a.name)  # Display "Pongo"
print(dog_b.name)  # Display "Pongo"
