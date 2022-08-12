from operator import length_hint
import random

print('Bme vindo ao Gerador de senhas')

chars = 'abcdefghijklmnopqrstuwxyz1234567890>,@$%¨&*!>;~ç][/;|^ABCDEFJKMNLOPQRSTUVWXZY'

number = input('Valor de senhas geradas: ')
number = int(number)

length = input ('tamanho da senha: ')
length = int(length)

print('\naqui estao suas senhas: ')

for pwd in range(number):
    passwords  = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)