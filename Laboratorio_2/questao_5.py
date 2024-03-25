'''Crie um programa que calcule o imposto de renda de pessoa física (IRPF) dada a tabela de incidência mensal
do imposto (Tabela 3) e o valor do salário que o usuário fornecerá ao programa.

Base de cálculo (R$) Alíquota (%) Parcela a deduzir do IRPF (R$)
Até 1.903,98 - -
De 1.903,99 até 2.826,65 7,5% 142,80
De 2.826,66 até 3.751,05 15% 354,80
De 3.751,06 até 4.664,68 22,5% 636,13
Acima de 4.664,68 27,5% 869,36'''


salario = float(input('Digite seu salario: '))


    
if (salario <= 1903.98):
    print('Isento de imposto de renda')

elif (salario > 1903.98 and salario <= 2826.65):
    valor_imposto = (salario*0.075)-142.80
    print('Você paga 7,5% de imposto, com desconto da parcela a deduzir fica: R$', valor_imposto)

elif (salario > 2826.65 and salario <= 3751.05):
    valor_imposto = (salario*0.15)-345.80
    print('Você paga 15% de imposto, com desconto da parcela a deduzir fica: R$', valor_imposto)

elif (salario > 4664.68):
    #Acima de 4.664,68 27,5% 869,36'''
    valor_imposto = (salario*0.275)-869.39
    print('Você paga 27,5% de imposto, com desconto da parcela a deduzir fica: R$', valor_imposto)
    
    
    
