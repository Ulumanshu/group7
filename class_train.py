class DasAuto:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"DasAuto object, name: {self.name}"


name_list = ['audi', 'vw', 'nissan']
object_list = []
for name in name_list:
    instance = DasAuto(name)
    print(instance)
    object_list.append(instance)

print(object_list)