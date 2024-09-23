def Is_PositiveInteger(num):
    try:
        nums = float(num)
        if nums.is_integer() and nums > 0:
            ans = int(nums)
            return(str(ans) + " is a positive integer")
        else:
            return(str(num) + " is not a positive integer")
    except:
        return(num + " is not a positive integer")
result = Is_PositiveInteger(input("enter:"))
print(result)


