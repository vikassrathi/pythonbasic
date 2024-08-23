



class multiple_inheritance_class1:
    def __init__(self):
        self.age=1

class multiple_inheritance_class2:
    def __init__(self):
        self.age=2
class child_class(multiple_inheritance_class1,multiple_inheritance_class2):
    def __init__(self):
        self.age=3
check=child_class()

print(check.age)