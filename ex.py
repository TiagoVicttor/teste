# numero = int(input('Digite um número: '))

# if numero % 2 == 0:
#     print(f'O número {numero} é par.')
# else:
#     print(f'O número {numero} é ímpar.')

#-------------------------------

#idade = int(input('Digite sua idade: '))

# if 0 <= idade <= 12:
#     print('Você é uma criança.')
# elif 12 < idade < 18:
#     print('Você é um adolescente.')
# else:
#     print('Você é um adulto.')


#-------------------------------

# usuario = 'victtorazzi'
# senha = '123456'

# nome = input('Digite seu nome de usuário: ')
# senha_digitada = input('Digite sua senha: ')

# if nome == usuario and senha_digitada == senha:
#     print('Acesso permitido')
# else:
#     print('Acesso negado')

#-------------------------------

# lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_nomes = ['Victtor', 'Tiago', 'Lucas', 'Maria']
# lista_anos = [2005, 2026]

# #-------------------------------

# # for numero in lista_num:
# #     print(numero)
# # for nome in lista_nomes:
# #     print(nome)
# # for ano in lista_anos:
# #     print(ano)

# #-------------------------------

# soma = 0
# for i in range(1, 11, 2):
#     soma += i
# print(f'A soma dos números ímpares é:{soma}')

# for i in range(10, 0, -1):
#     print(i)

# numero = int(input('Digite um número: '))
# for i in range(1, 11):
#     print(f'{numero} x {i} = {numero * i}')

# #-------------------------------

# lista_numeros = [1, 2, 3, 4, 5]
# soma1 = 0

# try:
#     for numero in lista_numeros:
#         soma1 += numero
#     print(f'A soma dos números é: {soma1}')
# except TypeError:
#     print('Erro: Certifique-se de que todos os elementos da lista sejam números.')

# #-------------------------------

# lista_numeros = [1,'a', 3, 4, 5]
# soma = 0
# try:
#     for i in lista_numeros:
#         soma += i
#     media = soma / len(lista_numeros)
#     print(f'A média dos números é: {media}')
# except ZeroDivisionError:
#     print('Erro: A lista está vazia, não é possível calcular a média.')
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')

#-------------------------------
# pessoa = {'nome': 'Tiago', 'idade': 18, 'cidade': 'São Paulo'}

# print(pessoa)
# pessoa['idade'] = 19
# print(pessoa)
# pessoa['Profissão'] = 'Programador'
# print(pessoa)
# del pessoa['cidade']

# print(pessoa)
#-------------------------------
# numero_quadrado = {x: x**2 for x in range(1, 6)}
# print(numero_quadrado)
#-------------------------------

# pessoa = {'nome': 'Tiago', 'idade': 18, 'cidade': 'São Paulo'}
# palavra_chave = input('Digite a chave que deseja verificar: ')

# if palavra_chave in pessoa:
#     print(f"A chave '{palavra_chave}' existe no dicionário.")
# else:
#     print(f"A chave '{palavra_chave}' não existe no dicionário.")

#-------------------------------

# frase = input('Digite uma frase: ')
# palavras = {}
# for palavra in frase.split():
#     palavras[palavra] = palavras.get(palavra, 0) + 1
# print(palavras)

#-------------------------------

# macas = int(input('Digite a quantidade de maçãs vendidas: '))
# bananas = int(input('Digite a quantidade de bananas vendidas: '))

# if macas > bananas:
#     print('Você vendeu mais maçãs do que bananas.')  
# elif macas < bananas:
#     print('Você vendeu mais bananas do que maçãs.')   
# else:
#     print('Você vendeu a mesma quantidade de maçãs e bananas.')

#-------------------------------
# tempo = 0
# a = int(input('Digite os dias para realizar a atividade A: '))
# b = int(input('Digite os dias para terminar a atividade B: '))
# c = int(input('Digite os dias para terminar a atividade C: '))

# if (a < 0 or b < 0 or c < 0):
#     print("Os dias não podem ser negativos")
# else:
#     tempo = a+b+c
#     print(f'O tempo total para fazer as atividades é de {tempo} dias')

#-----------------------------

# temperatura = int(input('Digite a temperatura atual: '))

