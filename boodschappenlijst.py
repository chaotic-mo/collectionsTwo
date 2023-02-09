from collections import Counter
"""
#lijst nodig om het item toe te voegen
#daarna de vraag of er meer zijn
# lijst bestaat uit: item/hoeveel
# item mag maar 1 keer benoemd worden
# item die dubbel is word nummer 2
#lijst wordt geprint naar de gebruiker
"""
print("Als u klaar bent type: exit!")
boodschappenlijst = []

while True:
    vraag = input("Wat moet u hebben?: ")
    if vraag == "exit":
        break
    boodschappenlijst.append(vraag)
print(Counter(boodschappenlijst))
