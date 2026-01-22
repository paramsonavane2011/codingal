class Class():
    __privVar = 123
    def __privFunc(self):
        print("hi")
    def hello(self):
        print(self.__privVar)

object = Class()
object.hello()
object.__privFunc()
