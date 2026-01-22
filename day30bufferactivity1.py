class rev():
    def reversal(self, a):
        res = a.split(" ")
        res = res[::-1]
        res = " ".join(res)
        return res

obj = rev()
print(obj.reversal("Hello World"))