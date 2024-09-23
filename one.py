def convert(gb):
    print(f"Megabytes (MB) : {(gb * 1024):.2f}")
    print(f"Kilobytes (KB) : {(gb * 1024 * 1024):.2f}")
    print(f"Bytes : {(gb * 1024 * 1024 * 1024):.2f}")
    print(f"Bits : {(gb * 1024 * 1024 * 1024 * 8):.2f}")
convert(float(input("Gigabytes (GB) : ")))