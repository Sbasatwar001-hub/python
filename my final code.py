import json
import os

BILL_FILE = "bills.json"

# ---------- FULL COLOR PALETTE ----------
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    # Normal colors
    RED     = "\033[31m"
    GREEN   = "\033[32m"
    YELLOW  = "\033[33m"
    BLUE    = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN    = "\033[36m"
    WHITE   = "\033[37m"
    # Bright colors
    B_RED     = "\033[91m"
    B_GREEN   = "\033[92m"
    B_YELLOW  = "\033[93m"
    B_BLUE    = "\033[94m"
    B_MAGENTA = "\033[95m"
    B_CYAN    = "\033[96m"
    B_WHITE   = "\033[97m"
    GREY      = "\033[90m"

inventory = {
    "apple": {"price": 120, "gst": 5},
    "banana": {"price": 40, "gst": 5},
    "milk": {"price": 60, "gst": 0},
    "cheese": {"price": 150, "gst": 12},
    "rice": {"price": 80, "gst": 5},
    "chips": {"price": 20, "gst": 18}
}

if os.path.exists(BILL_FILE):
    with open(BILL_FILE, "r") as f:
        all_bills = json.load(f)
else:
    all_bills = []

bill_number = len(all_bills) + 1


def save_bills():
    with open(BILL_FILE, "w") as f:
        json.dump(all_bills, f, indent=4)


def print_bill(bill_no, cart, grand_total):
    """Tall & narrow receipt-style bill print"""
    WIDTH = 34
    print(f"\n{C.B_YELLOW}{'='*WIDTH}{C.RESET}")
    print(f"{C.BOLD}{C.B_MAGENTA}{'BILL #' + str(bill_no):^{WIDTH}}{C.RESET}")
    print(f"{C.B_YELLOW}{'='*WIDTH}{C.RESET}")

    for item in cart:
        print(f"{C.B_CYAN}Item   :{C.RESET} {C.B_WHITE}{item['name']}{C.RESET}")
        print(f"{C.B_BLUE}Qty    :{C.RESET} {item['quantity']}")
        print(f"{C.GREEN}Amount :{C.RESET} \u20b9{item['amount']:.2f}")
        print(f"{C.YELLOW}GST    :{C.RESET} \u20b9{item['gst_amount']:.2f}")
        print(f"{C.B_GREEN}Total  :{C.RESET} \u20b9{item['total']:.2f}")
        print(f"{C.GREY}{'-'*WIDTH}{C.RESET}")

    print(f"{C.BOLD}{C.B_RED}{('GRAND TOTAL: \u20b9' + f'{grand_total:.2f}'):^{WIDTH}}{C.RESET}")
    print(f"{C.B_YELLOW}{'='*WIDTH}{C.RESET}")


