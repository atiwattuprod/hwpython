user = input("input: ")
try:
    user = int(user)
    print(user * 3)
except ValueError:
    print(user,user,user)
