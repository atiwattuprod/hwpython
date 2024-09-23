import math
def calculate_angles(**x:float)-> float:
    """คำนวณมุม B"""
    sin_b = (math.sin(math.radians(x['sin_a'])) * x['b'])/x['a']
    angle_b = math.degrees(math.asin(sin_b))
    print(f"มุม B ประมาณ {angle_b:.2f} องศา")
calculate_angles(sin_a = 30,b = 3.41,a = 2.5)