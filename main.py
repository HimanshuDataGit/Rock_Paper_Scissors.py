import random
<<<<<<< HEAD
choice =  int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

=======
choice =  int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
user = 0
pc = 0
>>>>>>> 61fa1d98fc38261fd2c8ada85c7be49481f7bc4c
computer = random.randint(0,2)
user = choice
pc = computer


if choice ==1:
    user = '''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________)'''
elif choice == 0:
    user = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)'''
elif choice == 2:
    user = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)'''   


if computer == 0:
    pc = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)'''
elif computer ==1:
    pc ='''
          _______
      ---'   ____)____
                ______)
                _______)
               _______)
      ---.__________) '''
elif computer == 2:
    pc = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)'''


if (choice >2 or choice<0):
    print("You choose an invalid number, please choose a valid number.")     
elif (choice == computer):
        print(f"Player:{user}\nComputer:{pc}\n\nIt's a Draw!!.")
elif(choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice ==2 and computer==1):
        print(f'Player:{user}\nComputer:{pc}\n\nCongrats!! You won.')
elif(computer==0 and choice==2) or (computer==1 and choice==0) or (computer==2, choice==1):
<<<<<<< HEAD
        print(f'Player:{user}\nComputer:{pc}\n\nBad luck!! you lost.')
=======
    print(f'Player:{user}\nComputer:{pc}\n\nBad luck!! you lost.')
>>>>>>> 61fa1d98fc38261fd2c8ada85c7be49481f7bc4c
