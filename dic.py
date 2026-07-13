#_______________________________________________EXERCÍCIOS DE CONJUNTOS E DICIONÁRIOS____________________________________________________

# convidados = set()

# while True:
#     nome = input('Digite o nome do convidado: ')
#     if nome == 'sair':
#         break
#     convidados.add(nome)

# print(f'Convidados confirmados: {', '.join(convidados)}')

#===============================================================================
# txt1 = set(input('Texto 1: ').lower().split())

# txt2 = set(input('Texto 2: ').lower().split())

# comum = txt1 & txt2

# print(f'Caracteres em comum: {comum}')

#===============================================================================

# lista1 = set(input('Lista de Laura: ').lower().split(', '))

# lista2 = set(input('Lista de Ana: ').lower().split(', '))

# comum = lista1.intersection(lista2)

# nova_lista1 = lista1 - comum
# nova_lista2 = lista2 - comum

# print(f'Itens em ambas as listas: {', '.join(comum)}')
# print(f'Itens apenas em Laura: {', '.join(nova_lista1)}')
# print(f'Itens apenas em Ana: {', '.join(nova_lista2)}')

#==============================================================================

# permissoes_principais = set(p.strip() for p in input('Digite as permissões principais: ').lower().split(','))

# permissoes_solicitadas = set(p.strip() for p in input('Digite as permissões sollicitadas: ').lower().split(','))

# subconjunto = permissoes_solicitadas.issubset(permissoes_principais)

# if subconjunto:
#     print('As permissões solicitadas fazem parte das permissões principais.')
# else:
#     print('As permissões solicitadas não fazem parte das permissões principais.')

#===============================================================================

# equipeA = {'planejar reunião', 'revisar documento', 'testar sistema'}

# equipeB = {'testar sistema', 'implementar funcionalidades', 'corrigir bugs'}

# tarefas_finais = equipeA.union(equipeB)

# print(f'Equipe A: {equipeA}')

# print(f'Equipe B: {equipeB}')

# print(f'Tarefas combinadas: {tarefas_finais}')

# pergunta = input('Deseja remover alguma tarefa: ').lower()

# if pergunta in tarefas_finais:
#     tarefas_finais.remove(pergunta)

# print(f'Tarefas finais: {tarefas_finais}')

#======================================================================================


# produto = {}

# for i in range(3):
#     nome = input('Digite o nome do produto: ')
#     quantidade = int(input('Digite a quantidade: '))
#     produto[nome] = quantidade

# print(f'Dicionário de produtos: {produto}')

#=======================================================

# estoque = {'caderno universitário': 50, 'caneta azul': 120, 'borracha branca':30}

# produto = input('Nome do produto a ser atualizado: ')


# if produto in estoque:
#     quantidade = int(input('Digite a nova quantidade: '))
#     estoque[produto] = quantidade
#     print(estoque)
# else:
#     print(f'O produto {produto} não está no estoque.')

#=======================================================================================

# participantes = {'Mariana':25, 'Carlos':32, 'Beatriz':28, 'Rafael':35}

# print(f'Nome dos participantes: {(', '.join(participantes.keys()))}')

# print(f'Idades dos participantes: {(', '.join(str(idade) for idade in participantes.values()))}')

# print('Participantes e suas idades: ')

# for nome, idade in participantes.items():
#     print(f'-{nome}: {idade}')

#=========================================================================================================

# participantes = {'Workshop 1': {'Alice', 'Bruno', 'Carla', 'Diego'}, 'Workshop 2': {'Fernanda', 'Gustavo', 'Helena'}}

# print(f'Participantes: {', '.join(str(nome) for nome in participantes.values())}')

# remover = input('Nome do participante a ser removido: ')

# for evento, nomes in participantes.items():
#     nomes.discard(remover)

# print('Lista de participantes atualizada: ')

# for evento, nomes in participantes.items():
#     print(f'-{evento}: {nomes}')

#===========================================================================================================

# vendas = {
#     'Eletronicos': [
#         {'produto': 'Smartphone', 'Quantidade': 5, 'Valor': 2000},
#         {'produto': 'Table', 'Quantidade': 3, 'Valor': 1500}
#     ],

#     'Eletrodomésticos': [
#         {'produto': 'Geladeira', 'Quantidade': 2, 'Valor': 3000},
#         {'produto': 'Micro-ondas', 'Quantidade': 4, 'Valor': 800}
#     ],

#     'Livros': [
#         {'produto': 'Livro A', 'Quantidade': 10, 'Valor': 50},
#         {'produto': 'Livro B', 'Quantidade': 53, 'Valor': 100}
#     ]
# }

# print('Total de vendas por categoria: ')

# for categoria, itens in vendas.items():
#     total = 0
#     for item in itens:
#         total += item['Quantidade'] * item['Valor']
#     print(f'-{categoria}: R${total:.2f}')
