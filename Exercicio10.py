'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre a temperatura em
graus Fahrenheit. C = 5 * ((F-32) / 9).   F = C * 9 / 5 + 32'''

temp_c = float(input('Digite a temperatura em graus Celsius: '))
temp_f = temp_c * 9 / 5 + 32
print(f'A temperatura em graus Fahrrenheit é de: {temp_f}')