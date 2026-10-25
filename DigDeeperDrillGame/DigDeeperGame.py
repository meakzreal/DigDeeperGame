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

# Variables

pygame.mixer.init()

Drilling_Sound = pygame.mixer.Sound("Sounds/drillingsound.wav")
Drilling_Sound.set_volume(0.2) ## 40% volume

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
    "Gold doesn't grow on trees. It grows in holes. Dig.",
    "A little bit of dirt never hurt anyone. Probably.",
    "Todays forecast: 100 percent chance of rocks.",
    "Mining is just gardening for people who hate sunlight.",
    "Meakz Industries: Digging holes so you dont have to get a real job."
]

# Definitions

def start_up_screen():
    print("=========================================")
    print("           DIG DEEPER - MENU")
    print("=========================================")
    print("⛏️  1. Start Drilling")
    print("💰  2. Sell Your Loot")
    print("💎  3. Check Market Prices")
    print("💬  4. Hear a Quote")
    print("🚪  5. Quit — The Cave Isn't Going Anywhere...")

    choice_of_start_up_screen = input(">> ")

    if choice_of_start_up_screen == "1":
        os.system("cls")
        print("Starting drilling...")
        Drilling_Sound.play()
        time.sleep(4)
        Drilling_Sound.stop()
        print("Drilling complete!")
        time.sleep(2)
        os.system("cls")
        time.sleep(1)
        start_up_screen()

    elif choice_of_start_up_screen == "2":
        print("You Cant sell yet!")
        time.sleep(2)
        os.system("cls")
        time.sleep(0.5)
        start_up_screen()

    elif choice_of_start_up_screen == "3":
        print("Market prices are not available yet!")
        time.sleep(2)
        os.system("cls")
        time.sleep(0.5)
        start_up_screen()

    elif choice_of_start_up_screen == "4":
        quote_of_the_day()
        time.sleep(2)
        os.system("cls")
        time.sleep(0.5)
        start_up_screen()

    elif choice_of_start_up_screen == "5":
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