def main():
    for i in range(ord('a'), ord('z') + 1):
        if (i-1)%5 != 0:
            print(f"{chr(i)} = {i}",end = '\t')
        else:
            print(f"{chr(i)} = {i}")
main()
