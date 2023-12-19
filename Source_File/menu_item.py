from doctest import OPTIONFLAGS_BY_NAME
import os
from termcolor import colored
import inquirer
from Menu import Menu
import time


class Settings:

    def clear_screen():
        
        os.system('cls' if os.name == 'nt' else 'clear')

    def slow_print(text, delay=0.01):
        
        for char in text:
            
            print(char, end='', flush=True)
            time.sleep(delay)
            
        print()

    def PrintMenu(name:str):
        Settings.clear_screen()
        LOGO = Menu.GetMenuByName(name).logo
        Settings.slow_print(LOGO,delay=0.001)
        menu_item.PrintAll(name)

    def ChangeMenu(name:str):
        Settings.clear_screen()
        menu_item.Curr_Menu = name
        Settings.PrintMenu(name)

    def Home():
            
        Settings.ChangeMenu("MainMenu")

class SecondFunctions:
    def remove():
        
        Settings.clear_screen()
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
            Settings.ChangeMenu('MainMenu')
    
    def list():
    
        os.system("ls")
    
    def clear_check():

        Settings.clear_screen()
        print(colored(f"You are in: {menu_item.Curr_Menu}",'light_yellow'))
    
    def local():
        
        os.system("pwd")
        
    def move():
        
        path_input = input("Enter the full path of the file/folder that you would like to move:\n")
        dest_path_input = input("\nEnter the destination folder's full path:\n")
        os.system(f"mv {path_input} {dest_path_input}")
    
    def cd():
        
        cd_input = inquirer.list_input("Which direction would you like to move",choices = ['back','forward']) 
        if cd_input == "back":
                
            os.chdir("..")
            os.system("pwd")
        
        elif cd_input == "forward":
            questions = [
                inquirer.List('dir',
                message="Where",
                choices= sorted(os.listdir()),
            )]
            answers = inquirer.prompt(questions)
            os.chdir(answers['dir'])
            os.system("pwd")
    
    def edit():
        edit_choice = inquirer.list_input('What do you want to edit', choices = sorted(os.listdir()))
        os.system(f'nano {edit_choice}')
        
    def cat():
        
        questions = [
            inquirer.List('file',
            message = 'What do you want to read',
            choices = sorted(os.listdir())
            )]
        answers = inquirer.prompt(questions)
        a = answers['file']
        os.system(f'cat {a}')

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
                SecondFunctions.remove()
            elif user_input == "ls":
                SecondFunctions.list()
            elif user_input == "clear":
                SecondFunctions.clear_check()
            elif user_input == "pwd":
                SecondFunctions.local()
            elif user_input == "mv":
                SecondFunctions.move()
            elif user_input == "cd":
                SecondFunctions.cd()
            elif user_input == "edit":
                SecondFunctions.edit()
            elif user_input == "cat":
                SecondFunctions.cat()
            else:
                print("Command not found!")
