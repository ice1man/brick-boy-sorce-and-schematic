import random
import machine
import time
import snake
import code
#import max7219
from LiquidCrystal import LiquidCrystal

def rps():
    display_text = LiquidCrystal(4, 5, 3, 6, 7, 8, 9)
    display_text.begin(16, 2)
    display_text.clear()
    BUTTON_A_PIN = 15
    BUTTON_B_PIN = 14
    BUTTON_C_PIN = 13
    BUTTON_D_PIN = 12
    button_a = machine.Pin(BUTTON_A_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_b = machine.Pin(BUTTON_B_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_c = machine.Pin(BUTTON_C_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
    button_d = machine.Pin(BUTTON_D_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
    # Display game instructions
    display_text.print("Rock Paper Scissors")
    time.sleep(2)
    display_text.clear()
    display_text.print("Press A for Rock")
    display_text.print("B for Paper C for Scissors")

    # Wait for player input
    while True:
        if button_a.value() == 1:
            player_choice = "rock"
            
        if button_b.value() == 1:
            player_choice = "paper"
            
        if button_c.value() == 1:
            player_choice = "scissors"
            
        # Generate computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine winner
        winner = None
        if player_choice == "rock" and computer_choice == "scissors":
            winner = "player"
            display_text.print("you win")
        elif player_choice == "paper" and computer_choice == "rock":
            winner = "player"
            display_text.print("you win")
        elif player_choice == "scissors" and computer_choice == "paper":
            winner = "player"
            display_text.print("you win")
        elif player_choice == computer_choice:
            winner = "tie"
            display_text.print("tie")
        else:
            winner = "computer"
            display_text.print("you louse")

    # Display results
    #display_text.clear()
    #display_text.write("Player chose: " + player_choice)
    #display_text.write("Computer chose: " + computer_choice)
    time.sleep(4)
    #display_text.clear()
    #if winner == "player":
    #    display.write("Player wins!")
    #elif winner == "computer":
    #    display.write("Computer wins!")
    #else:
    #    display.write("Tie!")
    
    time.sleep(10)
    #display_text.clear()
    #display_text.write("press a to play again")
    #display_text.write("press c to play rock")
    # Wait for player input to play again
    #while True:
    #    if button_a.value() == 1
    #        rps()
    #    if button_c.value() == 1
    #        snake()
