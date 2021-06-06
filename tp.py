print("-----------------WELCOME TO OUR RESTURANT------------------")
name = input("Enter your name:")
print("Welcome",name,"to our resturant")
dishes_name = []
price = []
total = 0
print("\nWhat would you like to order:")
print("\n| 1 | ---> Fast Food")
print("\n| 2 | ---> Non-veg")
print("\n| 3 | ---> Vegatarian")
print("\n| 4 | ---> Sweet Dish")
print("\n| 5 | ---> Finish order")
print("\n| 6 | ---> No order")

print("\nLet us know Your choice:")
while(True):
    choice = int(input("Enter your choice:"))
    if (choice == 1):
        orderDict = {"burger":70,"pizza":100,"fries":95,"dabeli":33}
        print("------MENU------")
        print("burger       70rs")
        print("pizza        100rs")
        print("fries        95rs")
        print("dabeli       33rs")
        print("Do u want to order something from this menu:")
        inp = input("Enter yes or no:")
        if inp == "yes":
              inp = input("Enter dishes name as it is and separte dishes name by comma: ").split(",")
              for i in inp:
                  i = i.replace(" ", "")
                  print(i,orderDict[i])
                  dishes_name.append(i)
                  price.append(orderDict[i])
                  
                  
        elif inp == "no":
            print("Thankyou for your reply")
        else:
            print("something invalid response you entered")
          
    elif (choice==2):
        orderDict = {"kabab": 100, "fish":289,"egg":175,"meat":55}
        print("------MENU------")
        print("kabab        100rs")
        print("fish         289rs")
        print("meat         175s")
        print("egg          55rs")
        print("Do u want to order something from this menu:")
        inp = input("Enter yes or no:")
        if inp == "yes":
              inp = input("Enter dishes name as it is and separte dishes name by comma: ").split(",")
              for i in inp:
                  i = i.replace(" ", "")
                  print(i,orderDict[i])  
                  dishes_name.append(i)
                  price.append(orderDict[i])
                  

        elif inp == "no":
            print("Thankyou for your reply")
        else:
            print("something invalid response you entered")
    elif(choice==3):
        orderDict = {"dosa":45,"idli":25,"rice":52,"roll":31}
        print("------MENU------")
        print("dosa           45rs")
        print("idli           25rs")
        print("rice           52rs")
        print("roll           31rs")
        print("Do u want to order something from this menu:")
        inp = input("Enter yes or no:")
        if inp == "yes":
              inp = input("Enter dishes name as it is and separte dishes name by comma: ").split(",")
              for i in inp:
                  i = i.replace(" ", "")
                  print(i, orderDict[i])
                  dishes_name.append(i)
                  price.append(orderDict[i])
                  
                  
        elif inp == "no":
            print("Thankyou for your reply")
        else:
            print("something invalid response you entered")
    elif(choice==4):
        orderDict = {"imarti":80,"barfi":100,"laddu":75,"rabri":98}
        print("------MENU------")
        print("imarti              80rs")
        print("barfi               100rs")
        print("laddu               75rs")
        print("rabri               98rs")
        print("Do u want to order something from this menu:")
        inp = input("Enter yes or no:")
        if inp == "yes":
              inp = input("Enter dishes name as it is and separte dishes name by comma: ").split(",")
              for i in inp:
                  i = i.replace(" ", "")
                  print(i, orderDict[i])  
                  dishes_name.append(i)
                  price.append(orderDict[i])
                  

        elif inp == "no":
            print("Thankyou for your reply")
        else:
            print("something invalid response you entered")
    elif(choice==5):
        print("------Thankyou------")
        print("You have ordered")
        print("-------Bill--------")
        print("ProductName\tPrice")

        for x, y in zip(dishes_name, price):
            print(x,"\t\t ",y)
        print("---------------------------")
        for sum in price:
            total += sum
        print("Total Amount\t\t",total)
        
        print("Have a great day ahead !!!!!!!!!!!!!!!!!!")
        exit(0)
            
    elif(choice==6):
        print("Thankyou For Coming To Our Site ",name)
        print("Have a great day ahead !!!!!!!!!!!!!!!!!!")
        exit(0)
    else:
        print("Invalid input pls enter correct input")
        
        
        
    

        






