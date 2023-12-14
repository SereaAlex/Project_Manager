from menu_item import menu_item
from Menu import Menu
import os
import time

def slow_print(text, delay=0.01):
    
    for char in text:
        
        print(char, end='', flush=True)
        time.sleep(delay)
        
    print()

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def PrintMenu(name:str):
    clear_screen()
    LOGO = Menu.GetMenuByName(name).logo
    print(LOGO)
    menu_item.PrintAll(name)

def ChangeMenu(name:str):
    clear_screen()
    menu_item.Curr_Menu = name
    PrintMenu(name)

class SomeFuncs:
    
    
    def Func1():
        
        files = os.listdir()
        
        py_files = [file for file in files if file.endswith('.py')]
        
        if len(py_files) == 0:
               
         print("No .py files found. Please add some .py files to test and try again.")
        
        else:
            
            clear_screen()
            print("""What would you like to test?:""")
            test_input = input("\nTest: ")
            os.system(f"python3 {test_input}")
            print("Test completed! (now back to the toolkit)")
            
    def Func2():
        
        clear_screen()
        print("""Type "create" to create a file or directory, \n or type "code" to just code ^-^""")
        
        create_input = input("\nWhat do you choose?: ")
        
        if create_input == "create":
            
            clear_screen()
            choosing = input("\nFile or directory?: ")
            
            if choosing == "file":
                
                clear_screen()
                name_file = input("\nWhat is the name of the file?: ")
                os.system(f"touch {name_file}")
                print(f"\nYour file named {name_file} was created!")
                
            elif choosing == "directory" or choosing == "dir":
                
                clear_screen()
                name_directory = input("What is the name of the directory?: ")
                os.system(f"mkdir {name_directory}")
                print(f"\nYour directory named {name_directory} was created!")
        
        if create_input == "code": 
            
            clear_screen()
            code_input = input("What would you like to code?: ")
            os.system(f"code {code_input}")
            
            finnish_input = input("Done coding? Amazing! Now press enter to go back to the toolkit...\n")
    def Func3():
        
        ChangeMenu("HelpMenu")
    def Func4():
        
        exit()
        
    def TextPurposes():
        pass
    
    def Home():
        
        ChangeMenu("MainMenu")
    
def InitMenuItems():
    
    option1 = menu_item("Testing",SomeFuncs.Func1,"MainMenu")
    option2 = menu_item("Create and code",SomeFuncs.Func2,"MainMenu")
    option3 = menu_item("Help",SomeFuncs.Func3,"MainMenu")
    option4 = menu_item("Exit",SomeFuncs.Func4,"MainMenu")

def InitHelpItems():
    
    option1 = menu_item("Type \"rm\" to remove files or directories",SomeFuncs.TextPurposes,"HelpMenu")
    option2 = menu_item("Type \"ls\" to list files or directories",SomeFuncs.TextPurposes,"HelpMenu")
    option3 = menu_item("Type \"mv\" to change path or rename files or directories",SomeFuncs.TextPurposes,"HelpMenu")
    option4 = menu_item("Type \"pwd\" to check in which directory that you are",SomeFuncs.TextPurposes,"HelpMenu")
    option5 = menu_item("Type \"cd\" to change directories",SomeFuncs.TextPurposes,"HelpMenu")
    option6 = menu_item("Type \"clear\" to clear the screen ^-^",SomeFuncs.TextPurposes,"HelpMenu")
    option7 = menu_item("Home",SomeFuncs.Home,"HelpMenu")

clear_screen()
Menu.InitAllMenues()
InitHelpItems()
InitMenuItems()
PrintMenu("MainMenu")

while True:
    
    user_input = input("Type: ")
    menu_item.TryExec(user_input)
