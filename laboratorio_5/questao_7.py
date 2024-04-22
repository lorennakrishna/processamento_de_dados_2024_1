'''

Fa̧ca um programa que leia um conjunto de notas de provas de alunos.
Aṕos ler os valores das notas, vocˆe
deve calcular a ḿedia da turma ok

e o desvio padr ̃ao e imprim ́ı-los para o usu ́ar

'''

import math


print('Nesse programa realizaremos a média da turma e o desvio padrão dela. \nPara parar de preencher as nptas, digite "-1". \n')
aux = 0
aux_dois = 0
lista_notas = []

#recolher notas 
while (aux == 0 ):
    
    nota_um = int(input("Digite a nota: "))
    
    if (nota_um == -1):
        
        aux = 1
    
    elif (nota_um != -1):
        #aux_dois = aux_dois + 1
        lista_notas.append(nota_um) #colando as notas na lista
    
    
#calculo da media 

count = len(lista_notas)
soma_notas = sum(lista_notas)
media = soma_notas/count

#print("quantidade de notas =", count)
#print("Media =", media)

'''
lista_teste = []        
teste_input = input("Digite uma palvra")

lista_teste.append(teste_input)

print(lista_teste)'''


#calcular o devio padrao

#calcular o quadrado da diferença -> (Primeira nota - media )^2 

#lista_notas vem todas as notas de 0 ate n nas posições | media e fixo| resultado preciso colocar em outra lista 

lista_desvio = []

aux_tres = 0 
while (aux_dois == 0):

    if (aux_tres == count):
        #print('fim')
        aux_dois = 1
        
        
    elif (aux_tres != count): #count-1 = 2
       
         result_um = (lista_notas[aux_tres] - media)**2 #(10-14)**2 = (-4)**2 = 16 (RODOU)
         lista_desvio.append(result_um)
         
         #print(result_um)
         aux_tres = aux_tres + 1
        #print(result_um)    #(15-14)**2 = (1)**2 = 1
                            #(17-14)**2 = (-3)**2 = 9
    #break;

count_desvio = len(lista_desvio)
soma_desvio = sum(lista_desvio)
media_desvio = soma_desvio/count_desvio 

#o desvio-padrão é a raiz quadrada da variância
#raiz da media do desvio 
result_desvio = math.sqrt(media_desvio)

#print("Devio padrao =", result_desvio)
        
'''numero = 16
raiz_quadrada = math.sqrt(numero)
print(raiz_quadrada)'''
        
        
#NOTA NORMALIZADA

#parte_um = ((nota_um - media)/media_desvio) +3 
#parte_dois = parte_um * (10/6) #nota NORMALIZADA

parte_um = 0 
parte_dois = 0 

#print(lista_notas)
aux_quatro = 0
count_nota_normalizada = len(lista_notas)
aux_cinco = 0 

#print(count_nota_normalizada)

while (aux_cinco == 0):
    
    if (aux_quatro < count_nota_normalizada):
        
        parte_um = ((lista_notas[aux_quatro] - media)/result_desvio) +3
        parte_dois = parte_um * (10/6)
        round_partedois = round(parte_dois, 2)
        #print("teste")
        print("\nnota original:", lista_notas[aux_quatro], "nota normalizada:", round_partedois)
        aux_quatro = aux_quatro + 1 
        
    elif (aux_quatro >= count_nota_normalizada):
        
       #print("fim")
        #print(parte_dois)
        aux_cinco = 1
        

