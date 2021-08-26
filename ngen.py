
import os
import time
from os import system, name
from time import sleep
import requests
import random
import string

print("""
╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐  ┌┬┐┌─┐  ┌┐┌┬┌┬┐┬─┐┌─┐
║ ╦├┤ │││├┤ ├┬┘├─┤ │││ │├┬┘   ││├┤   ││││ │ ├┬┘│ │
╚═╝└─┘┘└┘└─┘┴└─┴ ┴─┴┘└─┘┴└─  ─┴┘└─┘  ┘└┘┴ ┴ ┴└─└─┘
""")
time.sleep(2)
print("Recuerda que los codigos son a la suerte.")
time.sleep(0.3)
print("Disfruta!")
time.sleep(0.2)

num=input('Cuantos codigos quieres probar?: ')

f=open("Nitro Codes.txt","w", encoding='utf-8')

print("Empezando!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()




with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valido | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalido | {} ".format(line.strip("\n")))
input("!!!")
