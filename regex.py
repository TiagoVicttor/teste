
# _______________________________________________________________________EXERCÍCIOS DE STRING E REGEX____________________________________________________

# produto = input('Digite o nome do produto: ')
# produto_padronizado = produto.strip().lower()

# print(f'{produto_padronizado}')

#=================================================================

# nome = input('Digite o nome do cliente: ')
# cidade = input('Digite a cidade do cliente: ')

# print(f'Olá, {nome}! Seja bem-vindo ao sistema da cidade de {cidade}.')

#==========================================================================

# palavra = input('Digite uma palavra: ')

# print(f'Primeiras: {palavra[:3]}')
# print(f'Ultimas: {palavra[-3:]}')

#============================================================

# texto = input('Digite um texto: ')

# if texto.startswith("https://") and texto.endswith(".com"):
#     print('O texto é um link válido.')
# else:
#     print('O texto não é um link válido.')

#============================================================

# import re

# texto = input('Digite a descrição da receita: ')
# numero = re.findall(r'\d+', texto)[0]

# print(f'O número da receita é: {numero}')

#============================================================

# import re

# texto = input('Digite o texto a ser revisado: ')
# palavra = input('Qual palavra deseja substituir? ')
# palavra_nova = input('Qual a nova palavra? ')

# nova_frase = re.sub(rf'\b{palavra}\b', palavra_nova, texto)

# print(nova_frase)

#============================================================

# import re

# nome = input('Digite o nome do cliente: ')

# if re.fullmatch(r'[A-Z][a-z]*', nome):
#     print('Nome válido.')
# else:
#     print('Nome inválido.')

#=============================================================

# import re

# cpf = input('Digite o CPF no formato XXX.XXX.XXX-XX: ')

# if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
#     print('CPF válido.')
# else:
#     print('CPF inválido.')

#=============================================================

# import re

# titulo = input('Digite o título do livro: ')
# letra = input('Digite a letra inicial para a pesquisa: ')

# letra_inicial = re.findall(rf'\b{letra}[a-zà-ÿ]*', titulo, re.IGNORECASE)

# print(letra_inicial)

#=============================================================

# import re

# dados = input('Digite o nome completo e o ano de nascimento do paciente: ')
# padrao = r'(\w+) (\w+) - (\d{4})'

# resultado = re.search(padrao, dados)

# if resultado:
#     nome = resultado.group(1)
#     sobrenome = resultado.group(2)
#     nascimento = resultado.group(3)

#     print(f'Primeiro nome: {nome}')
#     print(f'Sobrenome: {sobrenome}')
#     print(f'Ano de nascimento: {nascimento}')

# else:
#     print('Formato inválido.')