def fact(a):
    ans = 1
    while a != 0:
        ans *= a
        a -= 1
    return ans
def main():
    num = int(input("Please enter a positive integer: "))
    print(f"The factorial of {num} is {fact(num)}")
main()
