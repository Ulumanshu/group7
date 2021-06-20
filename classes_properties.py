class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property  # getter - get field value
    def age(self):
        return self.__age

    @age.setter  # setter - sets a new field value
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter  # deleter - delete the field
    def age(self):
        print('DELETERIS VEIKIA')
        del self.__age

    @property
    def animal_code(self):
        return f"NM{len(self.name) > 2 and self.name[:2] or 'AA'}AG{self.age}"


if __name__ == "__main__":
    my_dog = Animal('Brisius', 5)
    my_dog.age = -3  # Sets age - uses setter
    print(my_dog.age)  # Reads age - uses a getter
    print(my_dog.animal_code)
    del my_dog.age
