from modules import port_scanner, brute_forcer

def display_menu():
    print("\n🔧 Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. FTP Brute-Forcer")
    print("3. Exit")

def run_port_scanner():
    host = input("\nEnter target host (e.g., 127.0.0.1): ").strip()
    ports = range(20, 1025)
    print(f"\nScanning {host} (ports 20-1024)...")
    open_ports = port_scanner.scan_ports(host, ports)
    if open_ports:
        print(f"\n🟢 Open ports found: {', '.join(map(str, open_ports))}")
    else:
        print("\n🔴 No open ports found in range 20-1024")

def run_ftp_bruteforcer():
    host = input("\nEnter FTP host (e.g., ftp.example.com : ").strip()
    username = input("Enter FTP username: ").strip()
    password_file = "passwords.txt"
    
    try:
        with open(password_file, "r") as f:
            passwords = [p.strip() for p in f.readlines() if p.strip()]
        
        if not passwords:
            print("\n⚠️ Password file is empty")
            return
            
        print(f"\nStarting brute-force attack with {len(passwords)} passwords...")
        brute_forcer.brute_force_ftp(host, username, passwords)
    except FileNotFoundError:
        print(f"\n❌ Error: '{password_file}' not found")

def main():
    while True:
        display_menu()
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            run_port_scanner()
        elif choice == "2":
            run_ftp_bruteforcer()
        elif choice == "3":
            print("\n👋 Exiting toolkit...")
            break
        else:
            print("\n❌ Invalid option. Please choose 1, 2, or 3")

if __name__ == "__main__":
    main()