'''

Esta quest ̃ao se assemelha ao item anterior — quest ̃ao 5. Fa ̧ca um programa que leia um conjunto de notas
de provas de alunos. Ap ́os ler os valores das notas, vocˆe deve imprimir as notas dos alunos que ficaram acima
ou igual `a m ́edia da turma. Em seguida, imprima as notas so alunos que ficaram abaixo da m ́edia da turma.

'''
lista_nome_alunos = []
lista_notas_alunos = []
aux = 0


while (aux == 0):
    
    if(aux == 1):
        
        break;
        
    elif (aux != 1):
    
        nome_aluno = input("Digite o nome do aluno: ")
            
        if (nome_aluno == '-1'):
                
            #print("fim")
            #print(lista_nome_alunos)
            #print(lista_notas_alunos)
            aux = 1
            
        elif (nome_aluno != '-1'):  
            
            lista_nome_alunos.append(nome_aluno)
            notas_alunos = int(input("Digite a nota: "))
            lista_notas_alunos.append(notas_alunos)

soma_notas = sum(lista_notas_alunos)
count = len(lista_notas_alunos)
media_notas = soma_notas/count

print("A media das notas e: ", media_notas)
#print(lista_nome_alunos)
#print(lista_notas_alunos) 

aux_dois = 0

while (aux_dois < count):

    if (lista_notas_alunos[aux_dois] >= media_notas):
        
        print("acima ou igual a media:",lista_nome_alunos[aux_dois], lista_notas_alunos[aux_dois])
        
        aux_dois = aux_dois + 1  
    
    elif (lista_notas_alunos[aux_dois] < media_notas):
    
        print("menor que a media: ",lista_nome_alunos[aux_dois], lista_notas_alunos[aux_dois])
        
        aux_dois = aux_dois + 1  





