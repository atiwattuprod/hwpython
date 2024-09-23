def main():
    number = input()
    answer = [int(aansw) for aansw in str(number)]
    if sum(answer) == 9:
        print("ใช่")
    else:
        print("ไม่")
main()
