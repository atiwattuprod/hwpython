import math

def Concentration():
    C0 = float(input("ปริมาณยาเริ่มต้น: "))
    e = 2.71828
    half_life = int(input("ครึ่งชีวิตของยา: "))
    time = int(input("ระยะเวลาที่คำนวณ: "))
    interval = 2
    k = math.log(2) / half_life
    print("\nความเข้มข้นของยาตามเวลา:\nเวลา (ชั่วโมง) | ความเข้มข้น (มิลลิกรัม)")
    print("-----------------------------------")
    for i in range(0,time+2,interval):
        C = C0 * e**(-k*i)
        print(f"    {i}|    {C:.2f}")
    print(f"\nเวลาที่ความเข้มข้นลดลงครึ่งหนึ่ง: {half_life} ชั่วโมง")
Concentration()
