import socket

def port_scan(target, start_port, end_port):
    print(f"\n[+] Scanning Target: {target}")
    print(f"[+] Ports: {start_port} - {end_port}\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()

        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
            break
        except socket.error:
            print("[!] Could not connect to server")
            break
