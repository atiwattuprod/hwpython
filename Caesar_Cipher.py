def CaesarCipher():
    bool = True
    while(bool):
        e_d_q = input("กด e เข้ารหัส กด d ถอดรหัส กด q ออกจากโปรแกรม\n")
        bool = not(e_d_q == 'q')
        if e_d_q == 'e':
            CaesarCipher_e()
        elif e_d_q == 'd':
            CaesarCipher_d()

def CaesarCipher_e():
    words1 = input("กรอกข้อความที่ต้องการเข้ารหัส\n")
    words = words1.split(' ')
    num = int(input("กรอกจำนวนตัวอักษรที่ต้องการเลื่อน\n"))
    re = ""
    for word in words:
        result = ""
        for char in word:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                result += chr((ord(char) + num -shift) % 26 +shift)
            elif char.isnumeric():
                result += str((int(char)-num) % 10)
            else:
                result += char
        re += result[::-1] + " "
    print(words1,"ถูกเข้ารหัสเป็น:",re)

def CaesarCipher_d():
    words1 = input("กรอกข้อความที่ต้องการถอดรหัส\n")
    words = words1.split(' ')
    num = int(input("กรอกจำนวนตัวอักษรที่ต้องการเลื่อน\n"))
    re = ""
    for word in words:
        result = ""
        for char in word:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                result += chr((ord(char) - num -shift) % 26 +shift)
            elif char.isnumeric():
                result += str((int(char)+num) % 10)
            else:
                result += char
        re += result[::-1] + " "
    print(words1,"ถูกถอดรหัสเป็น:",re)

def main():
    CaesarCipher()
main()