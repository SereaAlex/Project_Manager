#!/usr/bin/env python3


import os
import time
import readline
import glob

def completer(text, state):
    return (glob.glob(text + '*') + [None])[state]

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

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
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░  -v.0.5

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

#The program starts here

while program_on:
    
    user_input = input("\nType:")
    
#not enviroument commands
    
    if user_input == "home":
        
        clear_screen()
        slow_print(home(),0.0001)
    
    
    if user_input == "clear":
        
        clear_screen()
        
    if user_input == "ls":
        
        os.system("ls")
        
    if user_input == "pwd":
        
        os.system("pwd")
        
    if user_input == "cd ..":
        
         os.chdir("..")
        
    if user_input == "cd":
        
        try:
            
            cd_input = input("\nWhere?: ")
            os.chdir(cd_input)
    
        except:
            
            print("Please enter the correct path name.")
    
    if user_input == "rm":
        
        rm_input = input("Do you want to remove a file or a directory?: ")
        
        if rm_input == "file":
            
            rm_file_input = input("Name: ")
            os.system(f"rm {rm_file_input}")
            print(f"The file named {rm_file_input} was removed.")
        
        if rm_input == "directory" or rm_input == "dir":
            
            rm_directory_input = input("Name: ")
            os.system(f"sudo rm -r {rm_directory_input}")
            print(f"The directory named {rm_directory_input} was removed.")
            
    if user_input == "cat":
        
        cat_input = input("Name: ")
        os.system(f"cat {cat_input}")
        
    if user_input == "edit":
        
        edit_input = input("Name: ")
        os.system(f"nano {edit_input}")

#home commands

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
    

    if user_input == "3":
        
        os.system("curl parrot.live")
        
        print("Not funny after a while ha? :))")
        
        
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


[4.1] Type "clear" whenever your screen feels too crowded
[4.2] Type "home" to go back to the original screen
[4.3] Type "create" to create a file or a direcotry
[4.4] Type "code" in the create section to code stuff!
[4.5] Type "rm" to remove a directory or a file
[4.6] Type "pwd" to check the location that you are
[4.7] Type "ls" to check the contents of the directory that you are
[4.8] Type "cat" to read the contents of the file/s that you have
[4.9] Type "testing" for easy acces to test your programs (for now, only python) 
[4.10]Type "cd" to change directories forward only
[4.11]Type "cd .." to change directories backwards
[4.12]Type "edit" to change or rewrite files that you want directly in the toolkit
P.S: You can use " CTRL-C" for any operation to close
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
    
