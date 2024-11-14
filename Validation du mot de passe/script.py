mdp = input('Veuillez entrer un mot de passe : ')
while 1:
    testmdp = input('Veuillez confirmer votre mdp : ')
    if mdp == testmdp:
        print('Mot de passe validé !')
        break
    else:
        print('Les deux mots de passe ne correspondent pas ! ')
        