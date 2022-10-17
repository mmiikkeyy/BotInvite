import requests, time, os
from colorama import init, Fore
init(autoreset=True)
print(Fore.LIGHTMAGENTA_EX + """
 ██▓     ██▓  █████▒▄▄▄█████▓ ██▓ █    ██  ███▄ ▄███▓
▓██▒    ▓██▒▓██   ▒ ▓  ██▒ ▓▒▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒
▒██░    ▒██▒▒████ ░ ▒ ▓██░ ▒░▒██▒▓██  ▒██░▓██    ▓██░
▒██░    ░██░░▓█▒  ░ ░ ▓██▓ ░ ░██░▓▓█  ░██░▒██    ▒██ 
░██████▒░██░░▒█░      ▒██▒ ░ ░██░▒▒█████▓ ▒██▒   ░██▒
░ ▒░▓  ░░▓   ▒ ░      ▒ ░░   ░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
░ ░ ▒  ░ ▒ ░ ░          ░     ▒ ░░░▒░ ░ ░ ░  ░      ░
  ░ ░    ▒ ░ ░ ░      ░       ▒ ░ ░░░ ░ ░ ░      ░   
    ░  ░ ░                    ░     ░            ░   
                                                     
""")
print(Fore.LIGHTMAGENTA_EX + """
                                          [1] Application URL
                                          [0] Exit
""")

choice = int(input('Choose number :'))

client_id = input("Client ID: ")
print("""
[1] bot 
[2] applications.commands
""")

scope = int(input("Scope: "))

if scope == 1 :
   print(Fore.MAGENTA + "\nApplication: ",f"https://discord.com/api/v9/oauth2/authorize?client_id={client_id}&scope=bot")

if scope == 2 :
   print(Fore.MAGENTA + "\nApplication: ",f"https://discord.com/api/v9/oauth2/authorize?client_id={client_id}&scope=applications.commands")


# Exit
if choice == 0 :
    print('Goodbye see you later <3')
    time.sleep(2)
    exit()



input("")