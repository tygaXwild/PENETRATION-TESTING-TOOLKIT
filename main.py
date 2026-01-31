from utils.banner import show_banner
from scanner.port_scanner import port_scan
from attacks.brute_forcer import brute_force

def main():
    show_banner()

    print("\nChoose a module:")
    print("1. Port Scanner")
    print("2. Brute Force Simulator")

    choice = input("\nEnter choice (1/2): ")

    if choice == "1":
        target = input("Target IP/Host: ")
        start_port = int(input("Start Port: "))
        end_port = int(input("End Port: "))
        port_scan(target, start_port, end_port)

    elif choice == "2":
        username = input("Username: ")
        passwords = ["1234", "admin", "password", "root", "letmein"]
        correct_password = input("Set correct password (for simulation): ")
        brute_force(username, passwords, correct_password)

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
