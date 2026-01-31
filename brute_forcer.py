def brute_force(username, password_list, correct_password):
    print(f"\n[+] Starting brute-force simulation for user: {username}\n")

    for password in password_list:
        print(f"[*] Trying password: {password}")

        if password == correct_password:
            print(f"\n[SUCCESS] Password found: {password}")
            return

    print("\n[FAILED] Password not found in wordlist")
