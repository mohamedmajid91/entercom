import time

PORTCOM = '/dev/ttyUSB0'
TX = "Raspberry Pi 3B+"
RX = "Arduino Nano"
COMSYS = "2.4Ghz"
IDLE = "IDLE"
BUSY = "BUSY"

def new_start():
	print("\n\n\n\n\n\n\n\n\n\n\n")

def clear_solve():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def connection_succes():
	print(" _____                     _   _         ")
	print("|     |___ ___ ___ ___ ___| |_|_|___ ___ ")
	print("|   --| . |   |   | -_|  _|  _| | . |   |")
	print("|_____|___|_|_|_|_|___|___|_| |_|___|_|_|")
	print("                                         ")
	print("                                         ")
	print(" _____                                   ")
	print("|   __|_ _ ___ ___ ___ ___ ___           ")
	print("|__   | | |  _|  _| -_|_ -|_ -|          ")
	print("|_____|___|___|___|___|___|___|          ")

def interface_com_rpIDLE():
    print("                _   ____        _____ ____  __  __ ")
    print("               | | |___ \      / ____/ __ \|  \/  |")
    print("      ___ _ __ | |_  __) |_ __| |   | |  | | \  / |")
    print("     / _ \ '_ \| __||__ <| '__| |   | |  | | |\/| |")
    print("    |  __/ | | | |_ ___) | |  | |___| |__| | |  | |")
    print("     \___|_| |_|\__|____/|_|   \_____\____/|_|  |_|\n")                                                
    print("      ___  ____  ____     __     __  _             ")
    print("     / _ \/ __/ / __/__  / /_ __/ /_(_)__  ___  ___")
    print("    / , _/ _/  _\ \/ _ \/ / // / __/ / _ \/ _ \(_-<")
    print("   /_/|_/_/   /___/\___/_/\_,_/\__/_/\___/_//_/___/\n\n")
    print("              Created by ent3rpr1se")
    #time.sleep(1)                                               
    print("----------------------------------")
    print("Board Recognition System")
    print("")                     
    print("TX :",TX)
    print("RX :",RX)
    print("Serial Port :",COMSYS)
    print("COM Route :",PORTCOM)
    print("TX Status :",IDLE)
    print("RX Status :",BUSY)
    print("----------------------------------")

def interface_com_arduIDLE():
    print("                _   ____        _____ ____  __  __ ")
    print("               | | |___ \      / ____/ __ \|  \/  |")
    print("      ___ _ __ | |_  __) |_ __| |   | |  | | \  / |")
    print("     / _ \ '_ \| __||__ <| '__| |   | |  | | |\/| |")
    print("    |  __/ | | | |_ ___) | |  | |___| |__| | |  | |")
    print("     \___|_| |_|\__|____/|_|   \_____\____/|_|  |_|\n")                                                
    print("      ___  ____  ____     __     __  _             ")
    print("     / _ \/ __/ / __/__  / /_ __/ /_(_)__  ___  ___")
    print("    / , _/ _/  _\ \/ _ \/ / // / __/ / _ \/ _ \(_-<")
    print("   /_/|_/_/   /___/\___/_/\_,_/\__/_/\___/_//_/___/\n\n")
    print("              Created by ent3rpr1se")
    #time.sleep(1)                                               
    print("----------------------------------")
    print("Board Recognition System")
    print("")                     
    print("TX :",TX)
    print("RX :",RX)
    print("Serial Port :",COMSYS)
    print("COM Route :",PORTCOM)
    print("TX Status :",IDLE)
    print("RX Status :",IDLE)
    print("----------------------------------")