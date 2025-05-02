def Harshad_Number(a):
    digits = [int(digit) for digit in str(a)]
    sumdigit = sum(digits)
    return a % sumdigit == 0
def main():
    j = 1
    for i in range(1,101):
        if Harshad_Number(i):
            print(i,end = " ")
            if j%10 == 0:
                print()
            j += 1
main()