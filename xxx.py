def test1():
    n1 = 35
    D = 5
    E = 5
    RSA(20,D,n1)

def RSA(M,E,n):
    print((M**E)%n)

def main():
    print((20**5)%35)
    test1()
main()