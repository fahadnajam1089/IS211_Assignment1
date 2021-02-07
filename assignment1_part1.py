#default value of divide is 2
def listDivide(l,divide=2):
    c=0
    for e in l:
        #check all the elements are divisible, if it is divisible then increase c by 1
        if e%divide == 0:
            c=c+1
    return c

class ListDivideException:
    @property
    def testListDivide(self):
        if listDivide([1,2,3,4,5])!=2:
            return "Test Case Failed"
        elif listDivide([2,4,6,8,10])!=5:
            return "Test Case Failed"
        elif listDivide([30,54,63,98,100],divide=10)!=2:
            return "Test Case Failed"
        elif listDivide([])!=0:
            return "Test Case Failed"
        elif listDivide([1,2,3,4,5],divide=1)!=5:
            return "Test Case Failed"
