#_______________________________________________EXERCÍCIOS DE LISTAS E TUPLAS____________________________________________________

# lista = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi', 'morango', 'kiwi', 'melancia', 'pera', 'pêssego']

# item = input('Digite o item que você quer verificar: ')

# if item in lista:
#     print(f'O item "{item}" está presente na despensa.')
# else:
#     print(f'O item "{item}" precisa ser comprado.')

#===============================================================================

# notas = input('Notas: ').split()

# notas.sort()

# print(f'Notas ordenadas: {notas}')

#===============================================================================

# voluntarios = []
# nome = input('Digite o nome do voluntário: ')

# while nome != 'sair':
#     voluntarios.append(nome)
#     nome = input('Digite o nome do voluntário: ')

# print(f'Voluntários registrados: {voluntarios}')

#===============================================================================

# estoque1 = tuple(input('Produtos do estoque 1: ').split())
# estoque2 = tuple(input('Produtos do estoque 2: ').split())

# estoque_combinado = estoque1 + estoque2

# print(f'Estoque combinado: \n{estoque_combinado}')

#===============================================================================

# lista = ['Ana', 'Pedro', 'Carlos']

# print(f'Lista atual de convidados: {lista}')

# novo_convidado = input('Digite o nome do novo convidado: ')
# posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))

# lista.insert(posicao - 1, novo_convidado)

# print(f'Lista atualizada de convidados: {lista}')

#===============================================================================

# eventos_registrados = ['Encerramento','Palestra 3', 'Palestra 2', 'Abertura']

# eventos_registrados.reverse()

# print(f'Ordem corrigida: {eventos_registrados}')

#===============================================================================

# lista = ['Ana', 'Carlos', 'Pedro']
# print(f'Lista original: {lista}')

# incorreto = input('Digite o nome incorreto: ')
 
# if incorreto in lista:
#     correto = input('Digite o nome correto: ')
#     posicao = lista.index(incorreto)
#     lista.remove(incorreto)
#     lista.insert(posicao, correto)
#     print(f'O nome {incorreto} foi substituído por {correto}.')
#     print(f'Lista atualizada: {lista}')
# else:
#     print(f'Nome não encontrado')

#===============================================================================

# pedidos = list(input('Pedidos feitos (separados por vírgula): ').split(', '))

# pedidos.pop()

# print(f'Pedidos finais: {pedidos}')

#===============================================================================

# notas = [float(nota) for nota in input('Digite as notas dos alunos (separadas por vírgula): ').split(', ')]
# media = sum(notas) / len(notas)
# print(f'Média final da turma: {media:.2f}')

#===============================================================================
# dados = input('Digite os dados do aluno no formato Nome, idade, nota separados por vírgula: ').split(', ')

# for i in range(0, len(dados), 3):
#     nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
#     print(f'Aluno: {nome}')
#     print(f'Idade: {idade}')
#     print(f'Nota: {nota}\n')
