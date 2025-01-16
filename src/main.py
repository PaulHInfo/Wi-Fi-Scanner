from src.tools.wifi import *
print("""\
+--------------------------------------------------------------------+
|  __        ___       _____ _   _____           _ ____              |
|  \ \      / (_)     |  ___(_) |_   _|__   ___ | | __ )  _____  __  |
|   \ \ /\ / /| |_____| |_  | |   | |/ _ \ / _ \| |  _ \ / _ \ \/ /  |
|    \ V  V / | |_____|  _| | |   | | (_) | (_) | | |_) | (_) >  <   |
|     \_/\_/  |_|     |_|   |_|   |_|\___/ \___/|_|____/ \___/_/\_\  |
+--------------------------------------------------------------------+
 """)
print("Tools list -> Commande")
print("1 - Scann -> scann")
print("2 - discover -> disc")


def check_input(a):
    if(a == "scann"):

        scan()
    elif(a == "disc"):

        discover_wifi()
    else:
        print("please retry")
        pass

a = input("commande : ")
check_input(a)