nome = 'Djonatan '
sobrenome = 'Schvambach'
idade = 25
altura = 1.76
peso = 58
imc = peso / altura ** 2
#Utilização de Interpolação no Python
#formatação de 2 casas decimais
print(f'{nome}{sobrenome} idade {idade} IMC {imc:.2f}')
print('Nome {}{} idade {} {:.2f}'.format(nome , sobrenome, idade, imc))

anoNascimento = 2022 - idade
print(anoNascimento)