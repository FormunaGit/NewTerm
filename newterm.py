class NerdFontsIcons:
    class OS:
        freebsd = ""
        linuxMint = ""
        archLinux = "󰣇"
        tux = ""
        windows11 = ""
    class Misc:
        questionMark = ""
        semiCircleLeft = "󱎕"
        semiCircleRight = ""

import os # For the [real] command
import getpass # To get the user's nickname
import socket # To get the machine hostname
import platform


# Variables
useNF = False # Change this variable if you are using a NerdFonts-pathced font.
username = getpass.getuser()
macname = socket.gethostname()

try: # Check if colorama is imported, and try to install it (with user choice, ofcourse)
    from colorama import Fore, Back, Style # The only non-builtin dependency
except ImportError:
    print("ERROR: Colorama is REQUIRED to run NewTerm for colors.")
    print("Install Colorama with PIP?")
    ans = input("[Y/n] ").lower()
    if ans == "" or ans == "y":
        print("Running \"pip install colorama\"...")
        os.system("pip install colorama")
    elif ans == "n":
        print("NewTerm requires Colorama, so NT is closing.")
    else:
        print("Invalid option, taking as [no].")

try: # Check if distro is imported
    import distro
except ImportError:
    print(Fore.YELLOW + "Module [distro] is not found")


def OSIcon():
    # Detect OS
    if platform.system() == "Linux":
        if distro.id() == "linuxmint":
            return NerdFontsIcons.OS.linuxMint
        elif distro.id() == "arch":
            return NerdFontsIcons.OS.archLinux
        elif distro.id() == "freebsd":
            return NerdFontsIcons.OS.freebsd
    elif platform.system() == "Windows":
        return NerdFontsIcons.OS.windows11


def PromptBuilder(): # Build a cool NerdFonts prompt if NF is enabled.
    if useNF == True:
        prompt = f"{Fore.WHITE + NerdFontsIcons.Misc.semiCircleLeft + Back.WHITE + Fore.BLACK + OSIcon() } { distro.name() + Fore.WHITE + Back.BLACK + NerdFontsIcons.Misc.semiCircleRight + Fore.CYAN + username + Fore.BLUE}@{Fore.GREEN + macname + Fore.WHITE + Back.BLACK + Style.RESET_ALL + Fore.BLACK + NerdFontsIcons.Misc.semiCircleRight + Style.RESET_ALL}"
        return prompt
    elif useNF == False:
        return f"{Fore.RED + username + Fore.CYAN}@{Fore.GREEN + macname + Style.RESET_ALL} ~> "


def main(exit=False):
    while exit != True:
        cmd = input(PromptBuilder())

        if cmd == "help":
            print("NEWTERM - Python-made Shell\nVersion 1.0")
        elif cmd == "exit":
            print("Exiting...")
            exit = True
        # Here ends the NT built-in commands.
        elif cmd.startswith("real "): # All commands after the [real ] segment gets ran with whatever you used to run NT, so if you run ZSH, [real] will use ZSH.
            os.system(cmd[5:])

if __name__ == '__main__':
    main()