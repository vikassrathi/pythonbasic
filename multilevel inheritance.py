




class multilevel_inheritance_level1:
    def __init__(self):
        self.age=1


class multilevel_inheritance_level2(multilevel_inheritance_level1):
    def __init__(self):

        super().__init__()
        self.age = 2
class child_class(multilevel_inheritance_level2):
    def __init__(self):
        super().__init__()


check=child_class()
print(check.age)