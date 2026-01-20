import os
import time

def start_boot():
    os.system("figlet -f slant 'gemboot'")
    print("[-] Waiting for iPhone 6 in DFU mode...")
    os.system("python3 everything/ipwndfu -p") 
    time.sleep(5)
    print("Waiting...")
    os.system("python3 everything/ipwndfu --load ./pongoOS.bin")

if __name__ == "__main__":
    start_boot()