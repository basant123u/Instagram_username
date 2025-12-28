"""This tool is coded by Basant(alphax) you are free to use or copy the code, but please ensure the proper credit is given to the orginal author.
Remember taking other's credit doesn't make you a good programmer, hahaha!

SHORT DETAILS ABOUT AUTHOR (BASANT):

NAME : BASANT KUMAR MAHATO
CLASS : 11TH
STUDY : COMPLETED CLASS 10TH NOW STUDYING IN CLASS 11TH
FROM : JHARKHAND (INDIA)
DREAM : IIT < HAPPY LIFE :)

INSTAGRAM : B4SAN1 (IT MAY CHANGE)
TELEGRAM : X00III
"""

import os
import random
import time

try:
     import requests
     from bs4 import BeautifulSoup
     from colorama import Fore
     from playwright.sync_api import sync_playwright
except:
     print("Modules not fount, try executing bash setup.sh")

    
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE   
MAGENTA = Fore.MAGENTA

def clear():
     if os.name == 'nt':
       os.system('clear')
     else:
       os.system('cls')

     

print(f"""{RED}
---------------------------------     
{MAGENTA}| ᴀᴜᴛʜᴏʀ : ʙᴀꜱᴀɴᴛ                |
| ᴛᴇʟᴇɢʀᴀᴍ : @X00III             |
| ᴍᴀɪʟ : ᴍᴀɪʙᴀꜱᴀɴᴛʜᴏᴏɴ@ɢᴍᴀɪʟ.ᴄᴏᴍ |
{RED}---------------------------------     
""")
enter = input(f"{GREEN}Press any key to continue...")
if enter == "":
     clear()
else:
     exit()

a1 = ['w','e','r','u','o','a','s','z','x','c','v','n','m']

a2 = ['1','2','3','4','5','6','7','8','9','0','_','.','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

usr_len = int(input(f"{BLUE}Enter the username length : "))
print(f"{RED}[0] {MAGENTA}AESTHETIC USERNAME (lower)\n{RED}[1] {MAGENTA}ANY USERNAME (best for 4l & 5l)")
n = input()
if n == "0":
     alphabets = a1
     clear()
elif n == "1":
     alphabets = a2
     clear()
else:
     alphabets = a2
     print("using default username type(any username)")

# ascii art
print(f"""
██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝
██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  
██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                     {YELLOW} V 0.0.1                                
""")


def check_():
    with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.instagram.com/accounts/emailsignup/")
            time.sleep(1)
            try:
                page.fill("._aa4a", "fckr@gmail.com")
                page.locator("._aa4a").nth(1).fill("hello@bacchon123.")   
                page.locator("._aa4a").nth(2).fill("alphaxhere")
                page.locator("._aa4a").nth(3).fill(f"{result}")
                page.get_by_role("button", name="Sign Up").click()
                try:
                    page.get_by_role("button", name="Go back").click()
                    print(f"{YELLOW}Congrutulations you can use : {result}")
                except:
                    print(f"{CYAN}failed")
            except:
                 check_()
                
while True:
    rand = random.choices(alphabets, k=usr_len)
    result = ''.join(rand)
    url = f"https://www.instagram.com/{result}/"
    check = requests.get(url)
    check_str = str(check.text)
    soup = BeautifulSoup(check_str, "html.parser")
    soup_str = str(soup.title)
    if soup_str == "<title>Instagram</title>":
        print(f"{GREEN}{result}")
        check_()
    
    else:
        print(f"{RED}{result}")

if __name__ == "__main__":
    main()


