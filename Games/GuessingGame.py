def numba():
    import random
    num = random.randint(0,21)
    return num

def guess():
    var = int(input('Input a Number: '))
    return var

def check(var,num):
    if num == var:
        print('DINGDINGDINGDING')
        return True
    elif num < var:
        print('>>>>>>>>>>>Number is smaller')
    elif num > var:
        print('>>>>>>>>>>>Number is larger')
    return False

def menu():
    print('Do you wish to play the guessing game?')
    choice = input().upper()
    if choice == 'YES':
        flag = False
        num = numba()
        while flag == False:
            var = guess()
            flag = check(var,num)
    else:
        print('fck off')

menu()
