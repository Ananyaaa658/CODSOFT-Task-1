while True:
    def add(x,y):
        sum=x+y
        return sum
    def subtract(x,y):
        diff=x-y
        return diff
    def multiply(x,y):
        product=x*y
        return product
    def division(x,y):
        quotient=x/y
        return quotient
    def mod(x,y):
        remainder=x%y
        return remainder
    num1=int(input("Enter value 1:"))
    num2=int(input("Enter value 2:"))
    print("Choose the operation you want to pwrform:")
    print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Divison \n5. Modulus ")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        print("Sum-", num1,"+",num2,"=", add(num1,num2))
    elif(choice==2):
        print("Difference-", num1,"-",num2,"=", subtract(num1,num2))
    elif(choice==3):
        print("Product-", num1,"*",num2,"=", multiply(num1,num2))
    elif(choice==4):
        print("Quotient-", num1,"/",num2,"=", division(num1,num2))
    else:
        print("Remainder-", num1,"%",num2,"=", mod(num1,num2))

    calculate_again=input("Calculate again(yes/no): ")
    if(calculate_again=="no"):
        break
