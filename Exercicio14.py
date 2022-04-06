'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário
de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

qtd_peixes = int(input('Digite a quantidade de peixes pescada em kg: '))
excesso = qtd_peixes - 50
multa = excesso * 4

if excesso > 1:
    print(f'O excesso de peso foi de {excesso} kg, e a multa a ser paga é no valor de {multa} reais')
else:
    print(f'Não precisa pagar multa')
