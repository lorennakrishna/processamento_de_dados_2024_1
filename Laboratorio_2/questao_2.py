'''Crie um programa que determine a quantidade de dias que existe em um determinado mês do ano. Você pode
se referir ao mês do ano pelos números de 1 a 12 ao invés do nome e ter como padrão que a distribuição de
dias para este calendário é a de um ano que não é bissexto. '''

#base 2023

fevereiro = 28
abril = junho = setembro = novembro = 30
janeiro = março = maio = julho = agosto = outubro = dezembro = 31 

#print(maio)'''
'''
lanche = ('batata_frita', 'pudim')

print(lanche[1])'''

teste = int(input('Digite um numero de 1 a 12: '))

if (teste >= 1 and teste <= 12 ):
    mes_um = ('',janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro)
    print(mes_um[teste])
    
else:
    print('numero invalido')
    
    
    