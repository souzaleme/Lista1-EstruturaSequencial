'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00. nforme ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
 - comprar apenas latas de 18 litros;
 - comprar apenas galões de 3,6 litros;
 - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math
qtd_area = int(input('Digite a área a ser pintada em m²: '))
qtd_area_folga = qtd_area * 1.1
qtd_litros = qtd_area_folga / 6
qtd_lata = math.ceil(qtd_litros / 18)
qtd_galao = math.ceil(qtd_litros / 3.6)
preco_lata = qtd_lata * 80
preco_galao = qtd_galao * 25
print(f'{qtd_lata} lata(s) de 18 litros, no valor de R$ {preco_lata}')
print('ou')
print(f'{qtd_galao} galão(s) de 3,6 litros, no valor de de R$ {preco_galao}')
print('ou')

# Otimizando a compra de tintas
qtd_lata_ = math.floor(qtd_litros / 18)
sobra_lata = qtd_litros % 18
qtd_galao_ = math.ceil(sobra_lata)
preco_lata_ = qtd_lata_ * 80
preco_galao_ = qtd_galao_ * 25
soma = preco_lata_ + preco_galao_
print(f'{qtd_lata_} lata(s) de 18 litros, e {qtd_galao_} galão(s) de 3,6 litros, totalizando o valor de R$ {soma}')

