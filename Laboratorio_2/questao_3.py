'''Crie um programa que leia um número inteiro representando um ano e imprima uma mensagem afirmando se
o ano em questão é bissexto ou não. A ocorrência de anos bissextos (com 366 dias) é periódica e se dá por
uma regra definida no século XVI:
(a) Se um ano é múltiplo de 400, então este é bissexto. Ex: o ano 1600 é bissexto.
(b) Se um ano é múltiplo de 100, então este não é bissexto. Ex: o ano 1800 não é bissexto.
(c) Se um ano é múltiplo de 4, então este é bissexto. Ex: o ano 1984 é bissexto.
(d) Caso o ano não caia em nenhuma das regras anteriores, este não é bissexto. Ex: o ano 2003 não é
bissexto.
(e) É possível que haja colisão entre as três primeiras regras acima descritas. Neste caso, vale a primeira
regra definida.
Dica: Perceba que num ciclo de 400 anos, há sempre 97 anos bissextos.  '''


numero = int(input("Digite um ano: "))

#k = 0 
#verifc = False

#def multiplo_quatrocentos ():

#Multiplo de 400   
k = 0 
verifc = False
  

while ( k <= 11 and verifc == False): 

    #print(k)
    
    if (k <= 11): 
        
        if (numero >= 0 or k <= 10):
           
           # print ('teste valor:', k)
                
            verifc = bool(numero == 400 * k)
            
            if (verifc == True):
                #print(verifc, k)
                print(numero, 'é ano bissexto')
                break;
            
            elif (verifc != True):
                k = k + 1
               # print(k)
                
                if ( k == 12):
                    
                    break;
                    #print(k)
                    
                    #k = 0 
                    
                   # print(k)
                    
                   # break;
                
    #print(k) #aqui conta todos os k tambem, mesmo fora do if
    
if (k == 12):
    k = 0
    
    #print(k) #aqui conta apenas o 12  
    
    while ( k <= 11 and verifc == False): 

    #print(k)
    
        if (k <= 11): 
            
            if (numero >= 0 or k <= 11):
               
               # print ('teste valor:', k)
                    
                verifc = bool(numero == 100 * k)
                
                if (verifc == True):
                    #print(verifc, k)
                    print(numero, 'não é bissexto')
                    break;
                
                elif (verifc != True):
                    k = k + 1
                   # print(k)
                    
                    #if ( k == 12):
                        
                     #   print(k,'1100')

                    if (k == 12):
                        #print(k)
                        k = 0
                        #print(k) printa 0
                        #print(k) #aqui conta apenas o 12  
                        
                        while (k <= 10000): 
                            
                            #print(k)
                            
                            if (numero >= 0 or k <= 10000):
                               
                               # print ('teste valor:', k)
                                    
                                verifc = bool(numero == 4 * k)
                                
                                if (verifc == True):
                                    #print(verifc, k)
                                    print(numero, 'é bissexto')
                                    break;
                                
                                elif (verifc != True):
                                    k = k + 1
                                    #print(k)
                                    
                                    if ( k == 10001):
                                    
                                        print(numero, 'não é bissexto')
                    
    
    
    
    
    
'''
                     while ( k <= 11): 
                        
                        k = 0 
                        
                        if (numero >= 0 or k <= 10):
                           
                           # print ('teste valor:', k)
                                
                            verifc = bool(numero == 100 * k)
                            
                            if (verifc == True):
                                #print(verifc, k)
                                print(numero, 'não é ano bissexto')
                                break;
                            
                            elif (verifc != True):
                                k = k + 1
                                #print('', k)
              
        

#Multiplo de 100   

k = 0
while ( k <= 11): 
    
    if (numero >= 0 or k <= 10):
       
       # print ('teste valor:', k)
            
        verifc = bool(numero == 100 * k)
        
        if (verifc == True):
            #print(verifc, k)
            print(numero, 'não é ano bissexto')
            break;
        
        elif (verifc != True):
            k = k + 1
            #print('', k)
            
k = 0  
while ( k <= 10000): 
    
    if (numero >= 0 or k <= 10):
       
       # print ('teste valor:', k)
            
        verifc = bool(numero == 4 * k)
        
        if (verifc == True):
            #print(verifc, k)
            print(numero, 'é ano bissexto')
            break;
        
        elif (verifc != True):
            k = k + 1
            #print('', k)
            
k = 0  

print(numero, 'não é bissexto')'''