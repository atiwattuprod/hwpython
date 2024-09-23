def display_results(*y :float) -> float:
    """แสดงผลลัพธ์การคำนวณดอกเบี้ยทบต้น"""
    print(f"เงินต้น {y[0]:.2f} บาท")
    print(f"อัตราดอกเบี้ย {y[1]:.2f}% ต่อปี")
    print(f"ระยะเวลา {y[2]} ปี")
    print(f"จำนวนเงินสุดท้าย {y[3]:.2f} บาท")
    print(f"ดอกเบี้ยที่ได้รับ {(y[3] - y[0]):.2f} บาท")

def calculate_compound_interest(**x :float) -> float:
    """คำนวณดอกเบี้ยทบต้น"""
    p = x['principal']
    r = x['rate']
    n = x['years']
    a = p*((1 + r/100)**n)
    display_results(p,r,n,a)

result = calculate_compound_interest(principal=50000, rate=3, years=10)