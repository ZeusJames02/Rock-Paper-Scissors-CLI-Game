import os, random

""" Rock, Paper, and Scissors """

options = ["ROCK", "PAPER", "SCISSORS"]
scores = [0, 0]
status = ["\n\t\t\t\t ■ YOU WIN!", "\n\t\t\t\t ■ YOU LOSE!"]
start = False

def change_color(stat):
     if stat:
          print(status[0])
          os.system("color a")
     else:
          print(status[1])
          os.system("color c")

while True:
     os.system("color 7")
     print("\n\n\t    ▄■▀■▄■▀■▄■▀■▄■▀ ROCK, PAPER, AND SCISSORS ▄■▀■▄■▀■▄■▀■▄■▀\n")
     
     print("\t\t\t\t  SCORE: %d - %d\n" %(scores[0], scores[1]))

     for index in range(0, len(options)):
          print("\t\t\t\t %d - %s" %(index+1, options[index]))

     try:
          player = int(input("\n\t\t\t\t  SELECT: "))
     except:
          player = -1
     cpu = random.choice([1, 3])

     if player in [1, 2, 3]:
          if player == 1 and cpu == 2:
               scores[1] += 1
               change_color(0)
          elif player == 1 and cpu == 3:
               scores[0] += 1
               change_color(1)
          elif player == 2 and cpu == 1:
               scores[0] += 1
               change_color(1)
          elif player == 2 and cpu == 3:
               scores[1] += 1
               change_color(0)
          elif player == 3 and cpu == 1:
               scores[1] += 1
               change_color(0)
          elif player == 3 and cpu == 2:
               scores[0] += 1
               change_color(1)
          else:
               print("\n\t\t\t\t IT'S A DRAW!")

          print("\n\t\t\t\t ■ PLAYER: %s" %options[player-1])
          print("\t\t\t\t ■ CPU: %s" %options[cpu-1])
     else:
          print("\n\t\t\t\t ■ INVALID INPUT!")
     input("\n\t\t\t    Press any key to continue...")
          
     os.system("cls")
