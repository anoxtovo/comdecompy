#!/usr/bin/python3
#
#                 ###  ###  ##   ## ####   ###  ###  ##   ##    ####  ##  ##
#                ##   ## ## ### ### ##  # ##   ## ## ### ###    ##  #  ####
#                ##   ## ## ## # ## ##  # ##   ## ## ## # ##    ####    ##
#                 ###  ###  ##   ## ####   ###  ###  ##   ## ## ##      ##
#
# Hey, Everyone!, Someones looking at what is that shit!? Actualy  i'm thinking  about
# building a cool python script for convert both python source codes(*.py) to compiled 
# python code  files(*.pyc), and also convert  the any  compiled  python files to back 
# python  source  file format(*.py). comdecompy is a  interactive  python compiler and 
# decompiler  script, comdecom  also included  python source code encoder to some base
# encoding methods.
#
# Author: Thumula basura Suraweera
# Copyright (c) 2020 Thumula Basura Suraweera(An0xt0v0)
# web: https://anoxtovo.wordpress.com/comdecom-py
# git: https://githubcom/an0xt0v0/comdecompy

# importing modules
import sys
import os
import platform
import subprocess
from colorama import *
import shutil
import uncompyle6

# define some ansii escape colors

# Forground colors
init()

colorRed = Fore.RED
colorBlue = Fore.BLUE
colorGreen = Fore.GREEN
colorBlack = Fore.BLACK
colorYello = Fore.YELLOW

#background colors
colorWhiteBG = Back.WHITE
colorBlackBG = Back.BLACK
colorRedBG = Back.RED
colorGreenBG = Back.GREEN
colorBlackBG = Back.LIGHTWHITE_EX
colorReset = Fore.RESET + Back.RESET

#function for check platform and clear screen
def clearScreen():
    sys = platform.system()
    if sys == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#banner
def banner():
    print(f"""{colorGreen}\x09\x09╔═══════════════════════════════════════════════════════════════╗
\x09\x09║                                                               ║
\x09\x09║   ███  ███  ██   ██ ████   ███  ███  ██   ██    ████  ██  ██  ║
\x09\x09║  ██   ██ ██ ███ ███ ██  █ ██   ██ ██ ███ ███    ██  █  ████   ║
\x09\x09║  ██   ██ ██ ██ █ ██ ██  █ ██   ██ ██ ██ █ ██    ████    ██    ║
\x09\x09║   ███  ███  ██   ██ ████   ███  ███  ██   ██  █ ██      ██    ║
\x09\x09║                                                 version_0.2   ║
\x09\x09╚═══════════════════════════════════════════════════════════════╝{colorReset}
\x09\x09           {colorGreenBG}[  A     N     0     X     T     V    0  ]{colorReset}           
\x09{colorRed}[+]          Interactive Python Script Compiler & Decompiler Script          [+]{colorReset}
\x09{colorRed}[+]                  https://github.com/an0xt0v0/comdecompy                  [+]{colorReset}""")

