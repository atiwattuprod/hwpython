def multiplication(a):
    bool = True
    i = 12
    while bool:
        ans = a * i
        print(f"{a} * {i} = {ans}")
        i -= 1
        if i == 0:
            bool = False
def main():
        num = int(input("Enter the multiplication table you want: "))
        multiplication(num)
main()
