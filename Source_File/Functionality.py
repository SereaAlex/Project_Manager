import os
import inquirer
from Menu import Menu
from menu_item import menu_item
import time
from termcolor import colored
# from main import Display

class Functions(Menu):
    
    def slow_print(text, delay=0.01):
        
        for char in text:
            
            print(char, end='', flush=True)
            time.sleep(delay)
            
        print()

    def clear_screen():
        
        os.system('cls' if os.name == 'nt' else 'clear')

    def PrintMenu(name:str):
        Functions.clear_screen()
        LOGO = Menu.GetMenuByName(name).logo
        Functions.slow_print(LOGO,delay=0.001)
        menu_item.PrintAll(name)

    def ChangeMenu(name:str):
        Functions.clear_screen()
        menu_item.Curr_Menu = name
        Functions.PrintMenu(name)
        
    
    def InitAboutDescription():
        description = (Functions.slow_print(f'''
        {colored("This program has been developed by:","yellow")}\n
        -{colored("Serea Alex-Valentin and a big contribution from Macovei Iulian","cyan")},\n
        {colored("A student of Informatics Engineering at UGAL.",'green')}\n
        \n
        {colored("For any information or feedback, please contact me through:","magenta")}\n
        \n
        Github:\t{colored("https://github.com/SereaAlex","white")}\n
        Email:\t{colored("alex.serea1156@gmail.com","red")}
        ''',delay = 0.001),Options.TextPurposes,"AboutMenu")
        option = menu_item("Home",Options.Home,"AboutMenu")
        
    def InitMenuItems():
        
        option1 = menu_item("Testing",Options.Testing,"MainMenu")
        option2 = menu_item("Create and code",Options.Create,"MainMenu")
        option3 = menu_item("Help",Options.Help,"MainMenu")
        option4 = menu_item("About",Options.About,"MainMenu")
        option4 = menu_item("Exit",Options.Exiting,"MainMenu")

    
    def InitHelpItems():
        
        option1 = menu_item("Type \"rm\" to remove files or directories", Options.TextPurposes,"HelpMenu")
        option2 = menu_item("Type \"ls\" to list files or directories",Options.TextPurposes,"HelpMenu")
        option3 = menu_item("Type \"mv\" to change path or rename files or directories",Options.TextPurposes,"HelpMenu")
        option4 = menu_item("Type \"pwd\" to check in which directory that you are",Options.TextPurposes,"HelpMenu")
        option5 = menu_item("Type \"cd\" to change directories",Options.TextPurposes,"HelpMenu")
        option6 = menu_item("Type \"clear\" to clear the screen ^-^",Options.TextPurposes,"HelpMenu")
        option7 = menu_item("Type \"edit\" to edit files",Options.TextPurposes,"HelpMenu")
        option8 = menu_item("Type \"mv\" to move or rename files or directories",Options.TextPurposes,"HelpMenu")
        option9 = menu_item("Type \"cat\" to read files", Options.TextPurposes,"HelpMenu")
        option10 = menu_item("Home",Options.Home,"HelpMenu")

class Options:
    
    
    def Testing():
        
        files = os.listdir()
        
        py_files = [file for file in files if file.endswith('.py')]
        
        if len(py_files) == 0:
               
         print("No .py files found. Please add some .py files to test and try again.")
        
        else:
            
            Functions.clear_screen()
            questions = [
                inquirer.List('py',
                message="What would you like to test",
                choices= os.listdir(),
            )]
            answers = inquirer.prompt(questions)
            a = answers['py']
            os.system(f"python3 {a}")
            close = input('Press enter to get home..')
            Functions.ChangeMenu("MainMenu")
            
    def Create():
        
        Functions.clear_screen()
        print("""Type "create" to create a file or directory, \n or type "code" to just code ^-^""")
        
        create_input = inquirer.list_input('What do you choose?: ', choices = ['create','code'])
        
        if create_input == "create":
            
            Functions.clear_screen()
            choosing = inquirer.list_input('File or directory?: ', choices = ['file','directory'])
            
            if choosing == "file":
                
                Functions.clear_screen()
                name_file = input("\nWhat is the name of the file?: ")
                os.system(f"touch {name_file}")
                print(f"\nYour file named {name_file} was created!")
                close = input('Press enter to get home..')
                Functions.ChangeMenu("MainMenu")
                
            elif choosing == "directory" or choosing == "dir":
                
                Functions.clear_screen()
                name_directory = input("What is the name of the directory?: ")
                os.system(f"mkdir {name_directory}")
                print(f"\nYour directory named {name_directory} was created!")
                close = input('Press enter to get home..')
                Functions.ChangeMenu("MainMenu")
        
        if create_input == "code": 
            
            Functions.clear_screen()
            questions = [
                inquirer.List('py',
                message="What would you like to code",
                choices= os.listdir(),
            )]
            answers = inquirer.prompt(questions)
            os.system(f"code {answers['py']}")
            close = input('Press enter to get home..')
            Functions.ChangeMenu("MainMenu")
            
    def Help():
        
        Functions.ChangeMenu("HelpMenu")
        
    def TextPurposes():
        
        print('This is for Text Purposes')
    
    def Home():
        
        Functions.ChangeMenu("MainMenu")
    
    def About():
        
        Functions.ChangeMenu("AboutMenu")
        Functions.InitAboutDescription()
        
    def Exiting():
        Functions.slow_print(colored("""
                   
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝""",'light_blue'),0.001)
        Functions.clear_screen()
        exit()
        

