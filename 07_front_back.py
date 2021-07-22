"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    a = str(a)
    b = str(b)

    tam_a = len(a)
    tam_b = len(b)

    med_a = int(tam_a/2)
    med_b = int(tam_b/2)

    if (tam_a % 2 == 0 and tam_b % 2 == 0):
        return f"{a[:med_a] + b[:med_b] + a[med_a:] + b[med_b:]}"
    elif(tam_a % 2 != 0 and tam_b % 2 != 0):
        return f"{a[:med_a+1] + b[:med_b+1] + a[med_a+1:] + b[med_b+1:]}"
    elif(tam_a % 2 == 0 and tam_b % 2 != 0):
        return f"{a[:med_a] + b[:med_b+1] + a[med_a:] + b[med_b+1:]}"
    elif(tam_a % 2 != 0 and tam_b % 2 == 0):
        return f"{a[:med_a+1] + b[:med_b] + a[med_a+1:] + b[med_b:]}"
    return ''

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
    test(front_back, ('', 'Banana'), 'Banana')
    test(front_back, ('maça', ''), 'maça')
    test(front_back, ('', ''), '')
    test(front_back, (1, 2), '12')
    test(front_back, (12, 24), '1224')
    test(front_back, (123, 24), '12234')
    test(front_back, (12, 369), '13629')
    test(front_back, ('12'+'ab', 369), '1236ab9')