while True:
    print(f"{C.GREY}{'='*50}{C.RESET}")
    print(f"\t{C.BOLD}{C.B_CYAN}\u2728 Welcome to Sai Super Market \u2728{C.RESET}")
    print(f"{C.GREY}{'='*50}{C.RESET}")
    print(f"\n{C.B_BLUE}1. \U0001f9fe New bill{C.RESET}")
    print(f"{C.B_BLUE}2. \U0001f4dc View all bills{C.RESET}")
    print(f"{C.B_BLUE}3. \u2795 Add items{C.RESET}")
    print(f"{C.B_BLUE}4. \U0001f6aa Exit{C.RESET}")

    try:
        choice = int(input(f"\n{C.B_MAGENTA}Enter Your choice: {C.RESET}"))
    except ValueError:
        print(f"{C.B_RED}Sahi number daalo (1-4)!{C.RESET}")
        continue

    if choice == 1:
        cart = []
        print(f"\n\t{C.B_MAGENTA}-----<Items in store>----{C.RESET}\n")
        print(f"{C.BOLD}{'Item':<10} | {'Price':<7} | {'GST'}{C.RESET}")
        print(f"{C.GREY}{'-'*28}{C.RESET}")
        for item, d in inventory.items():
            print(f"{C.B_YELLOW}{item:<10}{C.RESET} | \u20b9{d['price']:<6} | {d['gst']}%")

        while True:
            user_item = input(f"\n{C.B_MAGENTA}Kon sa item khareedna hai? (ya 'checkout' likhein): {C.RESET}").strip().lower()

            if user_item == 'checkout':
                break

            if user_item in inventory:
                try:
                    item_quantity = int(input(f"{C.B_MAGENTA}Enter quantity: {C.RESET}"))
                except ValueError:
                    print(f"{C.B_RED}Quantity number mein daalo!{C.RESET}")
                    continue

                unit_price = inventory[user_item]["price"]
                unit_gst = inventory[user_item]["gst"]

                main_amount = unit_price * item_quantity
                main_gst = (unit_gst / 100) * main_amount

                cart.append({
                    "name": user_item,
                    "quantity": item_quantity,
                    "amount": main_amount,
                    "gst_amount": main_gst,
                    "total": main_amount + main_gst
                })
                print(f"{C.B_GREEN}\u2705 {item_quantity} x {user_item} cart mein add ho gaya.{C.RESET}")
            else:
                print(f"{C.B_RED}\u274c Ye item store mein available nahi hai.{C.RESET}")

        if cart:
            # FIX: C.GOLD didn't exist in class C -> replaced with C.B_YELLOW
            print(f"\n{C.B_YELLOW}{'='*50}{C.RESET}")
            print(f"\t{C.BOLD}{C.B_YELLOW}\U0001f9fe BILL #{bill_number} \U0001f9fe{C.RESET}")
            print(f"{C.B_YELLOW}{'='*50}{C.RESET}")
            print(f"{C.BOLD}{'Item':<10}{'Qty':<6}{'Amount':<10}{'GST':<10}{'Total'}{C.RESET}")
            print(f"{C.GREY}{'-'*50}{C.RESET}")

            grand_total = 0
            for item in cart:
                print(f"{C.CYAN}{item['name']:<10}{C.RESET}{item['quantity']:<6}{item['amount']:<10.2f}{item['gst_amount']:<10.2f}{item['total']:.2f}")
                grand_total += item['total']

            print(f"{C.GREY}{'-'*50}{C.RESET}")
            print(f"{C.BOLD}{C.GREEN}\U0001f4b0 Grand Total: \u20b9{grand_total:.2f}{C.RESET}")

            new_bill = {"bill_no": bill_number, "items": cart, "total": grand_total}
            all_bills.append(new_bill)
            save_bills()
            bill_number += 1
            print(f"{C.GREEN}\U0001f4be Bill #{new_bill['bill_no']} '{BILL_FILE}' mein save ho gaya.{C.RESET}")
        else:
            print(f"{C.RED}Cart khaali hai, koi bill nahi bana.{C.RESET}")


    elif choice == 2:
        if not all_bills:
            print(f"\n{C.B_RED}Abhi tak koi bill nahi bana.{C.RESET}")
        else:
            for b in all_bills:
                print_bill(b['bill_no'], b['items'], b['total'])

    elif choice == 3:
        new_item = input(f"{C.B_MAGENTA}Naya item ka naam: {C.RESET}").strip().lower()
        try:
            new_price = float(input(f"{C.B_MAGENTA}Price: {C.RESET}"))
            new_gst = float(input(f"{C.B_MAGENTA}GST %: {C.RESET}"))
            inventory[new_item] = {"price": new_price, "gst": new_gst}
            print(f"{C.B_GREEN}\u2705 '{new_item}' inventory mein add ho gaya.{C.RESET}")
        except ValueError:
            print(f"{C.B_RED}Price/GST number mein daalo!{C.RESET}")

    elif choice == 4:
        print(f"{C.B_CYAN}Dhanyawad! Phir milenge \U0001f44b{C.RESET}")
        break

    else:
        print(f"{C.B_RED}Galat choice, 1-4 mein se chuno.{C.RESET}")
        