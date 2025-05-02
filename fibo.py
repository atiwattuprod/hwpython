"""main"""
import time , os , random

def fibonacci(n1, memo={}):
    """fibonacci with memoization"""
    if n1 in memo:
        return memo[n1]
    if n1 == 0:
        return 0
    if n1 == 1:
        return 1
    memo[n1] = fibonacci(n1 - 1, memo) + fibonacci(n1 - 2, memo)
    return memo[n1]

def main():
    """main"""
    q = 0
    inpt = input("Choose difficulty level (1 = Easy, 2 = Medium, 3 = Hard): ")
    for i in range(3):
        level = {"1":10 ,"2":20 , "3":30}
        num = random.randint(1 , level[inpt]-4)
        lis = [fibonacci(item) for item in range(1,level[inpt]+1)]
        print(f"Remember this sequence: {lis[num:num+5]}")
        time.sleep(5)
        os.system('cls')
        lis2 = map(int,input("Remember this sequence: ").split())
        for i in lis2:
            ans = i == lis[num]
            num += 1
        q += 1 if ans ==  True else 0
        if ans == True:
            print("Correct!")
        else:
            print(f"Wrong! The correct sequence was {lis[num:num+5]}")
    print(f"You guessed correctly in {q} out of 3 rounds.")
main()

