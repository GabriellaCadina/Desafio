class Foo:
    def __init__(self, x=100):
        self._x = x
    
    # @property
    # def x(self):
    #     return self._x or 0
    
    # @x.setter
    # def x(self, value):
    #     self._x = value or 0

    
    

foo = Foo()
print(foo._x)
# print(foo.x)
# foo.x = None
# print(foo.x)
# # del foo.x