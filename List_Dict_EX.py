allMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวไก่ทอด":45,"ข้าวมันไก่พิเศษ":45,"ข้าวมันไก่ทอดพิเศษ":50}
menuList = []

def showBill():
    sum = 0
    print("------- My Food -------")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        sum += menuList[i][1]
    print("-----------------------")
    print("Total Price : %.2f บาท"%(sum))

print("***ยินดีต้อนรับสู่ร้านข้าวมันไก่***")
for i in allMenu.keys():
    print("%s  %d บาท"%(i,allMenu[i]))
    
while True:
    menuName = input("Please Enter Menu : ")
    menuList.append([menuName,allMenu[menuName]])
    a = input("Do you want to continue? (y/n) : ")
    if a.lower() == "n":
        break
    
showBill()