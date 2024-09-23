def three(num):
    a = (2 ** (num -1)) % num == 1
    b = num % 561 != 0
    c = num % 1105 != 0 
    d = num % 1729 != 0
    x = a & b & c & d
    print("Prime : " + str(x))
three(int(input("Input : ")))
