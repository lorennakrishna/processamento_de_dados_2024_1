'''

Fa ̧ca um programa que leia uma frase e imprima todas as palavras que que apare ̧cam mais de uma  ́unica vez
na frase.

'''


frase = input("Digite uma frase: ")
result = frase.split()
result_dois = []
#print(result[1])

'''
if (result[0] == result [1]):
    
    print('Igual')
    
elif (result[0] != result [1]):
    
    print('Diferente')'''
    
    
aux = 0
aux_dois = 1

#count = len(frase) #conta letras
count_dois =  len(result)

while(aux_dois < count_dois):
    
    if (result[aux] == result[aux_dois]): 
            #colocar na lista
            print(result[aux_dois])
                
            aux_dois = aux_dois + 1 
             
            
    elif (result[aux] != result [aux_dois]):
             
        if (aux_dois == count_dois - 1 ):
            
            #print('teste')
            #break;
            
            aux = aux + 1
            aux_dois = aux + 1
            
        elif (aux_dois != count_dois - 1 ):
        
            #aux = aux + 1
             aux_dois = aux_dois + 1 
             #print(result[aux_dois])
    

    '''elif (aux_dois == count_dois):
        
         aux = aux + 1
         aux_dois = 2
         #print(result[aux_dois])'''
         
#print(count_dois)
            # aux =  aux + 1 