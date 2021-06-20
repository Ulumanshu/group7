class Human:
    def __init__(self, name, height, weigth):
        self.name = name
        self.height = height
        self.weigth = weigth


class Programmer(Human):
    def __init__(self, name, height, weigth, languages):
        super().__init__(name, height, weigth)
        self.languages = languages


bob = Programmer("Bob", 180, 100, ["Python", "Java"])
print(bob.name)  # Access to the name field inherited from the Human class
print(bob.languages)


class Bat:
    def be_a_bat(self):
        print('I am bat')


class Man:
    def be_a_man(self):
        print('I am man')


class Batman(Bat, Man):
    pass


batman1 = Batman()
batman1.be_a_bat()
batman1.be_a_man()
