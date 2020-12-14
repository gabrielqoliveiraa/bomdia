

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        return f'VOTO OBRIGATÓRIO'
    else:
        return f'VOTO OPCIONAL'



idadeUsuario = int(input('Qual seu ano de nascimento ?: '))
print(voto(idadeUsuario))