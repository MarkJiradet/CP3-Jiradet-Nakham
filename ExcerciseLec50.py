def Addnumber(x,y):
    print(x,"+",y,"=",x+y)
def SubtractNumber(x,y):
    print(x,"-",y,"=",x-y)
def MultiplyNumber(x,y):
    print(x,"x",y,"=",x*y)
def DivideNumber(x,y):
    print(x,"/",y,"=",x/y)

while True:
    x = int(input("Input first number :"))
    y = int(input("Input second number : "))
    print("="*40)
    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    print("="*40)
    choice = int(input("Choose the functionality you want : "))
    if choice == 1:
        Addnumber(x,y)
    elif choice == 2:
        SubtractNumber(x,y)
    elif choice == 3:
        MultiplyNumber(x,y)
    elif choice == 4:
        DivideNumber(x,y)
    ask = input("Do you want to continue? (y/n):")
    if ask == "n":
        break
        
    