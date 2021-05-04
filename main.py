import requests
from colorama import Fore, init
from os import system
import os
import time
import random

system("title " + "Soundcloud Checker - Dems")

os.system("start \"\" https://discord.gg/U4g4bw6zNm")
titleprog = """

  ██████  ▒█████   █    ██  ███▄    █ ▓█████▄  ▄████▄   ██▓     ▒█████   █    ██ ▓█████▄ 
▒██    ▒ ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌▒██▀ ▀█  ▓██▒    ▒██▒  ██▒ ██  ▓██▒▒██▀ ██▌
░ ▓██▄   ▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒░██   █▌▒▓█    ▄ ▒██░    ▒██░  ██▒▓██  ▒██░░██   █▌
  ▒   ██▒▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓▓▄ ▄██▒▒██░    ▒██   ██░▓▓█  ░██░░▓█▄   ▌
▒██████▒▒░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░▒████▓ ▒ ▓███▀ ░░██████▒░ ████▓▒░▒▒█████▓ ░▒████▓ 
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒  ▒▒▓  ▒ 
░ ░▒  ░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒   ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░ ░░▒░ ░ ░  ░ ▒  ▒ 
░  ░  ░  ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░  ░ ░  ░ ░          ░ ░   ░ ░ ░ ▒   ░░░ ░ ░  ░ ░  ░ 
      ░      ░ ░     ░              ░    ░    ░ ░          ░  ░    ░ ░     ░        ░    
                                       ░      ░                                   ░      

"""
print(Fore.MAGENTA + titleprog)
print(Fore.WHITE + "                                  Username Checker by Dems\n")

good = 0
bad = 0

print(Fore.GREEN + "Press 1 to start checking:")
print(Fore.LIGHTYELLOW_EX + "[1] SoundCloud")

ask = int(input(Fore.RESET + "\n> "))
while ask < 1:
    print(Fore.LIGHTRED_EX + "Incorrect value\n")

    print(Fore.GREEN + "Press 1 to start checking:")
    print(Fore.LIGHTYELLOW_EX + "[1] SoundCloud")
    ask = int(input(Fore.RESET + "\n> "))

if ask == 1:
    combo1 = open("wordlist.txt", "r")
    while 1:
        readl1 = combo1.readline().split("\n")[0]
        if readl1 == "":
            break
        sess = requests.Session()
        url = f"https://soundcloud.com/{readl1}"

        HEADERS = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }

        req = sess.get(url, headers=HEADERS)
        if req.status_code == 200:
            bad = bad + 1
            print(Fore.YELLOW + url)
            print(Fore.LIGHTRED_EX + "[-] " + Fore.LIGHTYELLOW_EX + " Username not available" + "\n")

        elif req.status_code == 404:
            good = good + 1
            print(Fore.YELLOW + url)
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + " Username available" + "\n")
            with open("SoundCloud Results.txt", "a") as results:
                results.write(f"https://soundcloud.com/{readl1}" + "\n")


print("Results have been saved - " + Fore.LIGHTGREEN_EX + str(
    good) + Fore.RESET + " hits" + " and " + Fore.LIGHTRED_EX + str(bad) + Fore.RESET + " bad !")
time.sleep(7)