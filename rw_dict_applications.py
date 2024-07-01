#Tasks 1  
# main dictionary 

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}


# edit items to the dictionary 
restaurant_menu["Beverages"] ={"Diet Coke": 1.50, "Sweet Tea":1.75 }

restaurant_menu ["Main Course"]["Steak"] = 17.99

del restaurant_menu["Starters"]["Bruschetta"]


#  print new menu and check for correctness 
print(restaurant_menu)