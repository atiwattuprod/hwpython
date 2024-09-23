def DirectProof(num):
    a = sum(range(1,num + 1))
    b = (num*(num + 1))/2
    c = a == b
    print("Actual sum = " + str(a))
    print("Sum from formula = " + str(int(b)))
    print("Results : " + str(c))
DirectProof(int(input("Input : ")))