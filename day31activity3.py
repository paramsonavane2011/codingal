class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing")

class China():
    def capital(self):
        print("Beijing")
    def language(self):
        print("Chinese")
    def type(self):
        print("Developed")

i = India()
c = China()

for i in (i, c):
    i.capital()
    i.language()
    i.type()