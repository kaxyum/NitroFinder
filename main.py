import os
import random
import string

try:
    import requests
except:
    os.system("pip install requests")
    os.system("pip install charset_normalizer.md__mypyc")
    os.system("pip install chardet")
    import requests
try:
    from art import *
except:
    os.system("pip install art")
    from art import *
try:
    from colorama import Fore, Style, Back, init
except:
    os.system("pip install colorama")
    from colorama import Fore, Style, Back, init
try:
    import time
except:
    os.system("pip install time")
    import time

WEBHOOK_URL = ""

tprint("NitroFinder")

def check_nitroboost_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}"

    try:
        response = requests.get(url)
        content = response.text

        if '{"message": "Unknown Gift Code", "code": 10038}' in content:
            print("Nitro Boost Code inactive:", code)
            return False
        elif 'too many 4xx response codes, try again later' in content:
            return None
        else:
            print("Nitro Boost Code active found:", code)
            return True

    except requests.exceptions.RequestException as e:
        print("Error during the request:", str(e))
        return False

def send_discord_webhook(code):
    data = {
        "content": f"Nitro Boost Code active found: \n https://discord.gift/{code}"
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("The webhook has been sent.")

starting_letters = input("Enter the first letters of the Nitro Boost Code: ")

letters_to_generate = 16 - len(starting_letters)

found = False
while not found:
    ending_letters = ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(letters_to_generate))

    nitroboost_code = starting_letters + ending_letters

    while True:
        result = check_nitroboost_code(nitroboost_code)
        if result is None:
            time.sleep(2)
        elif result:
            found = True
            send_discord_webhook(nitroboost_code)
            break
        else:
            break
