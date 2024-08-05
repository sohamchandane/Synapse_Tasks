gadgets = [
    ("Explosive Batarangs", 3, True),
    ("Batarangs", 5, True),
    ("Smoke Pellets", 0, False),
    ("Tear Gas Grenades", 2, True),
    ("Night Vision Goggles", 1, True),
    ("Catclaw", 0, False),
    ("Grapple Gun", 3, True),
    ("Batsignal", 0, False),
    ("Utility Belt", 1, True),
    ("Stars", 1, True),
    ("Bombs", 3, True),
    ("Batmobile Tires", 4, True)
]

gadgets = list(map(lambda tup: (tup[2], tup[1], tup[0]), gadgets))
#In above code, I swapped the position of boolean values and string values for better readability

gadgets.sort(key=lambda tup: (-tup[1], tup[2]))
'''This sorts the list, -tup[1] is used because:-

    What happened without '-' sign, the output would be:
        (True, 1, 'Utility Belt')
        (True, 1, 'Stars')
        (True, 1, 'Night Vision Goggles')
        i.e. sorted in descending order

    -tup[1] helped it fix, it displayed:
        (True, 1, 'Night Vision Goggles')
        (True, 1, 'Stars')
        (True, 1, 'Utility Belt')
        i.e. sorted in ascending order
'''

print(*gadgets, sep="\n")