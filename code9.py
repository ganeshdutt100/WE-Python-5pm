name  =  input("Enter your name : ")

print("Hello, " + name + "!" ,  "Welcome to our smart cafe")
print("Menu :  Coffee($50) , Tea($10) , Cold Coffee($30) , Cold Drink($40) , Milkshake($12)")


choice  =  input("what would you like to order? : ")

if choice == "Coffee":
   price  = 50
elif choice == "Tea":
   price = 10
elif choice == "Cold Coffee":
   price = 30
elif choice == "Cold Drink":
   price = 40
elif choice == "Milkshake":
   price = 12
else:
    print("Sorry, we don't have that item on the menu.")    
    price = 0

if price > 0 :
    quantity  =  int(input("How many would you like to order? : "))
    total_price  =  price * quantity
    print("Your total bill is: $" + str(total_price))
