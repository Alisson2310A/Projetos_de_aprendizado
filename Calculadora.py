def calculadora():
    while True:
        print("Calculadora simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operacao = input("Selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a calculadora python")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção invalida, tente novamente")
            continue

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da operação some é: ", resultado)
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da operação subtração é: ", resultado)
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da operação multiplicação é: ", resultado)
        else:
            if numero_2 == 0:
                print("Divisões por 0 não são possíveis")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da operação divisão é: ", resultado)

calculadora()
