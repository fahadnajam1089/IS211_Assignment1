# divide parameter needs to be 2

def listDivide(numbers, divide=2):
    total = 0
    for e in numbers:

        # checking elements are divisible and if yes, then increase by 1
        if e % divide == 0:
            total = total + 1
    return total


class ListDivideException:
    @property
    def testListDivide(self):
        if listDivide([1, 2, 3, 4, 5]) != 2:
            return "Test Case Failed"
        elif listDivide([2, 4, 6, 8, 10]) != 5:
            return "Test Case Failed"
        elif listDivide([30, 54, 63, 98, 100], divide=10) != 2:
            return "Test Case Failed"
        elif listDivide([]) != 0:
            return "Test Case Failed"
        elif listDivide([1, 2, 3, 4, 5], divide=1) != 5:
            return "Test Case Failed"
