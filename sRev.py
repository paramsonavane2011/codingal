class Reverse():
    def __init__(self, s):
        self.s = s
    def reverse(self):
        return self.s[::-1]

obj = Reverse("Hello World")
print(obj.reverse())