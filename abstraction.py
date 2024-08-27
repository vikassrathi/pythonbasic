from abc import  ABC , abstractmethod



class vechile(ABC):

    def __init__(self,tyre):
        self.tyre=tyre

    @abstractmethod
    def type_of_vechile(self):
        pass

class car(vechile):
    def __init__(self,tyre):
        super().__init__(tyre)
    def type_of_vechile(self):
        pass

c=car(4)
print(c)
