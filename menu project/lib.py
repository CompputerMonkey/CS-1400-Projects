import os


# menu functions
def menu_call(section_select):
  menu = {"breakfast" : {"pancakes" : 2.99, "eggs & bacon" : 1.99, "waffles" :  3.99},
          "desserts" : {"icecream" : 2.99, "cake" : 4.99, "shake" : 4.99},
          "beverages" : {"root-beer" : 1.99, "water" : 0, "orange juice" : 0.99}
        }
  return menu[section_select]


def return_sections():
  print("here are the different food sections\n")
  print("type breakfast, desserts, beverages or type (total) to go to pay screen")
#end of menu functions


# printing dictionarys
def print_d(dictionary):
    dict_string = ""
    for key, value in dictionary.items():
        dict_string += f"{key}: {value}, "
    dict_string = dict_string[:-2]  # remove the final ", "
    print(dict_string)
# end of printing


# misc 

def welcome_text():
  print("__          __  _ \n\ \        / / | | \n \ \  /\  / /__| | ___ ___  _ __ ___   ___  \n  \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ \n   \  /\  /  __/ | (_| (_) | | | | | |  __/\n    \/  \/ \___|_|\___\___/|_| |_| |_|\___|")

def menu_text():
  os.system("clear")
  print("  _ __ ___   ___ _ __  _   _ \n | '_ ` _ \ / _ \ '_ \| | | | \n | | | | | |  __/ | | | |_| | \n |_| |_| |_|\___|_| |_|\__,_|\n")

def breakfast_text():
  os.system("clear")
  print(" _                    _     __          _   \n| |                  | |   / _|        | |\n| |__  _ __ ___  __ _| | _| |_ __ _ ___| |_ \n| '_ \| '__/ _ \/ _` | |/ /  _/ _` / __| __|\n| |_) | | |  __/ (_| |   <| || (_| \__ \ |_ \n|_.__/|_|  \___|\__,_|_|\_\_| \__,_|___/\__|\n")

def desserts_text():
  os.system("clear")
  print("      _                         _\n     | |                       | |\n   __| | ___  ___ ___  ___ _ __| |_\n  / _` |/ _ \/ __/ __|/ _ \ '__| __|\n | (_| |  __/\__ \__ \  __/ |  | |_ \n  \__,_|\___||___/___/\___|_|   \__|\n")

def beverages_text():
  os.system("clear")
  print(" _\n| |\n| |__   _____   _____ _ __ __ _  __ _  ___  ___ \n| '_ \ / _ \ \ / / _ \ '__/ _` |/ _` |/ _ \/ __|\n| |_) |  __/\ V /  __/ | | (_| | (_| |  __/\__ \ \n|_.__/ \___| \_/ \___|_|  \__,_|\__, |\___||___/\n                                 __/ |\n                                |___/\n")

def thanks_text():
  os.system("clear")
  print(" _______ _                 _\n|__   __| |               | |\n   | |  | |__   __ _ _ __ | | _____\n   | |  | '_ \ / _` | '_ \| |/ / __|\n   | |  | | | | (_| | | | |   <\__ \ \n   |_|  |_| |_|\__,_|_| |_|_|\_\___/\n")
# end of misc 