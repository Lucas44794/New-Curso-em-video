aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] > 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] < 7 and aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situacao'] = 'Reprovado'

for k, i in aluno.items():
    print(f' - {k} é igual a {i}')