# defining & call to the  compiler functions.
def compiler():
    # importing py_compile
    import py_compile

    while (KeyboardInterrupt,SystemExit()):
        print(colorBlue+"**Input Source Name With Full Path,"+ colorReset + colorRED +"\n use 'exit' or 'back' commands to exit compiler"+colorReset)
        userinput = input("compiler> ")

        if (os.path.isfile(userinput)):
            print("[+] Reading Source...          "+colorGreen+"[DONE]"+colorReset+"\n[-] Source: ",userinput)
            askPathYN = input("Whould You Want Store Binary File After Compilation in Specific Folder(Y/N)?")
            
            if (askPathYN == "Y" or askPathYN == 'y'):
                print(colorBlue + "\n** Enter The Full Path of Specific Directory\n** If The Directory Don't Exist Comdecom Automaticaly Genarete The Specific Directory !\n"+colorReset)
                askPathName = input(">> ")

                try:
                    if(os.path.isdir(askPathName)):
                        print(colorGreen+"[+] Directory Alredy Exists!"+colorReset)
                    
                    else:
                        os.mkdir(askPathName)
                        print("[+] Genarating Directory...\n[+] Directory: ", askPathName + "\n---------- [ DONE! ] ----------")

                    py_compile.compile(userinput);
                    print(colorGreenBG + "[+] Compilation Completed...\n" + colorReset + colorGreenBG+"[+] Moving Results to ", askPathName + colorReset)
                    shutil.move("__pycache__", askPathName)
                    print(colorGreenBG + "[+] Results Moved to \n", askPathName + colorReset)

                except:
                    print(colorRed+"[!] Compiler Error!"+colorReset)
            elif (askPathYN == "N" or askPathYN== "n"):
                try:
                    py_compile.compile(userinput)
                    print(colorGreenBG + "[+] Compilation Completed...\n" + colorReset + colorBlue+"** Check out the __pycache__ directory\n"+ colorReset)
                except:
                    print(colorRed+"[!] Compiler Error!"+colorReset)
            else:
                print("[!] Something Went Wrong Here...\n[+] Back to Start...")

        elif(userinput == "exit" or userinput == "back"):
            print(colorRedBG+colorBlack+"[*] Exitting compiler..."+colorReset)
            return(main)

# area-decompiler
def decompile():
    while(KeyboardInterrupt, SystemExit()):
        print(colorBlue+"** Input Compiled python file Name With Full Path\n** comdecom only supports for *.pyc format,"+ colorReset + colorRed + "\n** use 'exit' or 'back' commands to exit compiler"+colorReset)
        userinput = input("decompiler> ")
        output = input("output> ")

        if(os.path.isfile(userinput)):
            print("[+] Reading Compiled File...          "+colorGreen+"[DONE]"+colorReset+"\n[-] File: ",userinput)
            try:
                os.system("uncompyle6 " + userinput + " -o " + output)
                #uncompyle6.disas.disassemble_file(userinput, outstream=None, native=False)
                print(colorGreenBG + "[+] Compilation Completed...\n" + colorReset)
            
            except:
                print(colorRedBG + "[!] Decompilation error")

        elif(userinput == "exit" or userinput == "back"):
            print(colorRedBG+colorBlack+"[*] Exitting decompiler..."+colorReset)
            return(main)

# area-encoder
def encoder():
    # importing requirement

    while(KeyboardInterrupt, SystemExit()):
        print(colorRed+"** Under the Construnction...        :(\nuse 'back' or 'exit' commands to exit encorder..."+colorReset)
        userinput = input("encoder> ")

        if(userinput == "exit" or userinput == "back"):
            print(colorRedBG+colorBlack+"[*] Exitiing Encoder..."+colorReset)
            return(main)

def main():
    clearScreen()
    banner()

    # Interactive shell
    while  (KeyboardInterrupt,SystemExit()):
        usrinput = input(">> ")

        if (usrinput == "exit"):
            clearScreen();print("Bye, Bye!")
            exit()
        
        elif (usrinput == "help" or usrinput == "?"):
            print(colorGreen+"""
Usage/Help:
=======================================================
 Command               Usage/Info
---------             ---------------------------------
 help / ?              Usage/Help Message(This Message)
 compile               Start py to pyc compiler
 decompile             Start pyc to py decompiler
 encode                Start encoded script genarator
 refresh               Refresh Screen/ Back to Start
 back                  Back
 exit                  Exit COMDECOM
=======================================================
"""+colorReset)
        elif (usrinput == "compile"):
            compiler()
        
        elif (usrinput == "decompile"):
            decompile()
        
        elif (usrinput == "encode"):
            encoder()

        elif (usrinput == "refresh"):
            clearScreen(); banner()
            
        else:
            print("[!] Unknown Command.")

if __name__ == "__main__":
    main()
