# Program to Add, Subtract, Multiply and Divide Numbers
# Authored by Srijtih A

while True:    
    choice = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")

    if choice == '1':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        sum = n1 + n2
        print("The sum is:",sum)

    elif choice == '2':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        diff = n1 - n2
        print("The difference is:",diff)
    
    elif choice == '3':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        prod = n1 * n2
        print("The product is:",prod)
    
    elif choice == '4':
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        div = n1 / n2
        print("The quotient is:",div)
    
    elif choice == '5':
        break
    
    else:
        print("Enter correct choice!!")
