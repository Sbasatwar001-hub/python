import json, os, re

R = "\033[31m"; G = "\033[32m"; Y = "\033[33m"; B = "\033[34m"; C = "\033[36m"; M = "\033[35m"; W = "\033[0m"; BOLD = "\033[1m"
FILE_NAME = "bank_data.json"
valid_domains = (".com", ".org", ".net", ".info", ".edu", ".gov", ".in", ".co.in", ".org.in", ".net.in")

def load_database():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f: return json.load(f)
        except: pass
    return {
        "Admin@123": {"password": "admin@1232", "name": "Admin", "email": "admin@bank.in", "mobile": "9999999999", "balance": 0}
    }

def save_database():
    with open(FILE_NAME, "w") as f: json.dump(Database, f, indent=4)

def is_valid_password(p):
    if len(p) < 6: return False
    if p.isdigit() or p.isalpha(): return False
    if " " in p: return False
    return True

def is_password_exists(p):
    # check karega kya ye password pehle se kisi me hai
    for user_data in Database.values():
        if user_data.get("password") == p:
            return True
    return False

def is_valid_email(e):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, e) and e.endswith(valid_domains)

Database = load_database()

print(f"{B}{BOLD}\n\t\t╔════════════════════════╗{W}")
print(f"{B}{BOLD}\t\t║ WELCOME TO MY BANK ║{W}")
print(f"{B}{BOLD}\t\t╚════════════════════════╝{W}")

while True:
    
    print(f"{G}\n1. Login{W}"); print(f"{G}2. Create your account{W}"); print(f"{R}3. Exit Bank{W}")
    try:
        a = int(input(f"{Y}\n\tEnter your choice (1-3): {W}").strip())
    except:
        print(f"{R}\t Sirf 1, 2, 3 dalo!{W}"); continue

    if a == 1:
        username = input(f"{Y}\nEnter username: {W}").strip()
        password = input(f"{Y}Enter password: {W}").strip()
        if not username or not password: print(f"{R}Khali nahi!{W}"); continue

        if username in Database and Database[username]["password"] == password:
            print(f"{G}{BOLD}\n\t-----<Login successful!>-----{W}")
            print(f"{M}\n Welcome back {W}{BOLD}{Database[username]['name']}{W}")
            
            current_balence = Database[username].get("balance", 0)
            while True:
                print(f"{B}\n\n---- ATM MENU -----{W}")
                print(f"{G}1. Balance Check{W}"); print(f"{G}2. Deposit{W}"); print(f"{G}3. Withdraw{W}"); print(f"{R}4. Logout{W}")
                try:
                    User_choice = int(input(f"{Y}\n\tChoice (1-4): {W}").strip())
                except:
                    print(f"{R}\t 1-4 dalo!{W}"); continue

                if User_choice == 1:
                    print(f"{C}{BOLD}\nApka balance Rs.: {current_balence}{W}")
                elif User_choice == 2:
                    while True:
                        try:
                            amt_str = input(f"{Y}Enter your amount: {W}").strip()
                            Deposit_amount = float(amt_str)
                            if Deposit_amount <= 0 or Deposit_amount > 1000000: raise ValueError
                        except:
                            print(f"{R}Invalid amount please enter valid amount{W}\n"); continue
                        break
                    current_balence += Deposit_amount
                    Database[username]["balance"] = current_balence; save_database()
                    print(f"{G}Deposit successful! Total: Rs. {current_balence}{W}")
                elif User_choice == 3:
                    while True:
                        try:
                            amt_str = input(f"{Y}Enter your amount: {W}").strip()
                            Withdraw_amount = float(amt_str)
                            if Withdraw_amount <= 0 or Withdraw_amount > current_balence: raise ValueError
                        except:
                            print(f"{R}Invalid amount please enter valid amount{W}\n"); continue
                        break
                    current_balence -= Withdraw_amount
                    Database[username]["balance"] = current_balence; save_database()
                    print(f"{G}Withdraw successful! Total: Rs. {current_balence}{W}")
                elif User_choice == 4:
                    print(f"{M}\nLogout ho raha hai...{W}"); break
                else: print(f"{R}1-4 chuno{W}")
        else:
            print(f"{R}Invalid username or password!{W}")

    elif a == 2:
        print(f"{C}\n\t--- Create Account ---{W}")

        
        name = input(f"{Y}\nEnter your Full name : {W}").strip()
        while len(name) < 6 or not name.replace(" ","").isalpha():
            print(f"{R}Invalid name please enter valid name{W}\n")
            name = input(f"{Y}Full name: {W}").strip()

        mobile_no = input(f"{Y}Enter your Mobile no.: {W}").strip()
        while not (len(mobile_no)==10 and mobile_no.isdigit() and mobile_no[0] in "6789"):
            print(f"{R}Invalid mobile please enter valid mobile{W}\n")
            mobile_no = input(f"{Y}Mobile: {W}").strip()

        email = input(f"{Y}Email: {W}").strip()
        while not is_valid_email(email):
            print(f"{R}Invalid email please enter valid email{W}\n")
            email = input(f"{Y}Email: {W}").strip()
            
        while True:
            new_user = input(f"{Y}\n\nCreat your username: {W}").strip()
            if not new_user or " " in new_user:
                print(f"{R}Invalid username please enter valid username{W}\n"); continue
            if new_user in Database:
                print(f"{R}Username already exist try another{W}\n")
                continue
            break


        while True:
            new_pass = input(f"{Y} Creat your Password: {W}").strip()
            if not is_valid_password(new_pass):
                print(f"{R}Invalid password please enter valid password{W}\n"); continue

            if is_password_exists(new_pass):
                print(f"{R}Password already given try another{W}\n")
                continue

            confirm = input(f"{Y}Confirm password: {W}").strip()
            if new_pass!= confirm:
                print(f"{R}Password not matched please try again{W}\n"); continue
            break

        Database[new_user] = {"password": new_pass, "name": name, "email": email, "mobile": mobile_no, "balance": 0}
        save_database()
        print(f"{G}{BOLD}Account ban gaya! Ab login karo.{W}")

    elif a == 3:
        print(f"{R}{BOLD}Bank band. Dhanyawad!{W}"); 
        break