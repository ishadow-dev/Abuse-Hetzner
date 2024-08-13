#!/usr/bin/env python3
from subprocess import *
from requests import *


def loader(): # Function to display information about the server and menu
        print("+-------------------------------------------------------------------------------------+")
        print("|            _                           _    _        _                              |")
        print("|     /\    | |                         | |  | |      | |                             |")
        print("|    /  \   | |__   _   _  ___   ___    | |__| |  ___ | |_  ____ _ __    ___  _ __    |")
        print("|   / /\ \  | '_ \ | | | |/ __| / _ \   |  __  | / _ \| __||_  /| '_ \  / _ \| '__|   |")
        print("|  / ____ \ | |_) || |_| |\__ \|  __/   | |  | ||  __/| |_  / / | | | ||  __/| |      |")
        print("| /_/    \_\|_.__/  \__,_||___/ \___|   |_|  |_| \___| \__|/___||_| |_| \___||_|      |")
        print("| Telegram : @shadow_Y_T                                                              |")
        print("+-------------------------------------------------------------------------------------+")
        print(f"|Server Country: {server_country}                                                     ")
        print(f"|Server IP: {server_ip}                                                               ")
        print(f"|Server ISP: {server_isp}                                                             ")
        print("+-------------------------------------------------------------------------------------+")
        print("| 1 - Abuse Fixer                                                                     |")
        print("| 2 - Status                                                                          |")
        print("| 3 - Unistall                                                                        |")
        print("+-------------------------------------------------------------------------------------+")

def update(): # Function to update server
        run(["apt", "update"], check=True)

def ipv4_address(): #Function to find ip4 address
        result = run(["hostname", "-I"], capture_output=True, text=True)
        ip_address = result.stdout.split()[0]
        return ip_address

def country(ip): #Function to find country of the ip server
        url = f"http://ip-api.com/json/{ip}"
        response = get(url)
        data = response.json()
        if data["status"] == "success":
                return data["country"]
        else:
                return "Error : " + data["message"]

def isp(ip): #Function to find isp of the ip server
        url = f"http://ip-api.com/json/{ip}"
        response = get(url)
        data = response.json()
        if data["status"] == "success":
                return data["isp"]
        else:
                return "Error : " + data["message"]
# Server information 
server_ip = ipv4_address()
server_country = country(server_ip)
server_isp = isp(server_ip)

update()

# Loop to run the script
answer = "yes"
while answer == "yes":
        loader()
        choice = int(input("Please choose an option:"))

        if choice == 1:
                number_config = int(input("Number of config : "))
                for i in range(1, number_config + 1):
                        config_port = int(input(f"Enter Config port {i} ( example : 1890,1880,... ): "))
                ssh_port = int(input("Enter SSH port : "))

                config = f"ufw allow {config_port}"
                ssh = f"ufw allow {ssh_port}"

                run(config, shell=True, check=True, stdout=PIPE, stderr=PIPE)
                run(ssh, shell=True, check=True, stdout=PIPE, stderr=PIPE)
                run(["ufw", "enable"], check=True)

                print("The Abuse Was Fixed...")
        elif choice == 2:
                run(["ufw", "status"], check=True)
        elif  choice == 3:
                run(["ufw", "disable"], check=True)
                print("Abuse Fixer has disabled")
        else:
                print("Number is invalid!")
        answer = input("Do you want to continue... (yes/no)-(Default yes): ")
