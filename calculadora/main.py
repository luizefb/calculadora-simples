print('-=-'*14)
print('Bem vindo(a) ao aplicativo da calculadora!')
print('-=-'*14)

while True:
    print('Escolha a operação matemática para realizar o cálculo: ')
    print('-'*54)
    operacao = int(input('1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n5-Sair\n'))

    if operacao == 1:
        num1 = float(input('Você escolheu ADIÇÃO, qual o primeiro número da soma?\n'))
        num2 = float(input('E o segundo?\n'))
        resultado = num1 + num2
        print(f'O resultado soma dos números {num1} e {num2} é de {resultado}\n')
    elif operacao == 2:
        num1 = float(input('Você escolheu SUBTRAÇÃO, qual o primeiro número?\n'))
        num2 = float(input('E o segundo?\n'))
        resultado = num1 - num2
        print(f'O resultado da subtração dos números {num1} e {num2} é de {resultado}\n')
    elif operacao == 3:
        num1 = float(input('Você escolheu MULTIPLICAÇÃO, qual o primeiro número?\n'))
        num2 = float(input('E o segundo?\n'))
        resultado = num1 * num2
        print(f'O resultado da multiplação dos números {num1} e {num2} é de {resultado}\n')
    elif operacao == 4:
        num1 = float(input('Você escolheu DIVISÃO, qual o primeiro número?\n'))
        num2 = float(input('E o segundo?\n'))
        resultado = num1 / num2
        print(f'O resultado da divisão dos números {num1} e {num2} é de {resultado}\n')
    elif operacao == 5:
        sair = ''
        sair = str(input('VOCÊ TEM CERTEZA? [S/N]')).strip().lower()
        while sair not in 'sn':
            sair = str(input('VOCÊ TEM CERTEZA? [S/N]')).strip().lower()
            if sair == 's':
                print('Volte sempre!')
                exit()
            elif sair == 'n':
                print('=D\n')