from Fubbi import Fubbi

one = Fubbi()
two = Fubbi()
three = Fubbi()
four = Fubbi()

testOne = [0,1,3,4,5,2,6,7,10,8,9]
testOneCorrect = "0,1,2,3,4,5,6,7,8,9,10,j,"
testTwo = [1,2,2,3,4,5,10,11,9,7,8,12]
testTwoACorrect  = "1,2,4,5,6,j,10,12,9,7,11,8,"
testTwoBCorrect = "1,2,4,5,6,7,8,9,10,11,12,j,"
testFour = [9,8,6,1,11]
testFourCorrect = "5,6,7,8,9,10,11,12,j,2,8,1,9,4,1,6,11,"

def runOne ():
    correct = " False"
    for value in testOne:
        one.insert(value)
    if():
        correct = " True"
    return f'Testing Insert(), Junk_Add(), Junk_Check(): {one.export()} -> {one.export() == (testOneCorrect)}'


def runTwo ():
    out  = ""
    for value in testTwo:
        two.insert(value)
    two.remove(1)
    two.remove(2)
    two.insert(6)
    out = f'Testing Remove():{two.export()} -> {two.export() == testTwoACorrect}'
    two.junk_junk(10)
    out += f'\nTesting Junk_Junk(): {two.export()} -> {two.export() == testTwoBCorrect}'

    return out

def runThree():
    out = ""
    three.remove(1000)
    out += f'Testing Remove Blank, Linear_Search(): {three.linear_search(1000)} -> {three.linear_search(1000) == 0}'
    three.overwrite(two.export())
    out += f'\nTesting Overwrite(): {three.export()} -> {three.export() == testTwoBCorrect}'

    return out

def runFour():
    for value in testFour:
        four.insert(value)

    four.union(two)

    return f'Testing Union(): {four.export()} -> {four.export() == testFourCorrect}'


print(runOne())
print(runTwo())
print(runThree())
print(runFour())

