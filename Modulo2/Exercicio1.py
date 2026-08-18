def multiplys(*args):
    total = 1
    for number in args:
        total *= number
    return total 

number_to_multiply = multiplys(2,4,5,6,7,8,9,10)
print(number_to_multiply)

def isEvenOrOdd(numero):
    if numero % 2 == 0:
        print(f'{numero} Is even')
        return True
    print(f'{numero} Is odd')
    return False

isEvenOrOdd(92)
isEvenOrOdd(27)