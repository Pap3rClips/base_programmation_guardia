secondes = int(input('Veuillez entrer une durée en seconde'))
heures = secondes // 3600
minutes = (secondes % 3600) // 60
secondes_restantes = secondes % 60
print('heures : ', heures)
print('minutes : ', minutes)
print('seconde : ', secondes_restantes)
