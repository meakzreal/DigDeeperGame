## ==========================================
## Project: Dig Deeper
## Author: Meakz
## Purpose: You start with money, a basic drill, and a tiny underground tunnel. Your job is to dig deeper, discover valuable materials / sell them, and upgrade your Drill to DIG DEEPER!.
## ------------------------------------------
## Version: 1.0
## Created: 25/10/2026
## ==========================================

# Imports

import os
import time
import random
import pygame

# Variables for game

multiplier_drill = 1
cash = 0
random_drill_amount = [1 , 35]

# Variables

pygame.mixer.init()

Drilling_Sound = pygame.mixer.Sound("Sounds/drillingsound.wav")
Drilling_Sound.set_volume(0.1) ## 10% volume

# Quote Variables

quotes = [
    "100 Percent Of Miners Quit Before They Win Big. DO NOT be one of them!",
    "Youre good at Python, dont worry! Even rocks have bugs.",
    "Every millionaire started somewhere. You started in a hole.",
    "Your drill is terrible. Your dreams arent.",
    "The deeper you dig, the more your bank account smiles.",
    "The rocks arent going to mine themselves. Probably.",
    "Work smarter, not harder. Upgrade your drill.",
    "Youre not broke. Your money is just underground.",
    "Gold doesnt grow on trees. It grows in holes. Dig.",
    "A little bit of dirt never hurt anyone. Probably.",
    "Todays forecast: 100 percent chance of rocks.",
    "Mining is just gardening for people who hate sunlight.",
    "Meakz Industries: Digging holes so you dont have to get a real job."
]

# Definitions

def show_values():
    global cash,ready_to_leave,multiplier_drill
    os.system("cls")
    time.sleep(0.5)
    print("============")
    print(f"Cash: {cash}")
    print(f"Drill Multiplier: {multiplier_drill}")
    ready_to_leave = input("Click Enter to Leave\n>> ")
    
    if ready_to_leave == "":
        os.system("cls")
        time.sleep(1)
        start_up_screen()
        
    else:
        os.system("cls")
        time.sleep(1)
        start_up_screen()
    
def drilling_phase_1():
    global cash, multiplier_drill, random_drill_amount
     
    print("Starting drilling...")
    Drilling_Sound.play()
    time.sleep(5)
    Drilling_Sound.stop()
    cash = multiplier_drill + random.choice(random_drill_amount)
    Drilling_Sound.play()
    time.sleep(3)
    Drilling_Sound.stop()
    print("Drilling complete!")
def you_sure():
    global you_sure_q
    print("are you sure? y/n")
    you_sure_q = input(">> ")  
    if you_sure_q == "y":
        return True
        
    elif you_sure_q == "n":
        print("restarting")
        time.sleep(2)
        os.system("cls")
        time.sleep(1)
        start_up_screen()
        
def start_up_screen():
    print("=========================================")
    print("           DIG DEEPER - MENU")
    print("=========================================")
    print("⛏️  1. Start Drilling")
    print("💰 2. Sell Your Loot")
    print("3. Check Some Values")
    print("4. Hear a Quote")
    print("5. Quit — The Cave Isn't Going Anywhere...")

    choice_of_start_up_screen = input(">> ")

    if choice_of_start_up_screen == "1":
        os.system("cls")
        time.sleep(2)
        drilling_phase_1()
        time.sleep(2)
        os.system("cls")
        start_up_screen()

    elif choice_of_start_up_screen == "2":
        print("You Cant sell yet!")
        time.sleep(2)
        os.system("cls")
        time.sleep(0.5)
        start_up_screen()

    elif choice_of_start_up_screen == "3":
        print("Opening Option 3")
        time.sleep(2)
        os.system("cls")
        time.sleep(0.5)
        show_values()
        start_up_screen()

    elif choice_of_start_up_screen == "4":
        print("Opening Option 4")
        time.sleep(1)
        quote_of_the_day()
        time.sleep(2)
        os.system("cls")
        time.sleep(0.5)
        start_up_screen()

    elif choice_of_start_up_screen == "5":
        you_sure()
        print("Thanks for playing Dig Deeper!")
        time.sleep(2)
        exit()

    else:
        print("Invalid choice. Please choose 1-5.")
        time.sleep(2)
        start_up_screen()


def start_up():
    os.system("cls")
    time.sleep(1)
    print("Welcome to Dig Deeper!")
    time.sleep(1)
    os.system("cls")


def quote_of_the_day():
    os.system("cls")
    time.sleep(2)
    print(random.choice(quotes))
    time.sleep(3)


# Game Code

start_up()
quote_of_the_day()
start_up_screen()
