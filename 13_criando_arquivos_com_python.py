import os 

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# ----------------------------------------------------------------------------------------------------
caminho_arquivo = 'C:\\Users\\Adriene\\Documents\\CursoPython\\Aulas\\intermediario\\' 
caminho_arquivo += '13_arquivo.txt' 

# arquivo = open(caminho_arquivo, 'w') 
# # sempre que abrir o arquivo ja fechar para não esquecer no final
# # ao criar um arquivo este é salvo na pasta referente ao caminho

# arquivo.close()


# # context manager: ao usar o comando 'with' ele abre e fecha o arquivo de uma vez 
# # (não há a necessidade de se preocupar em esquecer de fechar o arquivo no final do programa )
# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#
# # ler o arquivo     
# with open(caminho_arquivo, 'r') as arquivo:
#    print(arquivo.read())

#-----------------------------------------------------------------------------------    
# utilizando w+ é possivel ler e escrever em um arquivo 
# lembrar que para isso deve-se lembrar de voltar o cursor para o começo do arquivo usando o comando .seek()
# --> sempre que há um comando de leitura o cursor passa para o final do arquivo, 
# assim deve lembrar de volta-lo para o começo com .seek()
# with open(caminho_arquivo, 'w+') as arquivo: 
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines( # usado pra escrever varias linhas (passando um iteravél)
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     print('Leitura iteira:')
#     arquivo.seek(0,0)
#     print(arquivo.read())
#     print('Lendo (Readline):')
#     arquivo.seek(0,0)
#     print(arquivo.readline().strip()) # .strip() retira os espaços do começo e fim de um string. Aqui foi usado para retirar
#                                       # a quebra de liha do final
#     print(arquivo.readline(), end='') # o comando .readline(), funciona como next, a cada vez que executado uma nova linha é lida
#     print(arquivo.readline().strip()) 
#     print(arquivo.readline().strip()) 

#     print('\nRIDELINES:')
#     arquivo.seek(0,0)
#     for linha in arquivo.readlines(): # readlines -> lista de linhas
#         print(linha.strip())


# print('-'*20)
# # ler o arquivo     
# with open(caminho_arquivo, 'r') as arquivo:
#    print(arquivo.read())

# ---------------------------------------------------------------------------------------------------
# encolding com with open
# usado para queo windows salve o arquivo em UTF-8 (texto fica escrito sem nenhum caractere diferente)
with open(caminho_arquivo, 'w', encoding = 'utf8') as arquivo: 
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines( 
        ('Linha 3\n', 'Linha 4\n')
    )

# ---------------------------------------------------------------------------------------------------
# modulos os
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
    
# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)
# os.rename(caminho_arquivo, '13_arquivo_2.txt')
