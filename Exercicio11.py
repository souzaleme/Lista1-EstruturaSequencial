'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.'''

num_1 = int(input('Digite um número inteiro: '))
num_2 = int(input("Digite outro número inteiro: "))
num_3 = float(input('Digite um número real: '))
condicao_a = (2 * num_1) * (num_2 / 2)
condicao_b = 3 * num_1 + num_3
condicao_c = num_3 ** 3

print(f'O produto do dobro do primeiro com metade do segundo é: {condicao_a}')
print(f'A soma do triplo do primeiro com o terceiro é: {condicao_b}')
print(f'O terceiro elevado ao cubo é: {condicao_c}')