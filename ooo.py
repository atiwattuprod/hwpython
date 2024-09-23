print("  Transform second ")
x = 0
x = input("Enter seconds : ")
try:
    x = int(x)
    if x >= 0:
        second = x % 60
        mins = x // 60
        hour = mins // 60
        mins = mins % 60
        day = hour // 24
        hour = hour % 24
        week = day // 7
        day = day % 7
        if week > 0 and second > 0:
            print(f"{x:,} seconds ==> {week} weeks {second} seconds")
        elif week > 0:
            print(f"{x:,} seconds ==> {week} weeks ")
        elif day > 0 and day <= 7 and second > 0:
            print(f"{x:,} seconds ==> {day} days {second} seconds")
        elif day > 0 and day <= 7:
            print(f"{x:,} seconds ==> {day} days ")
        elif hour > 0 and hour <= 24 and second > 0:
            print(f"{x:,} seconds ==> {hour} hours {second} seconds")
        elif hour > 0 and hour <= 24:
            print(f"{x:,} seconds ==> {hour} hours")
        elif mins > 0 and hour <= 60 and second > 0:
            print(f"{x:,} seconds ==> {mins} minutes {second} seconds")
        elif mins > 0 and hour <= 60:
            print(f"{x:,} seconds ==> {mins} minutes")
        elif second > 0 and second <= 60:
            print(f"{x:,} seconds ==> {second} seconds")
    else:
        print(f"This number ({x}) is not VALID !!!")
except:
    print(f"! ! ! please enter a whole number ==> {x}")
print(" --- program end ---")