
# closure e fuções que retornam funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

saudar_bom_dia = criar_saudacao("Bom dia")
saudar_boa_noite = criar_saudacao('Boa noite')

print(saudar_bom_dia('Adriene'))
print(saudar_boa_noite('Adriene'))

print()

for nome in ['Sergio', 'Maria', 'Joana']:
    print(saudar_bom_dia(nome))