import sys

if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
elif len(sys.argv) == 2 or len(sys.argv) > 3:
    print("Error: Dame dos argumento, por favor, ni mas ni menos")
elif sys.argv[1].isalpha() == True or sys.argv[2].isalpha() == True:
    print('Error: los numeros deben ser enteros')
else: 
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print('Sum:\t\t', (a + b))
    print('Difference:\t', (a - b))
    print('Product:\t', (a * b))
    if (b == 0):
        print('ERROR (division by zero)')
    else:
        print('Quotient:\t', (a / b))
    if (b == 0):
        print('ERROR (modulo by zero)')
    else:
        print('Remainder:\t', (a % b)) 

    
