# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


def menu():
    print('Comandos: listar, desfazer e refazer')
    print('Digite uma tarefa ou comado: ', end = " ")

def adicionar_itens(item, lista_tarefas=None): 
    if lista_tarefas is None:
        lista_tarefas = []
    lista_tarefas.append(item)

def listar_itens(lista):
    print()
    print('TAREFAS: ')
    for item in lista:
        print(f"\t{item}")
    print()

def desfazer_item(lista_tarefas, lista_desfeito):
    if not lista_tarefas:
        print('\nNenhuma tarefa para desfazer!\n')
        return

    item_desfeito = lista_tarefas.pop()
    lista_desfeito.append(item_desfeito)
    listar_itens(lista_tarefas)
    return lista_desfeito

def refazer_item(item_desfeito, lista_tarefas):
    item = item_desfeito.pop()
    lista_tarefas.append(*item)
    listar_itens(lista_tarefas)


x = True 
tarefas = []
lista_desfeitos = []
while x == True:
    menu()
    item = input()
    if item == 'listar':
        listar_itens(tarefas)
        continue
    elif item == 'desfazer':
        itens_desfeitos = [desfazer_item(tarefas, lista_desfeitos)]
        continue
    elif item == 'refazer':
        if not lista_desfeitos:
            print('\nNenhuma tarefa para refazer!\n')
        else:
            refazer_item(itens_desfeitos, tarefas)
        continue
    elif item == 'sair':
        x = False
    else:
        adicionar_itens(item,tarefas)
        listar_itens(tarefas)
        continue