#make fuction
def add(a,b):
    return a+b
def subst(a,b):
    return a-b
def time(a,b):
    return a*b
def div(a,b):
    return a/b

#program 
print("""========================
      Choose The Operation
      1.)add
      2.)subsitution
      3.)times
      4.)divition
      ===========================""")

while True:
    choice=input("Enter Your Choice(1,2,3,4)\t:")

    
    if choice in ("1","2","3","4"):
        num1=float(input("Enter Fist Number:"))
        num2=float(input("Enter Fist Number:"))
        if choice== "1":
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice== "2":
            print(num1,"-",num2,"=",subst(num1,num2))
            
        elif choice== "3":
            print(num1,"*",num2,"=",time(num1,num2))
        elif choice== "4":
            print(num1,"/",num2,"=",div(num1,num2))
        choice=input("You want Continue (Y/N):")
        if choice == "N":
            break
    else:
        print("unvalaibe")