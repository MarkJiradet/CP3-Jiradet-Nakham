def login():
    while True:
        username = input("Username : ")
        password = input("Password : ") 
        if username =="admin" and password == "1234":
            return True
        print("Wrong! Input again")
        
def showMenu():
    print("="*20)
    print(" 1.Vat Calculator")
    print(" 2.Price Calculator")
    print("="*20)
def menuSelect():
    userSelected = int(input("Please select the function you want : "))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice*vat/100)
    return result

def priceCalculate():
    price1 = float(input("First Product Price : "))
    price2 = float(input("Second Product Price : "))
    return vatCalculate(price1+price2)

if login() == True:
    showMenu()
    userselect = menuSelect()
    if userselect == 1:
        a = int(input("Enter your price : "))
        print("Vat is",vatCalculate(a))
    elif userselect == 2:
        print("The price you have to pay :",priceCalculate())
        
    
