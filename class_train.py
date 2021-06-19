class DasAuto:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"DasAuto object, name: {self.name}"

    def papypsek_beep(self):
        signalas = f"{self.name} tau pypsi!"
        print(signalas)


class Animal:
    KINGDOM = "Animalia"  # class variable

    def __init__(self, name='John', age=2, tag='1z7sdgh'):
        self.name = name  # set the default value for the name field of the Animal class object
        self.age = age
        self.__tag = tag

    def print_details(self):  # method for printing the state of an object
        print(f"Name: {self.name}, age: {self.age}.")

    def set_tag(self, tag):
        if len(tag) > 2:
            self.__tag = tag
        else:
            print("Tsg must be longer than 2.")

    def get_tag(self):
        return self.__tag


if __name__ == "__main__":
    # DasAuto
    name_list = ['audi', 'vw', 'nissan']
    object_list = []
    for name in name_list:
        instance = DasAuto(name)
        print(instance)
        object_list.append(instance)
    print(object_list)
    for object_ in object_list:
        object_.papypsek_beep()

    # Animal
    animal_objektas = Animal()
    print(animal_objektas.KINGDOM, animal_objektas.name)
    # Uzd 2. Sukurti 10 gyvunu su unikaliais parametrais
    # Uzd 3. susideti sukurtus gyvunus i sarasa ir sekantis zingsnis atrinkti gyvunus jaunesnius nei 2 metai.

