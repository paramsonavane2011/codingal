class pair():
    def add(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if (target - num) in d:
                print(d[target - num], i)
                break
            d[num] = i
        print(d)

pair().add([1, 2, 3, 4, 5], 5)