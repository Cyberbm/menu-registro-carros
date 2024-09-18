import re

email_de_registro = None
senha_de_registro = None

def pagina_de_registro():

        global email_de_registro, senha_de_registro

        def registro_email():

            lista_emails_registrados = []
            padrao_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{3,}$')

            while True:

                print('=' * 30)
                email_de_registro = input('Por favor, registre seu email: ').strip()

                if not padrao_email.match(email_de_registro):
                    print('Email inválido, tente novamente.')
                    continue

                if email_de_registro in lista_emails_registrados:
                    print('Esse email já está registrado. Por favor, tente outro.')
                    continue

                opcao = input(f'Este é o email que deseja registrar ? {email_de_registro} [S/N]: ').strip().upper()[0]

                if opcao == 'S':
                    print('Email registrado.')
                    lista_emails_registrados.append(email_de_registro)
                    break
                elif opcao == 'N':
                    print('Tente novamente.')
                    continue
                else:
                    print('Opção inválida, tente novamente.')
                    continue
            return email_de_registro

        email_de_registro = registro_email()


        def registro_senha():

            padrao_senha = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
            lista_senhas_registradas = []

            while True:

                senha_de_registro = input('Registre sua senha: ')
                if padrao_senha.match(senha_de_registro):
                    senha_confirmacao = input('Confirme sua senha: ')
                    if senha_de_registro == senha_confirmacao:
                        print('Senha registrada.')
                        lista_senhas_registradas.append(senha_de_registro)
                        break
                    else:
                        print('As senhas são incompativeis, tente novamente.')
                        print('=' * 30)
                        continue

                else:
                    print('Senha inválida, as senhas devem ter pelo menos 8 caracteres.\nIncluindo alfanumérico, maiúsculo, minúsculo e caracteres especiais.')
                    print('=' * 30)
            return senha_de_registro

        senha_de_registro = registro_senha()


def pagina_login():

    global email_de_registro, senha_de_registro

    while True:

        login_opcao = input(f'''{'='*30}
        
{' ' * 10}Bem vindo!
{'=' * 30}

Escolha entre uma das opções:

[ 1 ] Registrar conta
[ 2 ] Login

Qual das opções deseja escolher?: ''')

        if login_opcao == '1':
            pagina_de_registro()
        elif login_opcao == '2':
            login_email = input('Por favor, digite seu email associado a conta: ').strip()
            login_senha = input('Digite sua senha: ')
            if login_email == email_de_registro and login_senha == senha_de_registro:
                print('Seja bem vindo!')
                break
            else:
                print('Senha ou email incorretos, tente novamente.')
        else:
            print('Responda com uma das opções.')

pagina_login()