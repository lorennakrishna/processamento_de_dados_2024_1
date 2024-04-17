'''se o resto do numero for igual a 0 para numero diferentes de 1 e numero entao o numero nao e primo, 
pelo contrario é primo'''


numero = int(input("Digite um numero: "))
k=1  

while (k < 10):
    
    divisao = numero/k 
    resto = numero%k 
    
    if (divisao == 1 or divisao == numero):
        #print(numero, k, divisao)
        
        k = k + 1
    
    elif (divisao != 1 or divisao != numero):
    
        if (resto == 0):
        
            print('nao é primo')
            
            k = k+1
            break;
            
        elif (resto != 0):
        
            print('é primo')
            
            k = k + 1 
            break;
        
        