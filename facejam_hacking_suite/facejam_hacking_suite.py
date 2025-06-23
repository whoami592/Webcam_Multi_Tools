import os
import time
import sys
from colorama import Fore, Style
import argparse

# Banner display function
def display_banner():
    banner = f"""
{Fore.RED}
   _____ _          
  |  ___| | | |         
  | |__ _ _ __   ___ 
  |___| '_ ` _ \| '_ \ 
  | |  | | | | | | | | 
  |_|  |_| |_| |_|_| |_| 
                        
{Fore.GREEN}FaceJam Hacking Suite v1.0
Coded by Pakistani Ethical Hacker: Mr. Sabaz Ali Khan
{Fore.YELLOW}----------------------------------------------
{Fore.WHITE}Ethical Hacking Toolkit for Educational Purposes Only
Use Responsibly and Legally
{Fore.YELLOW}----------------------------------------------
{Style.RESET_ALL}
    """
    print(banner)

# Network Scanner Placeholder
def network_scanner(target):
    print(f"{Fore.BLUE}[*] Initiating network scan on {target}...{Style.RESET_ALL}")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Scan complete. Found open ports: 80, 443{Style.RESET_ALL}")

# Password Cracker Placeholder
def password_cracker(target_file):
    print(f"{Fore.BLUE}[*] Attempting to crack passwords in {target_file}...{Style.RESET_ALL}")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Cracking attempt finished. Results saved to output.txt{Style.RESET_ALL}")

# Vulnerability Scanner Placeholder
def vuln_scanner(target):
    print(f"{Fore.BLUE}[*] Scanning {target} for vulnerabilities...{Style.RESET_ALL}")
    time.sleep(2)
    print(f"{Fore.GREEN}[+] Found potential vulnerabilities: XSS, SQLi{Style.RESET_ALL}")

# Main Menu
def main_menu():
    while True:
        print(f"\n{Fore.CYAN}=== FaceJam Hacking Suite Menu ==={Style.RESET_ALL}")
        print("1. Network Scanner")
        print("2. Password Cracker")
        print("3. Vulnerability Scanner")
        print("4. Exit")
        
        choice = input(f"{Fore.YELLOW}Select an option (1-4): {Style.RESET_ALL}")
        
        if choice == "1":
            target = input("Enter target IP or domain: ")
            network_scanner(target)
        elif choice == "2":
            target_file = input("Enter password file path: ")
            password_cracker(target_file)
        elif choice == "3":
            target = input("Enter target URL: ")
            vuln_scanner(target)
        elif choice == "4":
            print(f"{Fore.RED}[!] Exiting FaceJam Hacking Suite. Stay Ethical!{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}[-] Invalid option. Please try again.{Style.RESET_ALL}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="FaceJam Hacking Suite by Mr. Sabaz Ali Khan")
    parser.add_argument("--target", help="Specify target for quick scan")
    args = parser.parse_args()
    
    display_banner()
    
    if args.target:
        print(f"{Fore.BLUE}[*] Quick scan initiated for {args.target}{Style.RESET_ALL}")
        network_scanner(args.target)
    else:
        main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operation interrupted by user. Exiting...{Style.RESET_ALL}")
        sys.exit(1)
