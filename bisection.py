from sympy import N, symbols, cos, sin, log, ln
from sympy.parsing import *
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
from time import sleep
x = symbols('x')
it_total = 0

def strToEquation(str, x_value):
    transformations = (standard_transformations + (implicit_multiplication_application,))
    equation = N(parse_expr(str, transformations=transformations).subs(x, x_value))
    return equation


while True:
    try:
        function = str(input('Insira a função desejada: '))

        def f(x):
            image = strToEquation(function, x)
            return image

        while True:
            a = float(input('Insira o primeiro limite: '))
            b = float(input('Insira o segundo limite: '))
            if f(a)*f(b)>=0:
                print('Uma das imagens deve ser positiva, e a outra, negativa!')
            else:
                break

        it_max = int(input('Insira o número máximo de iterações: '))
        erro_max = float(input('Insira o erro máximo: '))
    except Exception as error:
        print('Um erro ocorreu:', error)


    if f(a)<0:
        negative_lim = a
        positive_lim = b
    else:
        negative_lim = b
        positive_lim = a

    passo = int(it_max/10)
    print(passo)
    show_in = []
    for it in range(0, it_max, passo):
        show_in.append(it)
    show_in.append(it_max)
    print(show_in)
    while it_total <= it_max:
        m = (negative_lim+positive_lim)/2
        erro = (positive_lim-negative_lim)/2
        if erro_max < erro:
            if f(m)<0:
                negative_lim = m
                if it_total in show_in:
                    print('\nO f(m) é {0}, portanto o novo limite negativo é {0}'.format(f(m)))
                    print('O limite positivo permanece sendo {0}'.format(positive_lim))
                    print('Iterações feitas:', it_total)
            elif f(m)>0:
                positive_lim = m
                if it_total in show_in:
                    print('\nO f(m) é {0}, portanto o novo limite positivo é {0}'.format(f(m)))
                    print('O limite negativo permanece sendo {0}'.format(negative_lim))
                    print('Iterações feitas:', it_total)
            else:
                root = m
                print('A raiz é {0}'.format(root))
                break
        
        root = m
        it_total += 1
    print('\nProcesso finalizado!')
    print('Raiz encontrada: ', root)
    print('Iterações feitas: ', it_total)
    print('Erro: ', erro)
else:
    print('Saindo...')
    sleep(3)
