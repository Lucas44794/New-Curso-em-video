def voto(anoNascimento):
    import datetime
    idade = int(datetime.date.today().year) - anoNascimento
    if idade < 16:
        return f'Voto negado por ter {idade}'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Voto Opicional por ter {idade}'
    else:
        return f'Voto Obrigatorio por ter {idade}'

ida = int(input('Ano de nascimento: '))
print(voto(ida))