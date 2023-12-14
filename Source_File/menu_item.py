from doctest import OPTIONFLAGS_BY_NAME
import os

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

class SomeOtherFuncs:
    def Func5():
    
        rm_input = input("Do you want to remove a file or a directory?: ")
        
        if rm_input == "file":
            
            rm_file_input = input("Name: ")
            os.system(f"rm {rm_file_input}")
            print(f"The file named {rm_file_input} was removed.")
        
        if rm_input == "directory" or rm_input == "dir":
            
            rm_directory_input = input("Name: ")
            os.system(f"sudo rm -r {rm_directory_input}")
            print(f"The directory named {rm_directory_input} was removed.")
    
    def Func6():
    
        os.system("ls")
    
    def Func7():
    
        clear_screen()
    
    def Func8():
        
        os.system("pwd")
        
    def Func9():
        
        path_input = input("Enter the full path of the file/folder that you would like to move:\n")
        dest_path_input = input("\nEnter the destination folder's full path:\n")
        os.system(f"mv {path_input} {dest_path_input}")
    
    def Func10():
        
        cd_input = input("Which direction would you like to move?(back/forw): ")
        
        if cd_input == "back":
            
            os.chdir("..")
            
        elif cd_input == "forw":
            
            dir_input = input("Where?: ")
            
            os.chdir(dir_input)
                    


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
        except ValueError:
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
            else:
                print("Command not found!")
                    

