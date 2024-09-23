def matchCase(op,num1,num2):
    if op == 1:
        return f"{num1:.2f} + {num2:.2f} = {num1 + num2:.2f}"
    elif op == 2:
        return f"{num1:.2f} - {num2:.2f} = {num1 - num2:.2f}"
    elif op == 3:
        return f"{num1:.2f} * {num2:.2f} = {num1 * num2:.2f}"
    elif op == 4:
        return f"{num1:.2f} / {num2:.2f} = {num1 / num2:.2f}"
    elif op == 5:
        return f"{num1:.2f} ** {num2:.2f} = {num1 ** num2:.2f}"
    else:
        return "Please select choice 1-5 only"
    
def start():
    print("############################")
    print("#   Please select choice   #")
    print("############################")
    print("# 1. Plus      (+)         #")
    print("# 2. Minus     (-)         #")
    print("# 3. Multiply  (*)         #")
    print("# 4. Divide    (/)         #")
    print("# 5. Power     (**)        #")
    print("############################")
    a = int(input("Select : "))
    b = float(input("\nEnter number 1 : "))
    c = float(input("Enter number 2 : "))
    print(matchCase(a,b,c))

start()