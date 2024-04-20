'''

Fa̧ca um programa que leia uma frase e imprima outra frase que contenha as mesmas palavras da frase de
entrada na ordem inversa. Dica: verifique a utilidade das fun ̧c ̃oes str.split e str.join no help do Python
'''

aux = 0

frase = input("Digite uma frase: ")

result = frase.split()
#print(result)
count = len(result)
aux_dois = (count - count)-1
while (aux < count):
    
    print(result[aux_dois], end=" ")
    #teste_loop = count - 1
   # print(count)
    aux_dois = aux_dois - 1
    aux = aux + 1

