import json
import os

# --- COLOR COMBINATION ---
R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
B = "\033[34m"
C = "\033[36m"
M = "\033[35m"
W = "\033[0m"
BOLD = "\033[1m"

FILE_NAME = "bank_data.json"

# --- PERMANENT SAVE / LOAD LOGIC ---
def load_database():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except:
            print(f"{R}File corrupt hai, naya data bana raha hu{W}")
    # File nahi hai to default data
    return {
        "Sai001": {"password": "sai_009", "name": "Sainath", "email": "", "mobile": "", "balance": 0},
        "Admin@123": {"password": "admin@1232", "name": "Admin", "email": "", "mobile": "", "balance": 0}
    }

def save_database():
    with open(FILE_NAME, "w") as f:
        json.dump(Database, f, indent=4)

Database = load_database()

print(f"{B}{BOLD}\n\t\t╔════════════════════════╗{W}")
print(f"{B}{BOLD}\t\t║ WELCOME TO MY BANK ║{W}")
print(f"{B}{BOLD}\t\t╚════════════════════════╝{W}")

while True:
    print(f"{G}\n1. Login{W}")
    print(f"{G}2. Create your account{W}")
    print(f"{R}3. Exit Bank{W}")

    try:
        a = int(input(f"{Y}\n\tEnter your choice (1-3): {W}"))
    except ValueError:
        print(f"{R}\t Number hi dalo! (1-3){W}")
        continue

    if (a == 1):
        print(f"{C}\n\t--- Login selected ---{W}")
        username = input(f"{Y}\nEnter username: {W}").strip()
        password = input(f"{Y}Enter password: {W}").strip()

        if not username or not password:
            print(f"{R}Username / Password khali nahi ho sakta!{W}")
            continue

        if username in Database and Database[username]["password"] == password:
            print(f"{G}{BOLD}\n\n\t-----<Login successful!>-----{W}")
            print(f"{M}\n Welcome back {W}{BOLD}{Database[username]['name']}{W}")

            current_balence = Database[username].get("balance", 0)

            while True:
                print(f"{B}\n\n---- ATM MENU -----\033[0m")
                print(f"{G}1. Balance Check\033[0m")
                print(f"{G}2. Deposit\033[0m")
                print(f"{G}3. Withdraw\033[0m")
                print(f"{R}4. Logout\033[0m")

                try:
                    User_choice = int(input(f"{Y}\n\tApna Choice (1-4) batao: {W}"))
                except ValueError:
                    print(f"{R}\t Sirf number dalo 1-4 tak!{W}")
                    continue

                if (User_choice == 1):
                    print(f"{C}{BOLD}\nApka current balance hai Rs.: {current_balence}{W}")

                elif (User_choice == 2):
                    try:
                        Deposit_amount = float(input(f"{Y}Kripaya apni rashi daliye: {W}"))
                    except ValueError:
                        print(f"{R}\t Kripaya sahi number daliye{W}")
                        continue
                    if Deposit_amount <= 0:
                        print(f"{R}\t Rashi 0 se zyada honi chahiye{W}")
                        continue
                    current_balence += Deposit_amount
                    Database[username]["balance"] = current_balence
                    save_database() # <-- YAHI SE PERMANENT SAVE HOGA
                    print(f"{G}Deposit successful! Apka total balance hai Rs.: {current_balence}{W}")

                elif (User_choice == 3):
                    try:
                        Withdraw_amount = float(input(f"{Y}Kripaya apni rashi daliye: {W}"))
                    except ValueError:
                        print(f"{R}\t Kripaya sahi number daliye{W}")
                        continue
                    if Withdraw_amount <= 0:
                        print(f"{R}\t Rashi 0 se zyada honi chahiye{W}")
                        continue
                    if Withdraw_amount > current_balence:
                        print(f"{R}\t Insufficient Balance! Apke pass sirf Rs. {current_balence} hai{W}")
                        continue
                    current_balence -= Withdraw_amount
                    Database[username]["balance"] = current_balence
                    save_database() # <-- YAHI SE PERMANENT SAVE HOGA
                    print(f"{G}Withdraw successful! Apka total balance hai Rs.: {current_balence}{W}")

                elif (User_choice == 4):
                    print(f"{M}\nLogout ho raha hai... Login page par ja rahe hain{W}")
                    Database[username]["balance"] = current_balence
                    save_database()
                    break
                else:
                    print(f"{R}\n\t Kripaya sahi vikalp chune (1-4){W}")
        else:
            print(f"{R}Invalid username or password!{W}")

    elif (a == 2):
        print(f"{C}\n\t--- Create Account ---\033[0m")
        new_user = input(f"{Y}Naya username banao: {W}").strip()
        if not new_user:
            print(f"{R}Username khali nahi ho sakta!{W}")
            continue
        if new_user in Database:
            print(f"{R}Ye username pehle se hai! Dusra try karo{W}")
        else:
            new_pass = input(f"{Y}Naya password banao: {W}").strip()
            if not new_pass:
                print(f"{R}Password khali nahi ho sakta!{W}")
                continue
            new_name = input(f"{Y}Apna naam likho: {W}").strip()
            Database[new_user] = {"password": new_pass, "name": new_name, "email": "", "mobile": "", "balance": 0}
            save_database() # <-- Naya account bhi save
            print(f"{G}Account ban gaya! Ab Login karo.{W}")

    elif (a == 3):
        print(f"{R}{BOLD}Bank band ho raha hai. Dhanyawad!{W}")
        break