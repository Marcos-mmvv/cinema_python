# Recebe o nome

nome = input('Informe o seu nome: \n')

# Lista de filmes e suas salas

print('LISTA DE FILMES \n')
print('Sala 1 - A Volta dos Que Não Foram.')
print('Sala 2 - A Roda Quadrada.')
print('Sala 3 - Poeira em Alto Mar.')
print('Sala 4 - As Tranças do Rei Careca.')
print('Sala 5 - A Vingança do Peixe Frito \n')

# Receber a sala escolida

sala = int(input('Informe a sala desejada: '))

match sala:
    case 1:
        print(f'Filme escolhido por {nome}: A Volta dos Que não foram.')
    case 2: 
        print(f'Filme escolhido por {nome}: A Roda Quadrada')
    case 3:
        print(f'Filme escolhido por {nome}: Poeira em Alto Mar')
    case 4:
        print(f'Filme escolhido por {nome}: As Tranças do Rei Careca')
    case 5:
        print(f'Filme escolhido por {nome}: A Vingança do Peixe Frito')
    case _:
        print('Sala inexistente')

