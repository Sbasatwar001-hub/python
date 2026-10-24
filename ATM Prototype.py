
while True:
    current_balence = 0
    print("\n\t\t===  WELCOME TO MY BANK ATM  ===")
    print("\033[32m\n\n----MENU-----\033[0m")
    print("\033[32m\n1. Balence Check\033[0m")
    print("\033[32m2. Deposit\033[0m")
    print("\033[32m3. Withdraw\033[0m")
    print("\033[31m4.Exit\033[0m")

    User_choice = int(input("\033[32m\n\tApna Choice (1-4) batao\033[0m:"))

    if (User_choice == 1):
        
        print("\033[33m\nApka current balence hai Rs.:", current_balence)

    if (User_choice == 2):
        
        Deposit_amount = float(input("\033[33mKripaya apni rashi daliye:\033[0m"))

        while (Deposit_amount <= 0):
            
            print("\033[31m\tKripaya sahi rashi daliye\033[0m")
            
            Deposit_amount = float(input("\033[33m\nKripaya apni rashi daliye:\033[0m"))

        current_balence = current_balence + Deposit_amount
        
        print("\033[33mApka total balence hai Rs.:", current_balence)

    if (User_choice == 3):
        
        Withdraw_amount = float(input("\033[33mKripaya apni rashi daliye:\033[0m"))

        while (Withdraw_amount > current_balence):
            print("\033[31m\tKripaya sahi rashi daliye (balance se zyada nahi)\033[0m")
            
            Withdraw_amount = float(input("\033[33m\nKripaya apni rashi daliye:\033[0m"))

        current_balence = current_balence - Withdraw_amount
        
        print("\033[33mApka totalbalence hai Rs.:", current_balence)

    if (User_choice == 4):
        print("\033[31m\nDhanyawad! Bank se exit ho rahe hain...\033[0m")
        
        break
        
    if(User_choice>4 or User_choice<1):
        
        print("\033[31m\n\t Kripaya sahi vikalp chune\033[0m")
        