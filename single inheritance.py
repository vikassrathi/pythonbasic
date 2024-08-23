



class parent_class:
    def __init__(self):
        self.age=1
class child_class(parent_class):
    def __init__(self):
        super().__init__()
        self.age=2
check=child_class()
print(check.age)
