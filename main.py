# Cinema por idade

nome = input('Informe o seu nome: \n')
idade = int(input('Informe a sua idade: \n'))

# Lista de filmes e suas salas
while True:

    print('LISTA DE FILMES \n')
    print('Sala 1 - A Volta dos mortos vivos 16+. ')
    print('Sala 2 - Matrix 16+')
    print('Sala 3 - John Wick 18+')
    print('Sala 4 - Homem de Ferro 14+')
    print('Sala 5 - Super Mario Bros 12+\n')

    sala = int(input('Informe a sala desejada: '))

    # Receber a sala escolida

    match sala:
        case 1:
            if idade >= 16:
                print(f'Filme escolhido por {nome}: A Volta dos mortos vivos.')
                break
            else:
                print('Faixa etária insulficiente, escolha outro filme: \n')
                continue
        case 2:
            if idade >= 16:
                print(f'Filme escolhido por {nome}: Matrix')
                break
            else:
                print('Faixa etária insulficiente, escolha outro filme: \n')
                continue
        case 3:
            if idade >= 18:
                print(f'Filme escolhido por {nome}: John Wick')
                break
            else:
                print('Faixa etária insulficiente, escolha outro filme: \n')
                continue
        case 4:
            if idade >= 14:
                print(f'Filme escolhido por {nome}: Homem de Ferro')
                break
            else:
                print('Faixa etária insulficiente, escolha outro filme: \n')
                continue
        case 5:
            if idade >= 12:
                print(f'Filme escolhido por {nome}: Super Mario Bros')
                break
            else:
                print('Faixa etária insulficiente, escolha outro filme: \n')
                continue
        case _:
            print('Opção inválida')
            break
