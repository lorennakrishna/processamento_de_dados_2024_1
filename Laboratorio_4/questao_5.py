
#Digite seu genero
#M ou F
#Digite sua idade

#contar homens e mulherer e depois media de idade 

genero = '0'
aux = 0
lista_M = []
lista_id_m = []

lista_F = []
lista_id_f = []

while (genero != 'x'):
    
    genero = str(input("Seu genero: "))
    
    if (genero == 'M'):
        
        #for i in range (0,10):
            #vVetor_femea_idade[i] = genero
        lista_M.append(1)   
        idade_macho = int(input("Digite sua idade: "))
        lista_id_m.append(idade_macho)
        #print(genero, idade_macho, aux)
        #aux = aux + 1
        
    
    elif (genero == 'F'):
       
        lista_F.append(1) 
        
        idade_femea = int(input("Digite sua idade: "))
        lista_id_f.append(idade_femea)
        #print(genero, idade_femea, aux)
        #aux = aux + 1
        
    elif (genero == 'x' or genero == 'X'):
            break;

#print(vVetor_femea_idade[0:10])

#mulher 

'''while (genero != 'x' or aux <= 10):

    print(genero, idade, aux)
    aux = aux + 1
    
    if (genero == 'x' or genero == 'X'):
        genero = 'x'

#print(genero)'''


#Homens = M

#soma de quantos homens tem
soma_qnt_M = sum(lista_M)
#print(soma_qnt_M)

#media idade dos homens
soma_das_idades_M = sum(lista_id_m)
media_M = soma_das_idades_M / soma_qnt_M
media_M_round = round(media_M, 2)
print("Existem", soma_qnt_M, "homens e a media de idade e", media_M_round, "anos")


#Mulheres - F 

#soma de quantos mulheres tem
soma_qnt_F = sum(lista_F)
#print(soma_qnt_M)

#media idade dos homens
soma_das_idades_F = sum(lista_id_f)
media_F = soma_das_idades_F / soma_qnt_F
media_F_round = round(media_F, 2)
print("Existem", soma_qnt_F, "mulheres e a media de idade e", media_F_round, "anos")

