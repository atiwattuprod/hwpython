import math
def calculate_angles(**x:float)-> float:
    """คำนวณมุม A, B และ C"""
    A = (x['b']**2 + x['c']**2 -x['a']**2) / (2*x['b']*x['c'])
    B = (x['a']**2 + x['c']**2 -x['b']**2) / (2*x['a']*x['c'])
    C = (x['a']**2 + x['b']**2 -x['c']**2) / (2*x['b']*x['a'])
    angle_A = math.degrees(math.acos(A))
    angle_B = math.degrees(math.acos(B))
    angle_C = math.degrees(math.acos(C))
    print(f"Angle A = {angle_A:.2f}")
    print(f"Angle B = {angle_B:.2f}")
    print(f"Angle C = {angle_C:.2f}")
    sum_of_angles(angle_A,angle_B,angle_C)

def sum_of_angles(*y:float)-> float:
    result = sum(y) == 180
    print("Sum of internal angles = 180.00\nIs the sum equal to 180?:",result)

calculate_angles(a = 12,b = 7,c = 8)
