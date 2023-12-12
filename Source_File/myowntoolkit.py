#!/usr/bin/env python3


import os
import time


def slow_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def home():

    return """
      
████████╗░█████╗░░█████╗░██╗░░░░░██╗░░██╗██╗████████╗  
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░██╔╝██║╚══██╔══╝  
░░░██║░░░██║░░██║██║░░██║██║░░░░░█████═╝░██║░░░██║░░░  
░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔═██╗░██║░░░██║░░░  
░░░██║░░░╚█████╔╝╚█████╔╝███████╗██║░╚██╗██║░░░██║░░░  
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░  -v.0.3

███████╗███╗░░██╗░░░░░██╗░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝████╗░██║░░░░░██║██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗
█████╗░░██╔██╗██║░░░░░██║██║░░██║░╚████╔╝░█████╗░░██████╔╝
██╔══╝░░██║╚████║██╗░░██║██║░░██║░░╚██╔╝░░██╔══╝░░██╔══██╗
███████╗██║░╚███║╚█████╔╝╚█████╔╝░░░██║░░░███████╗██║░░██║
╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝



[1] Testing programs
[2] Create and code
[3] Funny parrot
[4] Help
[5] Exit





"""
clear_screen()
slow_print(home(),0.0001)

program_on = 1




while program_on:
    
    user_input = input("\nType:")
    
    
    if user_input == "1" or user_input == "testing":
    
        files = os.listdir()
        
        py_files = [file for file in files if file.endswith('.py')]
        
        if len(py_files) == 1:
            
            print("No .py files found. Please add some .py files to test and try again.")
        
        else:
            print("""What would you like to test?:""")
            test_input = input("\nTest: ")
            os.system(f"python3 {test_input}")
            print("Test completed! (now back to the toolkit)")

    
    if user_input == "2" or user_input == "code" or user_input == "create":
        
        clear_screen()
        print("Here you can create a file, edit a file or code!")
        create_input = input("\nWhat do you choose?: ")
        
        if create_input == "file" or create_input == "directory":
            
            clear_screen()
            choosing = input("\nFile or directory?: ")
            
            if choosing == "file":
                
                clear_screen()
                name_file = input("\nWhat is the name of the file?: ")
                os.system(f"touch {name_file}")
                print(f"\nYour file named {name_file} was created!")
                
            elif choosing == "directory":
                
                clear_screen()
                name_directory = input("What is the name of the directory?: ")
                os.system(f"mkdir {name_directory}")
                print(f"\nYour directory named {name_directory} was created!")
        
        if create_input == "code": 
            
            clear_screen()
            code_input = input("What would you like to code?: ")
            os.system(f"code {code_input}")
    
    if user_input == "home" or user_input == "4.b":
        
        clear_screen()
        slow_print(home(),0.0001)
    
    
    if user_input == "clear" or user_input == "4.a":
        
        clear_screen()
        
    if user_input == "ls":
        
        os.system("ls")
        
    if user_input == "pwd":
        
        os.system("pwd")
        
    if user_input == "cd back":
        
         os.system("cd ..")
        
    if user_input == "cd forward":
        
         cd_input = input("\nWhere?: ")
         os.system(f"cd {cd_input}")
    
    if user_input == "rm":
        
        rm_input = input("Do you want to remove a file or a directory?: ")
        
        if rm_input == "file":
            
            rm_file_input = input("Name: ")
            os.system(f"rm {rm_file_input}")
            print(f"The file named {rm_file_input} was removed.")
        
        if rm_input == "directory":
            
            rm_directory_input = input("Name: ")
            os.system(f"sudo rm -r {rm_directory_input}")
            print(f"The directory named {rm_directory_input} was removed.")
            
    if user_input == "cat":
        
        cat_input = input("Name: ")
        os.system(f"cat {cat_input}")
        
    if user_input == "edit":
        
        edit_input = input("Name: ")
        os.system(f"nano {edit_input}")
        
    if user_input == "3":
        
        os.system("curl parrot.live")
        
        
    if user_input == "4" or user_input == "help":
        
        clear_screen()
        slow_print("""

██╗░░██╗███████╗██╗░░░░░██████╗░
██║░░██║██╔════╝██║░░░░░██╔══██╗
███████║█████╗░░██║░░░░░██████╔╝
██╔══██║██╔══╝░░██║░░░░░██╔═══╝░
██║░░██║███████╗███████╗██║░░░░░
╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░░░░

░██████╗███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔════╝██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
╚█████╗░█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
░╚═══██╗██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
██████╔╝███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
╚═════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝


[4.a] Type "clear" whenever your screen feels too crowded
[4.b] Type "home" to go back to the original screen
[4.c] Type "create" to create a file or a direcotry
[4.d] Type "code" in the create section to code stuff!
[4.e] Type "rm" to remove a directory or a file
[4.f] Type "pwd" to check the location that you are
[4.g] Type "ls" to check the contents of the directory that you are
[4.h] Type "cat" to read the contents of the file/s that you have
[4.i] Type "testing" for easy acces to test your programs (for now, only python)

(If you wonder why there is no "cd", \n it's because it doesn't work for now -.-")
              """,0.0001)
        
        
    if user_input == "5" or user_input == "exit":
        
        slow_print("""
                   
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝""",0.0001)
        program_on = 0
        clear_screen()    
    
