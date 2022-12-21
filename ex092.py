import datetime
aposentadoria = 36
funcionario = dict()
funcionario['nome'] = str(input('Nome: ')).lstrip().capitalize()
funcionario['ano'] = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - funcionario["ano"]
funcionario['idade'] = idade
ctps = int(input('Numero da Carteira CTPS: '))
if ctps != 0:
    funcionario['ctps'] = ctps
    funcionario['contratacao'] = int(input('Ano da contratação: '))
    tcont = datetime.date.today().year - funcionario["contratacao"]
    funcionario['salario'] = float(input('Valor do salário: '))
    aposentar = aposentadoria - tcont
    anoAposentar = datetime.date.today().year + aposentar
    funcionario['anoiraaposentar'] = anoAposentar
print('-=' * 40)
for r, i in funcionario.items():
    print(f'{r} Tem o valor de {i}')
