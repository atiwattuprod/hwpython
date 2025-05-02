import math

# 1
def test1():
    lis = [1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14, 1e15, 1e16]
    for i in lis:
        n = float(i)
        re = (1 + 1 / n) ** n
        print(f"(1 + 1/ {n:.0e}) ^ {n:.0e} = {re:.10f}")

# 2
def test2():
    name = ['somchai sombat', 'Atiwat tuprod']
    email = []
    for i  in name:
        name1 = i.lower().split()
        email.append(name1[0] + '.' + name1[1][0:2] + '@kmitl.ac.th')
    print(email)

# 3
def test3(*kwargs, place = 2):
    sums = 0
    for i in kwargs:
        sums += float(i)**2
    ans = math.pow((sums / len(kwargs)), 1/2)
    print(f"{ans:.{place}f}")

# 4
def test4(n, tol=1e-10):
    if n == 0:
        return 0
    
    x = n 
    while True:
        x_new = x - (pow(x,7) - n) / (7 * pow(x,6))
        if abs(x_new - x) < tol:
            break
        x = x_new
    
    print(x)

def pow(a, n):
    ans = a
    for i in range(0,n-1):
        ans *= a
    return ans

# main
def main():
    test1()
    test2()
    test3(1,2,3,place=2)
    test3(0,0,1,1,0,1,0,1,1,1,place=2)
    test4(2097152)
main()