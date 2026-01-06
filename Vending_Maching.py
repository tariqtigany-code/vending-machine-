def vending_machine():
 #define the dictonary of snacks     
 Snacks = {
    "01":{"item":"Chocolate"         ,"price": 3.50},
    "02":{"item":"Sweets"            ,"price": 1.50},
    "03":{"item":"Mint Gum"          ,"price": 1.00},
    "04":{"item":"Chips "            ,"price": 2.00},
    "05":{"item":"Packaged Pastries ","price":3.00 }
 } 
#define the dictonary of Drinks 
 Drinks ={
    "00":{"item":"Water"     , "price":1.00},
    "11":{"item":"Pepsi"     , "price":2.50},
    "22":{"item":"Hot Coffe" , "price":5.50},
    "33":{"item":"Tea"       , "price":2.50},
    "44":{"item":"Ice Coffe ", "price":7.50}
        }

    
 print("________________________________________")
 print("|||  Welcome to the Vending Machine  |||") 
 print("________________________________________")

 print("|||           MENU                   |||")

 while True :
    

#display the menu of Snacks
#ljust()is a string method in Python used to left-align a string and pad it on the right with spaces (or another character) until it reaches a specified length.
  print("\nSnacks : ".ljust(35)) 
  print("Code".ljust(10) +"|"+" Item".ljust(18)+"|"+"  Price")
  print("-------------------------------------")

  for code in Snacks :
    name=Snacks[code]["item"]
    price=str(Snacks[code]["price"])

    print(code.ljust(10) + "|" + name.ljust(18)+ "| $ " + price + " "+"SAR")
 #diplay the menu of Drinks    
  print("\nDrinks : ")
  print("Code".ljust(10) +"|"+" Item".ljust(18)+"|"+"  Price")
  print("-------------------------------------")

  for code in Drinks :
    name=Drinks[code]["item"]
    price=str(Drinks[code]["price"])

    print(code.ljust(10) + "|" + name.ljust(18)+ "| $ " + price + " "+"SAR")
  item = None
#Get the user  selection 
  choose =input("\nEnter the item code :   ")
  if not choose.isdigit(): #Make sure that enter number not letter 
     print("Not Succesed .Please enter numbers only ,not letters")
    #search for the select item of Snacks
  elif choose in Snacks :
     item=Snacks[choose]
     #search for the select item of Drinks
  elif choose in Drinks :
     item=Drinks[choose]
  else : 
     print("this number not found in our menu")
#Process the payment if a vaild item selected  
  if item  :
     price=item["price"]
     print(f"\n You Selected :[{item["item"]}] =  Price : ${price:.2f} SAR")
     try:
        #Get payment amount from user 
        pay=float(input("Insert money: "))
        #check the user provide enough money
        if pay>=price:
            change=pay -price 
            print(f"\nHere's your {item['item']}")
            print(f"Your change is : ${change :.2f} SAR ")
        else :
            #inform the user if money is not enough  
            print(f"Not enough money , you need to pay $ {price - pay:.2f}or more ")
     except ValueError :
        #INFORM THE USER IF PUT NON -numerical input
        print("WRONG !! , PLEASE ENTER A VAILD NUMBER FOR PAYMENT")
  again = input("\nWould you like to buy another item? (yes/no): ").strip().lower()
  if again != 'yes' and again != 'y':
   print("Thank you for using our Vending Machine. Goodbye!")
   break
#call the function to start the program 
if __name__=="__main__":
   vending_machine()


