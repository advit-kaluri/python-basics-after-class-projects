decimal_num = int(input("enter a decimal number (or -1 to exit)"))

if decimal_num == -1:
    break


if decimal_num == 0:
    print("Binary: 0")
    continue

binary_str=""
temp_num = decimal_num

while temp_num > 0:
    remainder = temp_num % 2
    binary_str = str(remaineder)+ binary_str
    temp_num = temp_num // 2

    print(f"The binary representation of {decimal_num} is : {binary_str}")

