'''Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área
para o usuário.'''

lado1 = float(input('Digite o primeiro lado do quadrado: '))
lado2 = float(input('Digite o segundo lado do quadrado: '))
area_qua = lado1 * lado2
dobro_area = area_qua * 2
print(f'O dobro da área do quadrado é: {dobro_area}')
