from time import sleep
nome =str(input('Qual seu nome ?'))
print('='* 45)
print('\033[1;36mBEM-VINDO {} AO SIMULADOR DE EMPRESTIMO\033[m'.format(nome.upper()))
print('='* 45)
casa = float(input('Qual o valor do imovel:'))
salario = float(input('Seu salário:'))
pres = int(input('Quanto anos quer pagar:'))
print('PROCESSANDO...')
sleep(3)
meses = pres * 12
porcentagem = (salario * 30) / 100
parcela = casa / meses

if parcela >= porcentagem:
    print('Emprestimo \033[1;31mNEGADO\033[m, excedeu o limite de 30% do valor do seu salario de R${:.2f}'.format(salario))
else:
    print('Seu emprestimo foi \033[1;32mAPROVADO\033[m,com o valor mensal de R${:.2f} , durante {} anos.'.format(parcela,pres))
