menuList = []
priceList = []

def showBill():
    print("----- My Food -----")
    sum = 0
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        sum += priceList[i]
    print("Total Price = %.2f"%(sum))
        
        
while True:
    menuName = input("Please Enter Menu : ")
    menuPrice = float(input("Price : "))
    menuList.append(menuName)
    priceList.append(menuPrice)
    a = input("Do you want to continue? (y/n) : ")
    if a.lower() == "n":
        break
        
showBill()