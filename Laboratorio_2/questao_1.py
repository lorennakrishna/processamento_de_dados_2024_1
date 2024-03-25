#Laboratório 2 
'''Crie um programa que determine em que quandrante um determinado ângulo está dentro do círculo trigono-
métrico. Para ângulos múltiplos de 90 graus, você deve determinar o quadrante cujo menor ângulo pertencente

a ele seja mais próximo do 0. '''

entrada = int(input('Digite um ângulo: '))

#def primeiros_quadrantes ():
    
    
if (entrada == 0 and  entrada <= 89):
    { print('Quadrante 1') }

elif (entrada == 91 and entrada <= 179): 
    { print('Quadrante 2') }

elif (entrada == 181 and entrada <= 269): 
    { print('Quadrante 3') }

elif (entrada == 271 and entrada <= 359): 
    { print('Quadrante 4') } 

elif (entrada == 90): 
    { print(entrada, 'esta no primeiro quadrande. \t menor angulo do quadrante é: ', entrada-90) } 

elif (entrada == 180): 
    { print(entrada, 'esta no segundo quadrande. \t menor angulo do quadrante é: ', entrada-90+1) }   
    
elif (entrada == 270): 
    { print(entrada, 'esta no terceiro quadrande. \t menor angulo do quadrante é: ', entrada-90+1) }
    
elif (entrada == 360): 
    { print(entrada, 'esta no quarto quadrande. \t menor angulo do quadrante é: ', entrada-90+1) }
    
'''
menor angulo do quadrante 1
menor angulo do quadrante 2
menor angulo do quadrante 3
menor angulo do quadrante 4'''   
   
   
   
    
'''  elif (entrada == 361 or entrada >= 361):
    
    entrada2 = entrada - 360
    
    if (entrada2 == 0 or  entrada2 <= 90):
        { print('Quadrante 1') }

    elif (entrada2 == 91 or entrada2 <= 180): 
        { print('Quadrante 2') }
    
    elif (entrada2 == 181 or entrada2 <= 270): 
        { print('Quadrante 3') }
    
    elif (entrada2 == 271 or entrada2 <= 360): 
        { print('Quadrante 4') }'''

#def outros_quadrantes ():

   # if (entrada > 360):
        
       # { entrada == entrada - 360 }
    
 #   elif (entrada > 360):
  #      print('chegou')
 
#primeiros_quadrantes()
#quadrantea_maior_que()
#outros_quadrantes ()



