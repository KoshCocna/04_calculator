from calcArt import logo

print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

calc = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

flag = 'y'
num1 = int(input('enter the first number: '))

while flag == 'y':

    for op in calc:
        print(op)

    oper = input('enter the operator: ')

    num2 = int(input('enter the second number: '))

    calcFunc = calc[oper]

    res = calcFunc(num1, num2)
    print(f"{num1} {oper} {num2} = {res}")

    flag = input("enter the 'y', if you want to continue, if not, enter the 'n': ")

    if flag == 'y':
        num1 = res
