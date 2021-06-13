# Create a set
animals = {"dog", "cat", "elephant"}

# Add a new item
animals.add("mouse")

# Add several items at once
animals.update(["bird", "horse"])
# print(animals)

# Add the same item again
animals.add("mouse")
print(animals)

# Remove item, Python will throw an error if it is not in the set
animals.remove("cat")

# Remove item, Python will NOT throw an error if it is not in the set
animals.discard("cat")

animals_list = list(animals)
print(animals_list, animals_list[3])
for set_val in animals:
    print(set_val)