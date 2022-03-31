'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.'''

salario_hora = float(input('Digite quanto você ganha por hora trabalhada: '))
num_hora_mes = float(input('Digite o número de horas trabalhadas por mês: '))
salário_mensal = salario_hora * num_hora_mes
print(f'Este mês seu salário foi de: R$ {salário_mensal}')
