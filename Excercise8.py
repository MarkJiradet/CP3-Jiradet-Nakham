username = input("Username : ")
password = input("Password : ")

if username == "Mark":
    if password == "1234":
        print("Welcome to Babe Shop!")
        print("======================")
        print("1. Apple 1  = 20 Baht")
        print("2. Banana 1 = 15 Baht")
        print("3. Orange 1 = 10 Baht")
        print("======================")
        choose = int(input("Please select a product list : "))
        if choose == 1:
            apple = int(input("How much do you want?: "))
            print("Apple",apple,"=",20*apple,"Baht")
        elif choose == 2:
            banana = int(input("How much do you want?: "))
            print("Banana",banana,"=",15*banana,"Baht")
        elif choose == 3:
            orange = int(input("How much do you want?: "))
            print("Orange",orange,"=",10*orange,"Baht")
        else:
            print("Please Enter number (1,2,3)!")
    else:
        print("Wrong Password!")
else:
    print("Can't Login! Wrong username")