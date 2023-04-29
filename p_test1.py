
class mobile:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def get_name(self):
        return self.name
        
class cpu(mobile):
    def get_name(self):
        print("This mobile has HighTech %s CPU " % self.name)
        
        
brand = cpu("Intel","Sony")
print(brand.get_name())

class maktabkhooneh:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def value(self):
        return self.name + self.grade
        
person = maktabkhooneh("Ahmad","Master",24)
print(person.value())