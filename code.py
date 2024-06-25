import subprocess
import sys
import os

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    if stderr:
        print("Error:", stderr.decode())

def hcitool_lescan():
    print("Running hcitool lescan...")
    run_command('sudo hcitool lescan')

def btmon_capture():
    print("Running btmon...")
    run_command('sudo btmon')

def gatttool_interactive(target):
    print(f"Running gatttool in interactive mode with target {target}...")
    run_command(f'sudo gatttool -b {target} --interactive')

def bettercap_scan():
    print("Running bettercap for BLE scanning...")
    run_command('sudo bettercap -caplet ble.recon')

def install_bettercap():
    print("Installing bettercap...")
    run_command('sudo apt-get update')
    run_command('sudo apt-get install bettercap')

def menu():
    while True:
        print("\nBluetooth Tools Menu")
        print("1. Run hcitool lescan")
        print("2. Run btmon")
        print("3. Run gatttool interactive mode")
        print("4. Run bettercap BLE scan")
        print("5. Install bettercap")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            hcitool_lescan()
        elif choice == '2':
            btmon_capture()
        elif choice == '3':
            target = input("Enter target BLE address: ")
            gatttool_interactive(target)
        elif choice == '4':
            bettercap_scan()
        elif choice == '5':
            install_bettercap()
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
