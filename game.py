# Import libraries
import os
import random

# Import quotes from quotes.py
from quotes import eighties, nineties, thousands, tenthousands

# Global variables
decades = ["1) 1980s", "2) 1990s", "3) 2000s", "4) 2010s"]

# Clear screen function
def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

# Game class logic
class Game:
    
    def __init__(self, **kwargs):
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def welcome(self):
        # Game title
        print("="*20)
        print("MOVIE QUOTE TRIVIA")
        print("="*20)
        
        # Ask for player name
        global player
        player = input("\nWhat is your name? ")
        player = player.title()
        
        # Explain the game instructions
        clear()
        print(f"\nHello, {player}!\n")
        print("Here's how the game works...")
        print("10 famous quotes from your selected decade (1980s, 1990s, 2000s, 2010s) will be presented to you.")
        print("Your job is to GUESS the MOVIE that quote comes from.")
        print("\nYou will have 3 chances to guess each turn.")
        print("Don't worry about capitalization but spelling does count!")
        print("\nLastly, if the movie is part of a trilogy or saga, only guess the saga name.")
        print("(i.e. JUST Harry Potter NOT Harry Potter: The Half Blood Prince)")
        enter = input("\nPress enter...")
        
    def choose_decade(self):
        # Clear screen
        clear()
        
        print(f"\nOkay, {player}... Let's start by choosing a decade!\n")
        # List available decades to choose from
        for decade in decades:
            print(decade)
        try:
            # Ask the player which decade they would like to play from  
            print("\nselect 1, 2, 3 or 4...")
            global game_choice 
            game_choice = int(input())
            # In case player selects wrong option
            while game_choice >= 5:
                print("Oh no! Please select only 1, 2, 3 or 4...")
                game_choice = int(input())
            # 1980s
            if game_choice == 1:
                # Clear screen
                clear()
                print(f"You chose the 80s! Ready?")
                enter = input("\nPress enter...")
            # 1990s
            elif game_choice == 2:
                # Clear screen
                clear()
                print(f"You chose the 90s! Ready?")
                enter = input("\nPress enter...")
            # 2000s
            elif game_choice == 3:
                # Clear screen
                clear()
                print(f"You chose the 2000s! Ready?")
                enter = input("\nPress enter...")
            # 2010s
            elif game_choice == 4:
                # Clear screen
                clear()
                print(f"You chose the 2010s! Ready?")
                enter = input("\nPress enter...")
        except ValueError:
            print("Whoops! That's not a valid value...")
        except NameError:
            print("Whoops! That's not a valid value...")

    # Play the game        
    def play(self):
        # Clear screen
        clear()
        
        # Randomly select 10 k, v pairs from selected dictionary
        if game_choice == 1:
            game_quotes = random.sample(eighties.items(), 10)
        elif game_choice == 2:
            game_quotes = random.sample(nineties.items(), 10)
        elif game_choice == 3:
            game_quotes = random.sample(thousands.items(), 10)
        elif game_choice == 4:
            game_quotes = random.sample(tenthousands.items(), 10)
            
        
        right = 0
        wrong = 0
        # Iterate through 10 random selections and ask the player to guess the correct answer
        count = 1
        for k,v in game_quotes:
            # Clear screen
            clear()
            print("="*20)
            print("Movie Quote Trivia")
            print("="*20)
            print(f"\nQUOTE #{count}:")
            print(v)
            
            print("\nANSWER:")
            chances = 1
            choice = input()
            while choice.lower() != k.lower():
                if chances < 3:
                    print("\nOh no! That's not quite right... Try again!")
                    chances += 1
                    print("\nANSWER:")
                    choice = input()
                elif chances >= 3:
                    print(f"\nSorry {player}... The correct answer is '{k}'")
                    wrong += 1
                    count += 1
                    print("\nPress Enter for next quote...")
                    enter = input()
                    
            if choice.lower() == k.lower():
                print(f"\nYou got it, {player}!")
                right += 1      
                count += 1
            enter = input("Press Enter for next quote...")
        
        if count > 10:
            # Clear screen
            clear()
            print(f"Alright, {player}, that's all for this round!\n")
            enter = input("Press Enter to see your score...")
            
            clear()
            print(f"You got {right} out of 10 correct. Thank you for playing!")       
                    