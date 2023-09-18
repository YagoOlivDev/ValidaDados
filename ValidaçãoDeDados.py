from Funções import *

Arquivos= 'CadastrandoeinformandoDados.txt'

if not arquivoexiste(Arquivos):
    CriarArquivo(Arquivos)

while True:
    resposta = menu(['\033[1;38mVer Pessoas.', 'Cadastrar Pessoas.', 'Sair.'])
    if resposta == 1:
        print('Opção 1')
        LerArquivo(Arquivos)
        print('=' * 40)
        volt = str(input('Deseja voltar ao menu anterior? [S/N] ')).upper()

        if volt == 'S':
            continue

        else:
            exit('\033[1;38mProgama Encerrado!')

    elif resposta == 2:
        while True:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome:'))
            c_pf = valid(input('Seu CPF: '))

            try:
                with open('CadastrandoeinformandoDados.txt', 'r') as arquivo:
                    texto = arquivo.read()

                    if c_pf in texto:
                        print('\033[1;31mERROR! Pessoa ja cadastrada\033[m')

                    else:
                        cadastrar(Arquivos, nome, c_pf)
                        cabecalho('[C] para cadastrar novo usuário \n[V] para voltar ao menu principal.')
                        nova = input('\033[1;38mResposta: ').upper()

                        if nova == 'C':
                            continue

                        elif nova == 'V':
                            #cabecalho('Até a proxima!')
                            break

            except:
                ...

    elif resposta == 3:
        linha()
        print('\033[1;38mSaindo...')
        print('\033[1;38mPROGAMA ENCERRADO!')
        linha()
        break

    else:
        print('\033[1;31mERROR! Escolha uma opção válida\033[m')


