def inverse(num):
    try:
        nums = float(num)
        if nums.is_integer() and nums > 0:
            ans = int(nums)
            return "Inverse number is: " + str(num[::-1])
        else:
            return(str(num) + " is not a positive integer, exit !!")
    except:
        return(num + " is not a positive integer, exit !!")
result = inverse(input("enter:"))
print(result)