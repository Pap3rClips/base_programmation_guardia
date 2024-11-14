import random
toGuess = random.randint(0,100)
while 1:
    guess = int(input('Veuillez entrer un nombre entier : '))
    if guess == toGuess:
        print('Trouvé !!!')
        break
    elif guess < toGuess:
        print('Trop petit')
    else:
        print('Trop grand')