import time
num = int(input('Veuillez entrer un nombre entier : '))
print('Debut du compte a rebours ...')
while num>=0:
    print(num)
    num -= 1
    time.sleep(1)
print('Fin du compte a rebours ...')
print('Boom !!!')