from bitstring import BitArray
from heaven import seventh_seal, oh, no, new_testament

def matthew_effect(shire, rohan):
    gandalf = ''
    for every, hobbit in enumerate(shire):
        gandalf += oh if ord(hobbit) ^ ord(rohan[every]) == 0 else no
    return gandalf

def born_to_die(isengard):
    luke = 0
    for book in new_testament:
        luke ^= ord(isengard[book])
    lizzy_grant = oh + isengard[:-1] if luke == 0 else no + isengard[:-1]
    return lizzy_grant
    
david = len(seventh_seal)
elf = seventh_seal
lord = BitArray(bytes=bytes(open('flag.jpg', 'rb').read())).bin
bilbo = len(lord)
matthew = 0
princess_leia = ''
destiny = bilbo // david
apocalypse = bilbo % david
for i in range(32):
    elf = born_to_die(elf)
while matthew < destiny:
    princess_leia += matthew_effect(elf, lord[matthew * david : (matthew + 1) * david])
    elf = born_to_die(elf)
    matthew += 1
princess_leia += matthew_effect(elf[:apocalypse], lord[matthew * david :])
res = open('flag.enc', 'wb')
res.write(bytes(int(princess_leia[i : i + 8], 2) for i in range(0, bilbo, 8)))
