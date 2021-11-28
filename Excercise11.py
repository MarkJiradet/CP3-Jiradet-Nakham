number = int(input("Enter the height of the pyramid : "))
for i in range(number):
    print(" "*(number-i),"*"+(i*"**"))