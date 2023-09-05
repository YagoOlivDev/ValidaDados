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
            exit('Progama Encerrado!')
    elif resposta == 2:
        while True:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome:'))
            idade = leiaint('Idade:')
            with open('CadastrandoeinformandoDados.txt', 'r') as arquivo:
                texto = arquivo.read()
                if nome in texto:
                    print('\033[1;31mERROR! Pessoa ja cadastrada\033[m')
                else:
                    cadastrar(Arquivos, nome, idade)

    elif resposta == 3:
        print('Saindo...')
        break

    else:
        print('\033[1;31mERROR! Escolha uma opção válida\033[m')


