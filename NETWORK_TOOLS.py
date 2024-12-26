import os
import sys
import time
import socket
from colorama import Fore

# Commands
commands = [
    'ipconfig',
    'ipconfig /all',
    'systeminfo',
    'whoami',
    'ping',
    'tracert',
    'nslookup',
    'netstat -an'
]

# ipconfig - Basic network info.
def ipconfig():
    os.system('ipconfig')

# ipconfig /all - Detailed network info
def ipconfig_all():
    os.system('ipconfig /all')

# systeminfo - OS and hardware details.
def system_info():
    os.system('systeminfo')

# whoami - Computer's name
def whoami():
    os.system('whoami')

# ping - Test server connection.
def ping():
    try:
        ping_question = input('Please enter ip or domain to ping>> ')
        print(f'getting info about {ping_question}..')
        time.sleep(1)
        os.system(f'ping {ping_question}')
    except Exception as e:
        print(f'An error occurred: {e}')

# tracert - Trace server route.
def tracert():
    try:
        tracert_question = input("enter domain: ")
        os.system(f'tracert {tracert_question}')
    except Exception as e:
        print(f'An error occurred {e} ')

# nslookup - DNS info for a domain.
def nslookup():
    try:
        nslookup_question = input('enter domain: ')
        os.system(f'nslookup {nslookup_question}')
    except socket.gaierror:
        print('An error occurred, please try with different domain!')

# netstat -an - Active connections.
def netstat():
    os.system('netstat -an')
# Descriptions for each command
def info():
    print(Fore.LIGHTBLUE_EX  + "   ipconfig " + Fore.LIGHTWHITE_EX  + "Basic network info.\n" + Fore.LIGHTBLUE_EX  +"   ipconfig /all " + Fore.LIGHTWHITE_EX  + "Detailed network info.\n"+ Fore.LIGHTBLUE_EX  + "   systeminfo " + Fore.LIGHTWHITE_EX  + "OS and hardware details.\n" + Fore.LIGHTBLUE_EX  + "   whoami " + Fore.LIGHTWHITE_EX  + "Computer's name.\n" + Fore.LIGHTBLUE_EX  + "   ping " + Fore.LIGHTWHITE_EX  + "Test server connection.\n"+ Fore.LIGHTBLUE_EX + "   tracert " + Fore.LIGHTWHITE_EX  + "Trace server route.\n" + Fore.LIGHTBLUE_EX  + "   nslookup " + Fore.LIGHTWHITE_EX  + "DNS info for a domain.\n" + Fore.LIGHTBLUE_EX  + "   netstat -an " + Fore.LIGHTWHITE_EX  + "Active connections.")
    print(Fore.LIGHTWHITE_EX + "   --------------------------------")

def question():
    input(Fore.LIGHTBLUE_EX + "press any key to continue...")
    os.system('cls')
    main()
os.system('cls')
def main():
    # Banner
    print(Fore.LIGHTBLUE_EX + """
    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗        ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    """)
    print("                                                 -------------------")
    print("                                                   @ Made By $HIFU\n"
          "                                                   Version: 2.0")
    print("                                                 -------------------")

    while True:
        info()
        user_input = input(Fore.LIGHTWHITE_EX + "   Enter a " + Fore.LIGHTWHITE_EX + "command: (ex.ipconfig) ")
        if user_input.lower() in commands:
            if user_input.lower() == 'ipconfig':
                ipconfig()
                question()
            elif user_input.lower() == 'ipconfig /all':
                ipconfig_all()
                question()

            elif user_input.lower() == 'systeminfo':
                system_info()
                question()

            elif user_input.lower() == 'whoami':
                whoami()
                question()

            elif user_input.lower() == 'ping':
                ping()
                question()

            elif user_input.lower() == 'tracert':
                tracert()
                question()

            elif user_input.lower() == 'nslookup':
                nslookup()
                question()

            elif user_input.lower() == 'netstat -an':
                netstat()
                question()

        else:
            print(Fore.LIGHTRED_EX + "Can't recognize command, please try again!")

if __name__ == '__main__':
    main()