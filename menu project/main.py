#chatGPT comments

# Importing necessary libraries
import lib 
import os

# Initializing variables
amount = 0
user_input = 0

# Displaying welcome message
lib.welcome_text()
input("\n      Press Any Key To Start ")

# Initializing menu type variable
menu_type = 0

# Initializing ordering loop
ordering = True

# Ordering loop
while ordering:
  
  # Displaying main menu options
  if menu_type == 0:
    lib.menu_text()
    lib.return_sections()
    menu_type = 1
    
  # Handling user input for main menu options
  if menu_type == 1:
    user_input = input("\n")
    
    # If user selects "breakfast"
    if user_input == "breakfast":
      lib.breakfast_text()
      lib.print_d(lib.menu_call(user_input))
      menu_type = 2
      
    # If user selects "desserts"
    if user_input == "desserts":
      lib.desserts_text()
      lib.print_d(lib.menu_call(user_input))
      menu_type = 3
      
    # If user selects "beverages"
    if user_input == "beverages":
      lib.beverages_text()
      lib.print_d(lib.menu_call(user_input))
      menu_type = 4
      
    # If user selects "total"
    if user_input == "total":
      lib.thanks_text()
      print("total due: " + str(amount))
      ordering = False

  # Handling user input for breakfast items
  if menu_type == 2:  
    print("\nselect the item or type (back) to go to the section select")
    user_input = input()
    
    # If user selects "back"
    if user_input == "back":
      menu_type = 0
    else:
      breakfast = lib.menu_call("breakfast")
      amount += breakfast[user_input]
      
  # Handling user input for desserts items
  if menu_type == 3:  
    print("\nselect the item or type (back) to go to the section select")
    user_input = input()
    
    # If user selects "back"
    if user_input == "back":
      menu_type = 0
    else:
      desserts = lib.menu_call("desserts")
      amount += desserts[user_input]
      
  # Handling user input for beverages items
  if menu_type == 4:   
    print("\nselect the item or type (back) to go to the section select")
    user_input = input()
    
    # If user selects "back"
    if user_input == "back":
      menu_type = 0
    else:
      beverages = lib.menu_call("beverages")
      amount += beverages[user_input]
