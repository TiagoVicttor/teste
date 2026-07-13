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

equipeA = {'planejar reunião', 'revisar documento', 'testar sistema'}

equipeB = {'testar sistema', 'implementar funcionalidades', 'corrigir bugs'}

tarefas_finais = equipeA.union(equipeB)

print(f'Equipe A: {equipeA}')

print(f'Equipe B: {equipeB}')

print(f'Tarefas combinadas: {tarefas_finais}')

pergunta = input('Deseja remover alguma tarefa: ').lower()

if pergunta in tarefas_finais:
    tarefas_finais.remove(pergunta)

print(f'Tarefas finais: {tarefas_finais}')