# if temperatura > 25:
#     print('Atenção, temperatura acima do limite máximo')
# else:
#     print('Temperatura dentro do limite')

#----------------------------

# peso = float(input('Digite seu peso atual(kg): '))
# altura = float(input('Digite sua altura(m): '))

# def calc_imc(peso,altura):
#     imc = peso/(altura**2)
#     return imc

# print(f'Seu IMC é: {calc_imc(peso,altura):.2f}')

# if calc_imc(peso,altura) < 18.5:
#     print('Você está abaixo do peso!')
# elif 18.5 <= calc_imc(peso,altura) < 25:
#     print('Você está no peso normal!')
# else:
#     print('Você está acima do peso!')

#------------------------------

# gastos = float(input('Digite seu gasto deste mês: '))
# limite = 3000

# if gastos > limite:
#     print('Cuidado. Você passou do limite mensal.')
# else:
#     print('Você ainda está no dentro do limite mensal.')

#-------------------------------

# hora = int(input('Digite o horario de entrada: '))

# if 8 <= hora < 18:
#     print('Acesso liberado')
# else:
#     print('Acesso negado')

#----------------------------------

# nota1 = float(input('Digite sua primeira nota: '))
# nota2 = float(input('Digite sua segunda nota: '))
# nota3 = float(input('Digite sua terceira nota: '))

# media = (nota1+nota2+nota3)/3

# print(f'Media:{media:.1f} ')

# if media < 5:
#     print('Reprovado')
# elif media < 7:
#     print('Em recuperação')
# else:
#     print('Aprovado')

#=====================================

# km = int(input('Digite quantos km: '))
# pedagio = 0

# if km <= 100:
#     pedagio = 10
# elif 100 < km <= 200:
#     pedagio = 20
# else:
#     pedagio = 30

# print(f'Valor do pedágio é {pedagio}')

#========================================

# numero = int(input('Digite um número: '))

# if numero % 2 == 0:
#     print(f'O número {numero} é par')
# else:
#     print(f'O número {numero} é ímpar')

#=========================================

# valor = float(input('Digite o valor da renda mensal: '))
# parcela = float(input('Digite o valor da parcela desejada: '))

# if parcela <= valor*0.3 and valor > 2000:
#     print('Empréstimo aprovada')
# elif valor <= 2000:
#     print('Empréstimo negado. Renda insuficiente')
# else:
#     print('Empréstimo negada. Parcela acima de 30% da renda')

#======================================================================

# clientes = ['tiago','filipe','grazi','joyce','josé']

# for nome in clientes:
#     print(nome)

#=====================================================================

# contador = 0

# while contador < 10:
#     print('meu me amo')
#     contador += 1

#=====================================================================

# for i in range(5):
#     print('Bem vindo ao Buscante')

# contador = 0
# while contador < 5:
#     print('Bem vindo ao Alura')
#     contador+=1

#========================================

# valores = [10,20,30,40,50]
# soma = 0

# for valor in valores:
#     soma+=valor

# print(soma)

#=========================

# projetos = ['a','b','c','d',None,'f']

# for projeto in projetos:
#     if projeto is None:
#         print('Projeto faltando')
#     else:
#         print(projeto)
    
# =======================================

# livros = ['a','b','c','d','e']
# liv = input('Digite qual livro vc quer achar: ')

# for livro in livros:
#     if livro == liv:
#         print(f'O livro {livro} foi encontrado')
#         break

#===============================================

# contagem = 5

# while contagem > 0:
#     contagem -= 1
#     print(f'Você ainda tem {contagem}')

# print('Estoque esgotado')

#===============================================

# for i in range(10,0,-1):
#     if i %2 == 0:
#         print(f'"Faltam apenas {i} segundos - Não perca essa oportunidade!".')
#     else:
#         print(f'"A contagem continua: {i} segundos restantes.".')

# print('Aproveite a promoção agora')

#==================================================================================

# livros = [{"nome": "1984", "estoque": 5}, {"nome": "Dom Casmurro", "estoque": 0},
#     {"nome": "O Pequeno Príncipe", "estoque": 3}, {"nome": "O Hobbit", "estoque": 0},
#     {"nome": "Orgulho e Preconceito", "estoque": 2}]

