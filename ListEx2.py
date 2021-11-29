menuList = []
def showBill():
    print("------- My Food -------")
    sum = 0
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1],"THB")
        sum += menuList[i][1]
    print("-----------------------")
    print("Total Price : %.2f THB"%(sum))
        
        
while True:
    menuName = input("Please Enter Menu : ")
    menuPrice = float(input("Price : "))
    menuList.append([menuName,menuPrice])
    a = input("Do you want to continue? (y/n) : ")
    if a.lower() == "n":
        break
        
showBill()