
import random
import string

print('Sveiki atvyke i saugiu slaptazodziu generatoriu!')

length = int(input('\nIveskite skaitmeni, keliu simboliu slaptazodzio noretumete(minimaliai keturi skaitmenys):  '))

"""
while True:
    length = int(input('\nIveskite skaitmeni, keliu simboliu slaptazodzio noretumete(minimaliai keturi skaitmenys):  '))

    if length < 4:
        print("Iveskite didesni skaitmeni, nei 4")
"""
length = int(input('\nIveskite skaitmeni, keliu simboliu slaptazodzio noretumete(minimaliai keturi skaitmenys):  '))

while True:
        length = int(input('\nIveskite skaitmeni, keliu simboliu slaptazodzio noretumete(minimaliai keturi skaitmenys):  '))
        if length in ('Iveskite skaitmeni, keliu simboliu slaptazodzio noretumete(minimaliai keturi skaitmenys):  ')
            break
        print("invalid input.")
    if length < 4:
        continue
    else:
        print("Iveskite ilgesni slaptazodi")
        break

mazosios = string.ascii_lowercase
didziosios = string.ascii_uppercase
skaiciai = string.digits
simboliai = string.punctuation


all = mazosios + didziosios + skaiciai + simboliai

temp = random.sample(all,length)

password = "".join(temp)



print(password)