# for livro in livros:
#     if livro['estoque'] > 0:
#         print(f'Livro disponível: {livro['nome']}')

#================================================================================

# while True:
#     nome = input('Digite seu nome de usuário: ')
#     senha = input('Digite sua senha: ')

#     if len(nome) < 5:
#         print('O nome precisa ter pelo menos 5 caractéres.')

#     elif len(senha) < 8:
#         print('A senha precisa ter pelo menos 8 caractéres.')

#     else: break

# print('Cadastro realizado com sucesso!')

#=================================================

# def calculo(nascimento, atual):
#     idade = atual - nascimento
#     return idade

# nascimento = int(input('Digite o ano do seu nascimento: '))
# atual = int(input('Digite o ano atual: '))
# idade = calculo(nascimento, atual)
# print(f'Sua idade atual é de {idade}')

#===============================================================
# def num_caraceter(palavra):
#     return len(palavra)

# palavra = input('Digite uma palavra para saber quantos caracteres ela tem: ')

# print(f'A palavra {palavra} tem {num_caraceter(palavra)} letras!')

#=============================================================

# def exibir_saudacao(hora):
#     if hora < 12:
#         return "Bom dia"
#     elif hora < 18:
#         return 'Boa tarde'
#     else:
#         return 'Boa noite'
    
# hora = int(input('Digite a hora atual (0-23): '))

# print(exibir_saudacao(hora))

#=========================================================================


# telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

# def converter(telefones):
#     return [int(telefone) for telefone in telefones]

# def verificacao(telefones):
#     for telefone in telefones:
#         if isinstance(telefone,int):
#             return 'Todos os números foram convertidos com sucesso!'
#         else:
#             return 'Erro'
    
# telefone_novo = converter(telefones)
# print(verificacao(telefone_novo))

#=====================================================================

# valores = input('Digite os valores a serem somados: ').split() ## Ignora os espaços
# total = sum(map(float,valores)) ## map transforma os números que estão em string para os dentro do parametro
# print(f'O total da soma dos valores foi: {total}')

#===================================================================

# numeros = input('Digite os números separados por espaço: ').split()

# pares = filter(lambda x:int(x)%2==0,numeros)

# print('Números pares:',' '.join(pares)) ## join transforma os numeros da lista em string

#====================================================================

# produtos = input('Digite os produtos separado por virgula: ').split(',')
# precos = input('Digite os preços separados por virgula: ').split(',')

# for produtos, precos in zip(produtos,precos):
#     print(f'{produtos.strip()}: {precos.strip()}')

#====================================================================

# primeiro = float(input('Digite o primeiro número: '))
# segundo = float(input('Digite o segundo número: '))
# sinal = input('Escolha a operação (| + | - | * | / |): ')

# soma = lambda x,y: x+y
# subtracao = lambda x,y: x-y
# multiplicacao = lambda x,y: x*y
# divisao = lambda x,y: x/y if y != 0 else "Erro"

# if sinal == '+':
#     print(f'O resultado é: {soma(primeiro,segundo)}')
# elif sinal == '-':
#     print(f'O resultado é: {subtracao(primeiro,segundo)}')
# elif sinal == '*':
#     print(f'O resultado é: {multiplicacao(primeiro,segundo)}')
# elif sinal == '/':
#     print(f'O resultado é: {divisao(primeiro,segundo)}')
# else:
#     print('Operação inválida')
    
#================================================================

# def desconto(porcentagem):
#     def calcular_valor(valor):
#         return valor - (valor*(porcentagem/100))
#     return calcular_valor

# porcentagem = float(input('Digite a porcentagem do desconto: '))

# calcular_valor_final = desconto(porcentagem)

# valor = float(input('Digite o valor da compra: '))


# print(f'Preço final com desconto: {calcular_valor_final(valor)}')

#=================================================================

# def somar(num):
#     if num == 0:
#         return 0
#     else:
#         return num + somar(num - 1)

# num = int(input('Digite um numero: '))

# print(f'A soma de 1 até {num} é {somar(num)}' )

#=================================================================

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

import re

nome = input('Digite o nome do cliente: ')

if re.fullmatch(r'[A-Z][a-z]*', nome):
    print('Nome válido.')
else:
    print('Nome inválido.')