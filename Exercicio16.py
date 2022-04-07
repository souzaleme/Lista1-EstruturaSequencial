'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.Informe ao usuário a quantidades
de latas de tinta a serem compradas e o preço total.'''

import math
area_pintada = int(input('Digite a área a ser pintada em m²: '))
qtd_litros = area_pintada / 3
qtd_latas = math.ceil(qtd_litros / 18)
custo = 80 * qtd_latas

print(f'Quantidade de lata(s): {qtd_latas}')
print(f'Valor da(s) lata(s): R${custo}')



