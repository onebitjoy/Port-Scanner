import socket
from colorama import Fore as F

def scan_port(ipadr,port):
    try:
        sock = socket.socket()
        sock.connect((ipadr,port))
        sock.close()
        return True
    except:
        return False

def scan(target,ports):
    print(F.YELLOW+f'Checking ports on {target} \n--------------------------------')

    open_port_list=[]
    closed_port_list=[]

    if(type(ports)==list):
        for port in ports:
            if(scan_port(target,port) ):
                open_port_list.append(int(port))
            else:
                closed_port_list.append(int(port))
    else:
        for port in range(1,ports+1):
            if(scan_port(target,port)):
                open_port_list.append(int(port))
            else:
                closed_port_list.append(int(port))
    if(len(open_port_list)==0):
        print(F.RED+f'All ports closed!\n[-]Closed ports - {closed_port_list}')
    else:
        print(F.GREEN+f'[+] Open Ports - {open_port_list}'+'\n'+F.RED+f'[-] Closed Ports - {closed_port_list}')

targets = input(F.BLUE+'[*] Enter target machine: ')
c = input(F.CYAN+'1.Scan popular ports\t2.Scan sequential ports\n[*] Enter your choice - ')

if(c=='2'):
    ports = int(input(F.CYAN+'[*]Number of ports to scan: '))
else:
    ports = [20,21,22,23,24,25,80,100,443]
    
print('='*40)

if ',' in targets:
    for target in targets.split(','):
        scan(target,ports)
else:
    scan(targets,ports)
