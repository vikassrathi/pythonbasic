from typing import Generic,TypeVar

T=TypeVar('T')

class check:
    def __init__(self):
        self.typecheck='int'

    def checkdatatype(self,datatype:Generic[T]):
        if datatype==self.typecheck:
            return True
        else:
            return False

c=check()
value=c.checkdatatype('str')
print(value)