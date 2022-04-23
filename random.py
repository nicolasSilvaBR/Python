#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

coin = random.randint(0,1)

choice = input('Heads or Tails ? ')

if choice == 'Heads' and coin == 1:
  print(f'{coin}')
  print('You won')
elif choice == 'Tails' and coin == 0:
  print(f'{coin}')
  print('You won')  
else:
  print(f'{coin}')
  print('You loose')
  
  
  
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock,paper,scissors]

#Write your code below this line 👇
choice = input("Rock, Paper or Scissors ?").lower()
pcchoice = random.randint(0,2)
# 0 = rock
# 1 = paper
# 2 = scissors

if choice == 'rock': 
  print(rock)
  print(options[pcchoice])
  if pcchoice == 2:
    print("You Win")
  elif pcchoice == 0:
    print("Draw")
  else:
    print("You Loose")