import random

numero_aleatorio = random.randint(1,10)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você qual foi ?')

user_number = int(input('Qual seu palpite ? '))
erros = 0

while user_number != numero_aleatorio:
    print('Errado')
    erros += 1
    user_number = int(input('Qual próximo palpite ? '))
    if user_number > numero_aleatorio:
        print('Um pouco menos... Tente novamente.')
    elif user_number < numero_aleatorio:
        print('Um pouco mais... Tente novamente')
   


print(f'boaa, pensei exatamente no {numero_aleatorio}')
print(f'Você errou {erros} antes de acertar kkkk')