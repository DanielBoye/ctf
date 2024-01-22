# Decimal to Binary
def decimal_to_binary(decimal):
    binary = bin(int(decimal * 1000000))[2:]
    return binary

# Binary to Decimal
def binary_to_decimal(binary):
    decimal = int(binary, 2) / 1000000.0
    return decimal

decimal_numbers = [
    0.000020009, 
    0.00019001, 
    0.00011001,
    0.00006001,
    0.000280009, 
    0.000280009,
    0.000090004,
    0.000220005, 
    0.000290005, 
    0.00000001, 
    0.000350005, 
    0.000160009, 
    0.000050007, 
    0.000250009, 
    0.000210011, 
    0.000330004, 
    0.000270011, 
    0.00003001, 
    0.000120009, 
    0.00024001, 
    0.00001001, 
    0.000200005, 
    0.000140004, 
    0.000100004, 
    0.000310005, 
    0.000360012, 
    0.000260004, 
    0.000230011, 
    0.000320011, 
    0.00034001, 
    0.000070009, 
    0.000040012, 
    0.000170005, 
    0.000300011, 
    0.00008001, 
    0.000150009, 
    0.000180011, 
    0.00013001, 
]

# Convert decimal to binary and vice versa
for decimal in decimal_numbers:
    binary = decimal_to_binary(decimal)
    converted_decimal = binary_to_decimal(binary)
    print(binary, end=" ")
