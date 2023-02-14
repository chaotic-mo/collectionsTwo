'''
Maak een programma die een wachtwoord van 24 tekens genereerd.
Het wachtwoord moet aan de volgende eisen voldoen:
    # 2 tot 6 hoofdletters.
    # Minimaal 8 kleine letters.
    # 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
    # De speciale tekens mogen niet op de eerste
     laatste positie staan 
     ook niet op een vaste plek.
    # 4 tot 7 cijfers (0 t/m 9).
    # Op de eerste 3 posities mag geen cijfer staan.
'''
# necessary imports 
import string, random
# defining the strings
lettersu = string.ascii_uppercase
lettersc = string.ascii_lowercase
tekens = ['@','#','$','&','_','?','.']
cijfers = string.digits
# pwd lenght
pwd_lenght = 24
# generate a pwd_string
pwd = []

for letter_upper in range(random.randrange(2, 6)):
    pwd.append(lettersu[random.randrange(len(lettersu))])
for puncuations in range(3):
    pwd.insert(6, tekens[random.randrange(len(tekens))])
for numbers in range(random.randrange(4, 7)):
    pwd.insert(3, cijfers[random.randrange(len(cijfers))])
for letter_lower in range(pwd_lenght - len(pwd)):
    pwd.append(lettersc[random.randrange(len(lettersc))])

print(pwd)
print(len(pwd))