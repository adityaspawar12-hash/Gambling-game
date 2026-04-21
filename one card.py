import random
import time

def play_simple_matka():

    print("      SIMPLE MATKA (SINGLE CARD)        ")
   
    print("\n RULES: Pick a number (1-9). If the random")
    print("\n Card matches your pick, you win 9x ")
   

    try:
        user_digit = int(input("Enter your lucky digit (1-9): "))
        bet_amount = float(input("Enter your bet amount: ₹"))
        
        if not (1 <= user_digit <= 9):
            print(" Invalid digit! Choose between 1 and 9.")
            return
    except ValueError:
        print(" Invalid input! Please enter numbers only.")
        return

    print(f"\nDrawing a card")
    time.sleep(1) 

    # Simplified: Just generate ONE random number
    winning_number = random.randint(1, 9)

  
    print(f"RESULTING CARD : {winning_number}")
   

    if user_digit == winning_number:
        print(f" WINNER! You won ₹{bet_amount * 9}!")
    else:
        print(f" LOST! You should have picked: {winning_number}")
  

if __name__ == "__main__":
    play_simple_matka()