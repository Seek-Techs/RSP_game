import random
import os
import time
 
def clear():
    os.system("clear")
 
# Set of instructions for Rock-Paper-Scissors
def rps_instructions():
 
    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()

def rps():
     
    global rps_table
    global game_map
    global name
    
    # counting the number of games for loosing, winning, tieing
    l = 0
    w = 0
    t = 0
    total_game = 0 
    
    # Game Loop for each game of Rock-Paper-Scissors
    while True:
 
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
 
        print()
    
        # Get the computer move randomly
        computer_action = random.choice(game_map)
        
        
        # Player Input
        inp = input("Enter your move : ")
    
 
        if inp.lower() == "help":
            clear()
            rps_instructions()
            #continue
        elif inp.lower() == "exit":
            clear()
            break
        elif inp.lower() == computer_action:
            print("Computer making a move....")
            print()
            time.sleep(2)
            print("Computer chooses ", computer_action.upper())
           
            t = t + 1
            total_game += 1
            print("TIE GAME", t)
            print('Total game played', total_game)
        
        elif inp.lower() == "rock":
            print("Computer making a move....")
            print()
            time.sleep(2)
            if computer_action == "scissors":
                
                # Print the computer move
                print("Computer chooses ", computer_action.upper())
                
                w = w + 1
                total_game += 1
                
                print("Rock smashes scissors! You win!", w)
                print('Total game played', total_game)
            else:
                # Print the computer move
                print("Computer chooses ", computer_action.upper())
                l = l + 1
                total_game += 1
                print("Paper covers rock! Youeeeee lose.", l)
                print('Total game played', total_game)
        elif inp.lower() == "paper":
            print("Computer making a move....")
            print()
            time.sleep(2)
            if computer_action == "rock":
                # Print the computer move
                print("Computer chooses ", computer_action.upper())
                
                w = w + 1
                total_game += 1
                print("Paper coverwwwws rock! You win!", w)
                print('Total game played', total_game)
                
            else:
                # Print the computer move
                print("Computer chooses ", computer_action.upper())
                l = l + 1
                total_game += 1
                print("Scissors cuts paper! You lose.", l)
                print('Total game played', total_game)
                
        elif inp.lower() == "scissors":
            print("Computer making a move....")
            print()
            time.sleep(2)
            if computer_action == "paper":
                print("Computer chooses ", computer_action.upper())
                
                w = w + 1
                total_game += 1
                print("Scissors cuts paper! You win!", w)
                print('Total game played', total_game)
            else:
                # Print the computer move
                print("Computer chooses ", computer_action.upper())
                l = l + 1
                total_game += 1
                print("Rock smashes scissors! You lose.", l)
                print('Total game played', total_game)
     
        else:
            clear()
            print("Wrong Input!!")
            rps_instructions()
            continue
           
        

if __name__ == '__main__':
 
    # The mapping between moves and numbers
    game_map = ["rock", "paper", "scissors"]

     
    name = input("Enter your name: ")
 
    # The GAME LOOP
    while True:
 
        # The Game Menu
        print()
        print("Let's Play!!!")
       
        print("Enter 1 to play Rock-Paper-Scissors")
       
        print("Enter 2 to quit")
        print()
 
        # Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            clear()
            print("Wrong Choice")   
            continue
 
        # Play the traditional version of the game
        if choice == 1:
            rps()

        # Quit the GAME LOOP    
        elif choice == 2:
            print('Thanks for playing')
            break
 
        # Other wrong input
        else:
            clear()
            print("Wrong choice. Read instructions carefully.")




