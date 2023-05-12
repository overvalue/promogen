import ctypes
import string
import os
import time
import requests
from colorama import Fore
ISSUE = "make an issue for support"

USE_WEBHOOK = True

print(ISSUE)

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
from subprocess import call
call('color b', shell=True)
os.system('color FF')
try:  
    from discord_webhook import DiscordWebhook
except ImportError:
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:
    import requests
except ImportError:
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()
try:
    import numpy
except ImportError:
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()


url = "https://github.com"
try:
    response = requests.get(url)
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
 
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()


class NitroGen: 
    def __init__(self):
        self.fileName = "Nitro Codes.txt"

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt":
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Promotion Codes Generator and Checker - Made by bleak#3325")
        else:  # Or if it is unix
            print(f'\33]0;Nitro Promotion Codes Generator and Checker - Made by bleak#3325\a',
                  end='', flush=True) 

        print("""
dont skid it keeds
                                                                                              
                                    """)
                                    
        time.sleep(1)  
        self.slowType(
            "\nInput How Many Codes to Generate and Check: ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("Specified input wasn't a number.\nPress enter to exit")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "If you want to use a Discord webhook, type it here or press enter to ignore: ", .02, newLine=False)
            url = input('')  
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()


        valid = []
        invalid = 0
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 24])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://promos.discord.gg/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break

            except Exception as e:
                print(f" Error | {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Promotion Codes Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by !!.#9763")
                print("")
            else:
                print(
                    f'\33]0;Nitro Promotion Codes Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by !!.#9763\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")

        input("\nThe end! Press Enter 5 times to close the program.")
        [input(i) for i in range(4, 0, -1)]

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro:str, notify=None):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        if response.status_code == 200:
            print(f" {Fore.GREEN}Valid {Fore.LIGHTGREEN_EX}> {Fore.GREEN}                  {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True

        else:
            print(f" {Fore.CYAN}[*] {Fore.BLUE}Invalid {Fore.LIGHTRED_EX}> {Fore.RED}                  [ {nitro} ] ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
