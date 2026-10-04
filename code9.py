name  =  input("Enter your name : ")

print("Hello, " + name + "!" ,  "Welcome to our smart cafe")
print("Menu :  Coffee($50) , Tea($10) , Cold Coffee($30) , Cold Drink($40) , Milkshake($12)")


choice  =  input("what would you like to order? : ")

if choice == "Coffee":
    print("You have ordered Coffee. The price is $50")
elif choice == "Tea":
    print("You have ordered Tea. The price is $10")
elif choice == "Cold Coffee":
    print("You have ordered Cold Coffee. The price is $30")
elif choice == "Cold Drink":
    print("You have ordered Cold Drink. The price is $40")
elif choice == "Milkshake":
    print("You have ordered Milkshake. The price is $12")
else:
    print("Sorry, we don't have that item on the menu.")    

