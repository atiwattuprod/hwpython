def Checkinput(n):
    if '' in n:
        raise ValueError("ข้อผิดพลาด: กรุณากรอกรายการสินค้าอย่างน้อยหนึ่งรายการ")
    elif ',' in n[0]:
        raise ValueError("ข้อผิดพลาด: กรุณากรอกชื่อรายการสินค้าที่ถูกต้อง")

def All():
    try:
        input1 = input("กรอกรายการสินค้าที่มีอยู่แล้วในครัว: ").split(', ')
        Checkinput(input1)
        lis1 = set(input1)
        input1 = input("กรอกรายการสินค้าที่ต้องซื้อ: ").split(', ')
        Checkinput(input1)
        lis2 = set(input1)
    except ValueError as error:
        print(error)
        print("-"*30)
    except :
        print("ข้อผิดพลาด: เกิดข้อผิดพลาดที่ไม่ทราบสาเหตุ")
        print("-"*30)
    else:
        print("")
        print(f"รายการสินค้าทั้งหมดที่ต้องมี: {lis1.union(lis2)}")
        print(f"รายการสินค้าที่ซ้ำกัน: {lis1.intersection(lis2)}")
        print(f"รายการสินค้าที่มีอยู่แล้วในครัว ไม่ต้องซื้ออีก: {lis1-lis2}")
        print(f"รายการสินค้าที่ต้องซื้อแต่ไม่มีในครัว: {lis2-lis1}")
        print(f"รายการสินค้าที่ไม่ซ้ำกัน:  {lis1.union(lis2)-lis1.intersection(lis2)}")
        print("-"*30)

def main():
    All()
main()