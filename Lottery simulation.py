import random
import time
totmon = 0
print("Welcome to the demonstration of the lottery simulation.")
time.sleep(1)
print("----MENU----")
time.sleep(1)
menu = input("1) Start\n")
if menu == "1":
    time.sleep(1)
    people = int(input("How many people are in the lottery?\n"))
    win = random.randint(1, people)
    time.sleep(1)
    money = float(input("How much does the lottery ticket cost?\n"))
    time.sleep(1)
    tr = input("Click enter to buy a ticket\n")
    for x in range(1000000000000000000000000000):
        if tr == "":
            totmon += money
            draw = random.randint(1, people)
            if draw == win:
                print("You actually won!")
                print("Took you",totmon,"to win it")
                break
            else:
                print("You did not win")
                print("You have spent",totmon,"on tickets.")
