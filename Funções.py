import re
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



def cadastrar(arq, nome='desconhecido', cpf = 0):
    while True:
        try:

                a = open(arq, 'at')

        except:
            print('Houve um erro na abertura do arquivo')
        else:
            try:
                a.writelines(f'{nome:<24}CPF: {cpf} \n')
            except:
                print('\033[1;33mHouve um erro na hora de escrever os dados!\033[m')
            else:
                print(f'\033[1;32mNovo registro de {nome} ADICIONADO!\033[m')
                a.close()
                break
        #nova = str(input('Deseja cadastrar uma nova pessoa? [S/N] ').upper())
        #if nova == 'S':
            #break
        #elif nova == 'N':
            #cabecalho('Até a proxima!')
            #exit()


def valid(cpf):
    regressivo1 = 10
    #c_pf = re.sub(r'[^0-11]', '', cpf)

    cpf_digitado = re.sub(r'[^0-9]', '', cpf)
    nove_digitos = cpf_digitado[:9]
    #nove_digitos = cpf[:9]

    resultado1 = 0
    for dig in nove_digitos:
        resultado1 += int(dig) * regressivo1
        regressivo1 -= 1

    dig1 = (resultado1 * 10) % 11
    if dig1 <= 9:
        dig1 = dig1
    else:
        dig1 = 0
    # print(nove_digitos,dig)

    digitos2 = nove_digitos + str(dig1)
    regressivo2 = 11
    resultado2 = 0

    for dig2 in digitos2:
        resultado2 += int(dig2) * regressivo2
        regressivo2 -= 1
    dig2 = (resultado2 * 10) % 11
    if dig2 <= 9:
        dig2 = dig2
    else:
        dig2 = 0
    comp = f'{nove_digitos}{dig1}{dig2}'
    if cpf_digitado == comp:
        return cpf_digitado
    else:
        print('\033[1;31mERROR! CPF inválido!')
