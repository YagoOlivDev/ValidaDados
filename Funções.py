def leiaint(into):
    while True:
        try:
            n = int(input(into))
        except (ValueError, TypeError):
            print('ERROR! Por favor digite um número inteiro valido!')
            continue
        else:
            return n


def linha(tam = 40):
    return '\033[1;38m=' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('\033[1;38MMenu Principal'.center(47))
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print('\033[1;38m-=-' * 10)
    opcao = leiaint('Sua opção: ')
    return opcao


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Arquivo não encontrado!')
    else:
        print('')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o Arquivo!')
    else:
        cabecalho('Pessoas Cadastradas:')

        print(a.read())



def cadastrar(arq, nome='desconhecido', idade= 0):
    while True:
        try:

                a = open(arq, 'at')

        except:
            print('Houve um erro na abertura do arquivo')
        else:
            try:
                a.writelines(f'{nome:<27}Idade {idade} anos\n')
            except:
                print('\033[1;33mHouve um erro na hora de escrever os dados!\033[m')
            else:
                print(f'\033[1;32mNovo registro de {nome} ADICIONADO!\033[m')
                a.close()
        nova = str(input('Deseja cadastrar uma nova pessoa? [S/N] ').upper())
        if nova == 'S':
            break
        elif nova == 'N':
            cabecalho('Até a proxima!')
            exit()
