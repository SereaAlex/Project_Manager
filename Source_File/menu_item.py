from doctest import OPTIONFLAGS_BY_NAME
import os
from termcolor import colored
import inquirer
import Menu
import time
def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.01):
    
    for char in text:
        
        print(char, end='', flush=True)
        time.sleep(delay)
        
    print()

def PrintMenu(name:str):
    clear_screen()
    LOGO = Menu.GetMenuByName(name).logo
    slow_print(LOGO,delay=0.001)
    menu_item.PrintAll(name)

def ChangeMenu(name:str):
    clear_screen()
    menu_item.Curr_Menu = name
    PrintMenu(name)

def Home():
        
    ChangeMenu("MainMenu")

class SomeOtherFuncs:
    def Func5():
        
        clear_screen()
        rm_input = inquirer.list_input("Do you want to remove a file or a directory?: ", choices = ['file', 'directory'])
        
        if rm_input == "file":
            os.system('ls')
            rm_file_input = input("\nName: ")
            os.system(f"rm {rm_file_input}")
            print(f"The file named {rm_file_input} was removed.")
        
        if rm_input == "directory":
            os.system('ls')
            rm_directory_input = input("\nName: ")
            os.system(f"sudo rm -r {rm_directory_input}")
            print(f"The directory named {rm_directory_input} was removed.")
            close = input("Press enter to get home..")
            ChangeMenu('MainMenu')
    
    def Func6():
    
        os.system("ls")
    
    def Func7():
        clear_screen()
        print(colored(f"You are in: {menu_item.Curr_Menu}",'light_yellow'))
    
    def Func8():
        
        os.system("pwd")
        
    def Func9():
        
        path_input = input("Enter the full path of the file/folder that you would like to move:\n")
        dest_path_input = input("\nEnter the destination folder's full path:\n")
        os.system(f"mv {path_input} {dest_path_input}")
    
    def Func10():
        
        cd_input = inquirer.list_input("Which direction would you like to move",choices = ['back','forward']) 
        if cd_input == "back":
                
            os.chdir("..")
            os.system("pwd")
        
        elif cd_input == "forward":
            questions = [
                inquirer.List('dir',
                message="Where",
                choices= os.listdir(),
            )]
            answers = inquirer.prompt(questions)
            os.chdir(answers['dir'])
            os.system("pwd")
    
    def Func11():
        edit_choice = inquirer.list_input('What do you want to edit', choices = os.listdir())
        os.system(f'nano {edit_choice}')

class menu_item:
    ## Variabilele statice
    lista_de_instante = []
    Curr_Menu = "MainMenu"

    def __init__(self, name: str, funct, InWhichMenu:str):
        self.name = name
        self.funct = funct
        self.InWhichMenu = InWhichMenu
        menu_item.lista_de_instante.append(self)

    def PrintAll(InWhichMenu:str):
        if len(menu_item.lista_de_instante) == 0:
            return

        i = 0
        for option in menu_item.lista_de_instante:
                if option.InWhichMenu == InWhichMenu:
                    print(f"[{i + 1}] " + option.name)
                    i += 1

    def TryExec(user_input: str):
        try:
            ## Get all the menu items from the current menu:
            CurrOptions = []
            for option in  menu_item.lista_de_instante:
                if option.InWhichMenu == menu_item.Curr_Menu:
                    CurrOptions.append(option)
            ## Exec by index
            option_index = int(user_input) - 1
            if 0 <= option_index < len(CurrOptions):
                CurrOptions[option_index].funct()
            else:
                print("Invalid option number!")
        except:
            ## Exec by name
            for option in CurrOptions:
                if option.name == user_input:
                    option.funct()
                    return
            ##
            if user_input == "rm":
                SomeOtherFuncs.Func5()
            elif user_input == "ls":
                SomeOtherFuncs.Func6()
            elif user_input == "clear":
                SomeOtherFuncs.Func7()
            elif user_input == "pwd":
                SomeOtherFuncs.Func8()
            elif user_input == "mv":
                SomeOtherFuncs.Func9()
            elif user_input == "cd":
                SomeOtherFuncs.Func10()
            elif user_input == "edit":
                SomeOtherFuncs.Func11()
            else:
                print("Command not found!")
                    

