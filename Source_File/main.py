from menu_item import menu_item
from Menu import Menu
import os
import time
from colorama import init
from termcolor import colored
import inquirer
import readline
import glob

def custom_completer(text, state):
    matches = glob.glob(text + '*')
    return (matches + [None])[state]

readline.set_completer(custom_completer)
readline.parse_and_bind("tab: complete")

init()

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
    slow_print(LOGO,delay=0.001)
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
            os.system('ls')
            print("""\nWhat would you like to test?:""")
            test_input = input("\nTest: ")
            os.system(f"python3 {test_input}")
            close = input('Press enter to get home..')
            ChangeMenu("MainMenu")
            
    def Func2():
        
        clear_screen()
        print("""Type "create" to create a file or directory, \n or type "code" to just code ^-^""")
        
        create_input = inquirer.list_input('What do you choose?: ', choices = ['create','code'])
        
        if create_input == "create":
            
            clear_screen()
            choosing = inquirer.list_input('File or directory?: ', choices = ['file','directory'])
            
            if choosing == "file":
                
                clear_screen()
                name_file = input("\nWhat is the name of the file?: ")
                os.system(f"touch {name_file}")
                print(f"\nYour file named {name_file} was created!")
                close = input('Press enter to get home..')
                ChangeMenu("MainMenu")
                
            elif choosing == "directory" or choosing == "dir":
                
                clear_screen()
                name_directory = input("What is the name of the directory?: ")
                os.system(f"mkdir {name_directory}")
                print(f"\nYour directory named {name_directory} was created!")
                close = input('Press enter to get home..')
                ChangeMenu("MainMenu")
        
        if create_input == "code": 
            
            clear_screen()
            questions = [
                inquirer.List('py',
                message="What would you like to code",
                choices= os.listdir(),
            )]
            answers = inquirer.prompt(questions)
            os.system(f"code {answers['py']}")
            close = input('Press enter to get home..')
            ChangeMenu("MainMenu")
    def Func3():
        
        ChangeMenu("HelpMenu")
    def Func4():
        slow_print(colored("""
                   
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝""",'light_blue'),0.001)
        clear_screen()
        exit()
        
        
    def TextPurposes():
        
        print('This is for Text Purposes')
    
    def Home():
        
        ChangeMenu("MainMenu")
    
    def About():
        
        ChangeMenu("AboutMenu")
        InitAboutDescription()
def InitMenuItems():
    
    option1 = menu_item("Testing",SomeFuncs.Func1,"MainMenu")
    option2 = menu_item("Create and code",SomeFuncs.Func2,"MainMenu")
    option3 = menu_item("Help",SomeFuncs.Func3,"MainMenu")
    option4 = menu_item("About",SomeFuncs.About,"MainMenu")
    option4 = menu_item("Exit",SomeFuncs.Func4,"MainMenu")

def InitAboutDescription():
    description = (slow_print(f'''
    {colored("This program has been developed by:","yellow")}\n
    -{colored("Serea Alex-Valentin and a big help from Macovei Iulian","cyan")},\n
    {colored("A student of Informatics Engineering at UGAL.",'green')}\n
    \n
    {colored("For any information or feedback, please contact me through:","magenta")}\n
    \n
    Github:\t{colored("https://github.com/SereaAlex","white")}\n
    Email:\t{colored("alex.serea1156@gmail.com","red")}
    ''',delay = 0.001),SomeFuncs.TextPurposes,"AboutMenu")
    option = menu_item("Home",SomeFuncs.Home,"AboutMenu")

def InitHelpItems():
    
    option1 = menu_item("Type \"rm\" to remove files or directories",SomeFuncs.TextPurposes,"HelpMenu")
    option2 = menu_item("Type \"ls\" to list files or directories",SomeFuncs.TextPurposes,"HelpMenu")
    option3 = menu_item("Type \"mv\" to change path or rename files or directories",SomeFuncs.TextPurposes,"HelpMenu")
    option4 = menu_item("Type \"pwd\" to check in which directory that you are",SomeFuncs.TextPurposes,"HelpMenu")
    option5 = menu_item("Type \"cd\" to change directories",SomeFuncs.TextPurposes,"HelpMenu")
    option6 = menu_item("Type \"clear\" to clear the screen ^-^",SomeFuncs.TextPurposes,"HelpMenu")
    option7 = menu_item("Type \"edit\" to edit files",SomeFuncs.TextPurposes,"HelpMenu")
    option8 = menu_item("Type \"mv\" to move or rename files or directories",SomeFuncs.TextPurposes,"HelpMenu")
    option9 = menu_item("Home",SomeFuncs.Home,"HelpMenu")

clear_screen()
Menu.InitAllMenues()
InitHelpItems()
InitMenuItems()
PrintMenu("MainMenu")

while True:
    user_input = input("Type: ")
    menu_item.TryExec(user_input)
