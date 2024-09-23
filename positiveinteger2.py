def Is_PositiveInteger(num):
    try:
        num = float(num)
        if num.is_integer() and num > 0:
            return int(num)
        else:
            return None
    except ValueError:
        return None

def GreatestCommonDivisor(num1, num2):
    a = Is_PositiveInteger(num1)
    b = Is_PositiveInteger(num2)
    if a is None or b is None:
        return "as is not a positive integer, exit !!!"
    if b == 0:
        return "GCD : " + str(a)
    else:
        return GreatestCommonDivisor2(b, a % b)

def GreatestCommonDivisor2(a, b):
    if b == 0:
        return "GCD : " + str(a)
    else:
        return GreatestCommonDivisor2(b, a % b)

x = input("x: ")
y = input("y: ")
result = GreatestCommonDivisor(x, y)
print(result)
