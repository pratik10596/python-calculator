# Author: Pratik Pradhan
# Calculator to perform basic operations

# Perform operations using python dictionary
def cal(num1,num2,ch):
    return{
        1 : num1+num2,
        2 : num1-num2,
        3 : num1*num2,
        4 : num1/num2
    }[ch]      

ch=1

while (ch > 0):
    print("Press 1 For Addition")
    print("Press 2 For Subtraction")
    print("Press 3 For Multiplication")
    print("Press 4 For Division")
    print("Press 0 To Quite")

    ch = int(input("Enter Your Choice(1/2/3/4/0): "))
    
    # To stop calculator at anytime
    if(ch == 0):
        print("Calculator Stopped")
        break

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if ch in [1,2,3,4]:
        if (ch == 1):
            print(num1,"+",num2,"=", cal(num1,num2,ch))
        elif(ch == 2):
            print(num1,"-",num2,"=", cal(num1,num2,ch))
        elif(ch == 3):
            print(num1,"*",num2,"=", cal(num1,num2,ch))
        elif(ch == 4):
            print(num1,"/",num2,"=", cal(num1,num2,ch))
    else:
        print("Invalid Choice")
