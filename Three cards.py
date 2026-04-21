import random
import time
import sys

def clear_screen():
    # Simple way to clear the console for a clean look
    print("\n" * 50)

def show_rules():
   
    print("           🏺 THE OFFICIAL MATKA RULES 🏺           ")
    
    print("\n  1. THE DRAW:")
    print("   - Two draws happen: 'OPEN' and 'CLOSE'.")
    print("   - Each draw picks 3 cards (1-9).")
    print("   - The sum of these 3 cards gives the 'Ank' (Single).")
    print("   - Example: 1, 2, 5 -> Sum 8 -> Result is 125-8")
    print("\n  2. THE JODI:")
    print("   - The Open Ank and Close Ank combine to form a 2-digit Jodi.")
    print("   - Example: Open 8, Close 4 -> Jodi is 84.")
    print("\n  3. PAYOUT RATES (The 'Profit'):")
    print("   - SINGLE (1 digit) : 9x  (Bet 100 -> Win 900)")
    print("   - JODI   (2 digits): 90x (Bet 100 -> Win 9,000)")
    print("   - PANNA  (3 digits): 280x(Bet 100 -> Win 28,000)")
    
    input(" \n      PRESS ENTER TO START YOUR BETS...            ")

def get_panna():
    digits = [random.randint(1, 9) for _ in range(3)]
    digits.sort()
    ank = sum(digits) % 10
    return "".join(map(str, digits)), ank


def main():
    show_rules()
    clear_screen()

    print("---  PLACE YOUR BETS  ---")
    print("Types: [1] Single  [2] Jodi  [3] Panna")
    
    choice = input("Select Bet Type (1/2/3): ")
    
    if choice == '1':
        bet_name = "Single"
        user_pick = input("Pick a Single Digit (1-9): ")
        payout = 9
    elif choice == '2':
        bet_name = "Jodi"
        user_pick = input("Pick a Jodi (11-99): ")
        payout = 90
    elif choice == '3':
        bet_name = "Panna"
        user_pick = input("Pick a Panna (3 digits, e.g., 125): ")
        payout = 280
    else:
        print("Invalid Choice!")
        return

    try:
        amount = float(input(f"Amount to bet on {user_pick}: ₹"))
    except ValueError:
        print("Enter a valid money amount.")
        return

    print("\n[LIVE] DRAW STARTING...")
    time.sleep(1)

    # Open Draw
    open_panna, open_ank = get_panna()
    print(f"OPEN RESULT  ---> {open_panna} (Ank: {open_ank})")
    time.sleep(1.5)

    # Close Draw
    close_panna, close_ank = get_panna()
    print(f"CLOSE RESULT ---> {close_panna} (Ank: {close_ank})")
    time.sleep(1)

    # Final Result
    jodi = f"{open_ank}{close_ank}"
    full_result = f"{open_panna}-{jodi}-{close_panna}"

    print(f"\n      FINAL CARD: {full_result}")
    

    # Logic to check win
    win = False
    if choice == '1' and user_pick == str(open_ank):
        win = True
    elif choice == '2' and user_pick == jodi:
        win = True
    elif choice == '3' and (user_pick == open_panna or user_pick == close_panna):
        win = True

    if win:
        print(f"🎉 MUBARAK HO! You won ₹{amount * payout}!")
    else:
        print(" Better luck next time. The Matka King takes it all.")
        print("\n--- WINNING COMBINATIONS FOR THIS ROUND ---")
        print(f"To win SINGLE, you should have picked: {open_ank}")
        print(f"To win JODI, you should have picked:   {jodi}")
        print(f"To win PANNA, you should have picked:  {open_panna} or {close_panna}")

if __name__ == "__main__":
    main()