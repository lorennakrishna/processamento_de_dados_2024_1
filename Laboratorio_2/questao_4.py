'''4. Crie um programa que calcule, de acordo com a tabela mensal de contribuição do INSS (Tabelas 1 e 2),
o quanto um trabalhador tem que recolher mensalmente para a previdência pública. Você precisa obter do
usuário o valor do salário de contribuição e a informação sobre qual a opção de contribuição. Considere apenas
duas possibilidades de contribuição: o contribuinte avulso e o trabalhador comum.

Salário de contribuição Alíquota
Até R$ 1.751,81 8%
De R$ 1.751,82 a R$ 2.919,72 9%
De R$ 2.919,73 até R$ 5.839,45 11%'''


trabalhador = int(input('Você é:\n\n 1- trabalhador comum \t 2- contribuinte avulso?: '))

#salario = float(input('Digite seu salario: '))

if (trabalhador == 1):
    
    salario = float(input('Digite seu salario: '))
    
    if (salario <= 1751.81):
        valor_imposto = salario*0.08
        print('Você paga 8% de imposto, que é: R$', valor_imposto)
    
    elif (salario > 1751.81 and salario <= 2919.72):
        valor_imposto = salario*0.09
        print('Você paga 9% de imposto, que é: R$', valor_imposto)
    
    elif (salario > 2919.72):
        valor_imposto = salario*0.11
        print('Você paga 11% de imposto, que é: R$', valor_imposto)
        
elif (trabalhador == 2):
    
    salario = float(input('Digite seu salario: '))
    #R$ 998,00 até R$ 5.839,45
    if (salario >= 998.00 and salario <= 5839.45):
        valor_imposto = salario*0.20
        print('Você paga 20% de imposto, que e: R$', valor_imposto)
    
    elif (salario < 998.00):
        valor_imposto = 998*0.20
        print('Você paga 20% de imposto, que e: R$', valor_imposto)
    
    elif (salario > 5839.45):
        valor_imposto = 5839.45*0.20
        print('Você paga 20% de imposto, que e: R$', valor_imposto)

else:
    
    print('Opcao invalida')


    
    