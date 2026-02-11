class Roman():
    def __init__(self, number):
        self.number = number
    def roman(self):
        roman_map = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        result = []
        for value, symbol in roman_map.items():
            while self.number >= value:
                result.append(symbol)
                self.number -= value

        return "".join(result)

num = Roman(123)
print(num.roman())