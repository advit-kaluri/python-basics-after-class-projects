base = int(input("enter the base number : "))
exponent = int(input("enter the power (n): "))

result = 1

for i in range(exponent):
    result *= base
    print (f"the result is: {result} " )