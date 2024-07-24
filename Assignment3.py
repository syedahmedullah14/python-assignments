# Function to convert a number into different formats
def convert_number(number):
    binary_format = bin(number)
    octal_format = oct(number)
    hexadecimal_format = hex(number)
    float_format = float(number)
    complex_format = complex(number)
    
    print(f"The binary of the number is {binary_format}")
    print(f"The octal of the number is {octal_format}")
    print(f"The hexadecimal of the number is {hexadecimal_format}")
    print(f"The float of the number is {float_format}")
    print(f"The complex of the number is {complex_format}")

# Input from the user
number = int(input("Enter a number: "))
convert_number(number)
