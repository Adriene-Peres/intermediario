import json

#CRIANDO ARQUIVO JSON:
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('14_exemplo_json.json', 'w', encoding='utf8') as arquivo:
    # json.dump(pessoa, arquivo, indent=2)

    # caso queira deixar o texto com a mesma formatação (acetos, etc.): 
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) 

# -----------------------------------------------------------------------------------------
# IMPORANDO DADOS DE UM ARQUIVO JSON:
with open('14_exemplo_json.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    # print(pessoa['nome'])