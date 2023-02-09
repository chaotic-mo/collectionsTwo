"""
# programma die 54 kaarten genereerd
# die geschut wordten 7 kaart van boven pakt
# de 7 kaarten worden getoont
# overige kaarten gaan weer terug
-------------------------------
# het deck heeft 4 kleuren: harten, klaver, schoppen, ruiten
# ieder kleur 13 kaarten in range/len 2tot10
# in het deck 2 jokers
# zonder user defined function 18 regels 
# met user defined function 28
#     zonder en met exclusief lege regels
"""
import random   
card_signs = ['Harte', 'Klaver', 'Schoppen', 'Ruiten']
card_values = ['A', 'King', 'Queen', 'Jack', '2', '3', '4', '5', '6', '7', '8', '9', '10']

deck = ['joker', 'joker']

for signs in card_signs:
    for values in card_values:
        deck.append(f"{signs} {values}")
        
random.shuffle(deck)
sevencards = deck[0:7]

del deck[0:7]
for i in range(len(sevencards)):
    print(f"Kaart {i+1}:{sevencards[i]}")
print(f"\noverige kaarten {len(deck)}:{deck}")