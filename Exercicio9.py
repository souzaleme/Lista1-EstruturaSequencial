'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em
graus Celsius. C = 5 * ((F-32) / 9).'''

temp_f = float(input('Digite a temperatura e graus Fahrenheit: '))
temp_c = 5 * ((temp_f-32) / 9)
print(f'A temperatura em graus Celsius é: {temp_c}')