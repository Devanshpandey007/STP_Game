# Created by Devansh Pandey
# devansh.pan11@gmail.com
import random
from time import sleep

list = []
max = 3
x = 0
for i in range(max):
    choose = str(input("Type 'rock' to choose rock, 'paper' to choose paper and 'scissor' to choose sessior\n"))
    choose = choose.lower()
    y = random.randint(0, 2)
    # y1 = rock, y2= paper and y3 = sessior

    if y == 0:
        sleep(2)
        print("PC: Rock")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

    elif y == 1:
        sleep(2)
        print("PC: Paper")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    else:
        sleep(2)
        print("PC: Scissor")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if choose == 'rock':
        x = 0
        if x == 0 and y == 1:
            sleep(1)
            print('you lost')
            list.append(0)
        elif x == 0 and y == 2:
            sleep(1)
            print('you won')
            list.append(1)
        else:
            sleep(1)
            print("It's a draw")
    elif choose == 'paper':
        x = 1
        if x == 1 and y == 2:
            sleep(1)
            print('You lost')
            list.append(0)
        elif x == 1 and y == 0:
            sleep(1)
            print("You won")
            list.append(1)
        else:
            sleep(1)
            print("It's a draw")
    else:
        x = 2
        if x == 2 and y == 0:
            sleep(1)
            print("you lost")
            list.append(0)
        elif x == 2 and y == 1:
            sleep(1)
            print("You won")
            list.append(1)
        else:
            sleep(1)
            print("It's a draw")
    print("If you won you will get '1' point , 0 point if computer won and no point if it's a draw")
    print(list)
