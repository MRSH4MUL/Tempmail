#Developer : @MD SHIMUL

import requests
import os
print ("jone my TG 🔗🥵")
os.system("xdg-open https://t.me/DARKCYBER420")
logo = """##    ##  ######   ########    \n ##   ##  ##    ##  ##           \n ##  ##   ##        ##           \n #####    ##   #### ######      \n ##  ##   ##    ##  ##          \n ##   ##  ##    ##  ##          \n  ##    ##  ######   ##\n
\033[38;5;46mDeveloper> MR SHIMUL
\033[30;1m TG : https://t.me/DARKCYBER420
\033[35;1m GITHUB : MRSH4MUL
\033[34;1m TOOL : TEMP-MAIL """
print (logo)
class TempMail:
    def __init__(self):
        url = "https://www.1secmail.com/api/v1/"
        params = {
            'action': "genRandomMailbox",
            'count': "1"
        }
        headers = {
            'User-Agent': "okhttp/3.9.1",
            'Accept-Encoding': "gzip"
        }
        req = requests.get(url, params=params, headers=headers).text
        self.email = req.split('["')[1].split('"]')[0]
        print(f"Generated Email: {self.email}")

    def refresh_messages(self):
        name = self.email.split('@')[0]
        dom = self.email.split('@')[1]

        url = "https://www.1secmail.com/api/v1/"
        params = {
            'action': "getMessages",
            'login': name,
            'domain': dom,
        }
        headers = {
            'User-Agent': "okhttp/3.9.1",
            'Accept-Encoding': "gzip"
        }
        response = requests.post(url, params=params, headers=headers)
        print(response.text)

    def start(self):
        try:
            while True:
                input("\033[35;1mPress Enter to refresh the messages or Ctrl+C/Ctrl+X to exit...")
                self.refresh_messages()
        except KeyboardInterrupt:
            print("\nExiting...")


TempMail().start()