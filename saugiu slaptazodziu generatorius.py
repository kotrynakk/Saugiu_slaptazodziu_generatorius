
import random
import string

print('Sveiki atvyke i saugiu slaptazodziu generatoriu!')

length = int(input('\nIveskite skaitmeni, keliu simboliu slaptazodzio noretumete(minimaliai keturi skaitmenys):  '))

mazosios = string.ascii_lowercase
didziosios = string.ascii_uppercase
skaiciai = string.digits
simboliai = string.punctuation


all = mazosios + didziosios + skaiciai + simboliai

temp = random.sample(all,length)

if length < 4:
        print("Iveskite ilgesni slaptazodi")
elif length > 4:
    password = "".join(temp)
    print("Jusu saugus slaptazodis yra " + password)

print("end of program")
