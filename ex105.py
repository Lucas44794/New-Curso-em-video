def notas(*n, sit=False):
    """
    => Função para analuisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar situação
    :return: dicionário com várias informações sobre a situação turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r["media"] >= 7:
            r['situacao'] = 'BOA'
        elif r["media"] >= 5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'RUIM'
    return r

#Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)