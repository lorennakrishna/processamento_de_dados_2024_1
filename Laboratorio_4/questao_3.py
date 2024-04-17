"n! = n · (n – 1)· (n – 2) "



numero_n = int(input("Digite um numero: "))

aux = numero_n-1

#13

#13! = 13 * 12 * 11.....*1 


while (aux != 1):
    
    result = numero_n * (aux) #13 * 12 = 156
    numero_n = result
    aux = aux-1
    print(result)
    
    
    
    
    