from time import sleep

cores = {
    'Azul':'\033[1;94m',
    'Vermelho':'\033[1;91m',
    'Branco':'\033[1;97m',
    'Verde':'\033[1;32m',
    'Roxo':'\033[1;90m',
    'Reset':'\033[0m'
}

catalogo_carros = {}

def menu_principal():

    while True:

        print(f'''{cores['Branco']}{'===' * 17}
{' ' * 15}Bem vindo ao menu!
{' ' * 2} Aperte os comandos entre [ ] para se guiar.
{'===' * 17}
Registrar um carro para venda [ 1 ]
Pesquisar por um carro [ 2 ] 
Sair [ 3 ]
{cores['Branco']}{'===' * 17}''')
        opcao = input(f'Digite uma das opções: {cores['Reset']}').strip()


        if opcao == '1':
                registrar_marca = input('Qual a marca do carro ?: ').strip().capitalize()

                registrar_carro = input(f'Qual o nome do carro da marca {registrar_marca}?: ').strip().title()

                try:
                    registrar_ano = int(input(f'Qual o ano do carro ?: '))
                except ValueError:
                    print('Digite um ano válido.')
                    continue

                try:
                    registrar_valor = int(input(f'Qual o valor que deseja por no carro {registrar_carro} da marca {registrar_marca} ?: '))
                except ValueError:
                    print('Digite um valor válido.')
                    continue

                if registrar_marca not in catalogo_carros:
                    catalogo_carros[registrar_marca] = {}

                if registrar_ano not in catalogo_carros[registrar_marca]:
                    catalogo_carros[registrar_marca][registrar_ano] = {}

                catalogo_carros[registrar_marca][registrar_ano][registrar_carro] = registrar_valor

                print(f'{cores['Branco']}O carro {registrar_carro} da marca {registrar_marca} foi registrado com o valor{cores['Reset']} {cores['Verde']}R$:{registrar_valor}{cores['Reset']}')

                opcao_2 = input('Deseja registrar mais um carro ?[ S / N ] ').upper()[0].strip()

                if opcao_2 == 'S':
                    continue
                elif opcao_2 == 'N':
                    menu_principal()
                else:
                    print('Por favor, digite um comando válido.')

                return catalogo_carros

        elif opcao == '2':
                print('''Escolha entre:
[ 1 ] Pesquisar por marca
[ 2 ] Voltar ao menu principal''')
                pesquisa = input('Escolha uma das opções: ').strip()
                if pesquisa == '1':
                    marca_pesquisa = input('Digite a marca que deseja pesquisar: ').title().strip()
                    if marca_pesquisa in catalogo_carros:
                        print(f'Carros disponíveis da marca {marca_pesquisa}')
                        for ano, carros in catalogo_carros[marca_pesquisa].items():
                            for carro, valor in carros.items():
                                print(f'{carro} - Ano: {ano}, Valor: R${valor}')
                    else:
                        print(f'Não possuímos carros da marca {marca_pesquisa} registrados.')

                elif pesquisa == '2':
                    menu_principal()

                else:
                    print('Digite um comando válido')

        elif opcao == '3':
                print('Finalizando...')
                sleep(2)
                print('Fim do programa.')
                break

menu_principal()




