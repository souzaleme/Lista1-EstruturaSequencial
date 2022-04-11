'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
este link (em minutos)'''

tamanho = int(input('Digite o tamanho do arquivo em MB: '))
velocidade = int(input('Digite a velocidade em Mbps: '))
velocidade_byte = velocidade / 8
tempo_seg = tamanho / velocidade_byte
tempo_min = tempo_seg / 60
print(f'o tempo para download será de {tempo_min} minutos')