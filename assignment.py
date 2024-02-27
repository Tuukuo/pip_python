def add  (x,y):
    #This function is used for adding two numbers
    return x + y

def subtract (x,y):
    #This function is used for subtracting two numbers
    return x - y

def multiply (x,y):
    #This function is used for multiplying two numbers
    return x * y

def divide (x,y):
    #This function is used for dividing two numbers
    return (x / y)
#Take input from the user
print("please select the operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=input("please enter choice 1/2/3/4:")
num_1=int(input("please enter the first number:"))
num_2=int(input("please enter the second number:"))

if choice== '1':
    print(num_1,"+",num_2,"=",add(num_1,num_2))

elif choice=='2':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))

elif choice=='3':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))

elif choice=='4':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))

    

