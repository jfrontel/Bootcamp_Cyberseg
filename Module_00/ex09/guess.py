import random

nb_lucky = 100
nb_random = random.randrange(1,5)
print ("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.")
print ("Type 'exit' to end the game.\nGood luck!")

def ft_do_question():
    print("What's your guess between 1 and 99?\n >> ", end='')
    nb_lucky = input()
    if nb_lucky == 'exit':
        exit("Goodbye!")
    if nb_lucky.isalpha() == True:
        print("That's not a number.")
        return int(100)
    elif int(nb_lucky) <= 20 and int(nb_lucky) > 0:
        return (int(nb_lucky))  
    else:
        print("Numero no valido")
        return int(100)

i = 0
while nb_random != nb_lucky:
    nb_lucky = ft_do_question()
    
    if nb_lucky > nb_random and nb_lucky < 100:
        print('Too high!')
    elif nb_lucky < nb_random and nb_lucky >= 0:
        print('Too low!')
    i = i + 1
else:
    if (i == 1):
        print("WOW!! Has acertado a la PRIMERA!!!")
    if (i == 42):
        print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("Congratulations! You got it on your first try!!")
    else:
        print("Congratulations, you've got it!")
        print(f'You won in {i} attempts!')