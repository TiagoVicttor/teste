# valor = float(input('Digite o valor da conta: '))
# porcentagem = int(input('Digite a porcentagem da gorjeta: '))

# gorjeta = (porcentagem/100)*valor
# total = valor + gorjeta

# print(f'Valor da gorjeta: R${gorjeta:.2f}')
# print(f'Total a pagar: R${total:.2f}')

#=======================================================

# def verificar(cpf):
#     if not cpf.isdigit():
#         return 'Erro: O CPF de conter apenas dígitos'
#     elif len(cpf) > 11 or len(cpf) < 11:
#         return 'Erro: O CPF deve ter exatamente 11 dígitos'
#     else:
#         return 'CPF válido'


# cpf = input('Digite seu CPF: ')
# cpf_verificado = verificar(cpf)

# print(cpf_verificado)

#===================================================================

# def contador_vogais(texto):
#     vogais = 'aeiou'
#     quantidade = 0

#     for letra in texto.lower():
#         if letra in vogais:
#             quantidade+=1
#     return quantidade

# texto = input('Digite o texto: ')

# print(f'O texto contém {contador_vogais(texto)} vogais.')

#=======================================================================

# texto = input('Digite um texto: ')

# palavras_longas = []

# for palavra in texto.split():
#     if len(palavra)>10:
#         palavras_longas.append(palavra)

# if palavras_longas:
#     print(f'Palavras longas encontradas: {", ".join(palavras_longas)}')
# else:
#     print('Nenhuma palavra longa encontrada.')

#--------------------------------------------------------------

# import random

# def gerar_senha():

#     maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     minusculas = 'abcdefghijklmnopqrstuvwxyz'
#     numeros = '0123456789'
#     especiais = '!@#$%&*'

#     senha = [
#         random.choice(maiusculas),
#         random.choice(minusculas),
#         random.choice(numeros),
#         random.choice(especiais)
#     ]

#     todos_caracteres = maiusculas + minusculas + numeros + especiais
#     senha.extend(random.choices(todos_caracteres, k=8))
#     random.shuffle(senha)
#     return ''.join(senha)

# print(f'Senha gerada: {gerar_senha()}')

#_____________________________________________________________________________________

# import random

# def jokempo():
#     opcoes = ['pedra', 'papel', 'tesoura']
#     computador = random.choice(opcoes)
#     jogador = input('Escolha pedra, papel ou tesoura: ').lower()

#     if jogador not in opcoes:
#         print('Opção inválida. Tente novamente.')
#         return jokempo()

#     print(f'computador escolheu: {computador}')

#     if computador == jogador: 
#         print(f'Empate!')

#     elif (computador == 'pedra' and jogador == 'tesoura') or (computador == 'papel' and jogador == 'pedra') or (computador == 'tesoura' and jogador == 'papel'):
#         print('Computador venceu!')
        
#     else:
#         print('Jogador venceu!')

# jokempo()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# import random


# def adivinha():
#     numero_secreto = random.randint(1,100)
#     tentativas = 0

#     while True: 

#         numero = int(input('Tente adivinhar o número (1-100): '))

#         if numero < 1 or numero > 100:
#             print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.')
#             raise ValueError('Número fora do intervalo! Digite um número entre 1 e 100')

#         if numero < numero_secreto:
#             print('Muito Baixo! Tente novamente.')
#             tentativas += 1

#         elif numero > numero_secreto:
#             print('Muito Alto! Tente novamente.')
#             tentativas += 1

#         else:
#             print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.')
#             break

# adivinha()

#--------------------------------------------------------------------------------------------------------

# def calculadora():
#     primeiro = float(input('DIgite o primeiro número: '))
#     operacao = input('Digite a operação (+, -, *, /): ')
#     segundo = float(input('Digite o segundo número: '))

#     try:
#         if operacao == '+':
#             resultado = primeiro + segundo
#         elif operacao == '-':
#             resultado = primeiro - segundo
#         elif operacao == '*':
#             resultado = primeiro * segundo
#         elif operacao == '/':
#             resultado = primeiro / segundo
#         else:
#             print('Opção inválida. Escolha uma operação.')
#             return

#         print(f'Resultado: {resultado}')

#     except ValueError:
#         print('Erro: Entrada inválida. Digite apenas números.')
#     except ZeroDivisionError:
#         print('Erro: Divisão por zero não é permitida.')
# calculadora()

#====================================================================

# import os

# def gerenciador_tarefas():
#     tarefas = []

#     while True:
#         print('1. Adicionar tarefa')
#         print('2. Visualizar tarefas')
#         print('3. Remover tarefa')
#         print('4. Sair')

#         escolha = int(input('Escolha uma opção: '))

#         if escolha == 1:
#             os.system('cls')
#             tarefa = input('Digite a tarefa: ').split()
#             if tarefa:
#                 tarefas.append(tarefa)
#                 print('Tarefa adicionada!')
#             else:
#                 print('Erro: A tarefa não pode estar vazia.')
            

#         elif escolha == 2:
#             os.system('cls')
#             if tarefas:
#                 print('Tarefas:')
#                 for i, tarefa in enumerate(tarefas, 1):
#                     print(f'{i}. {tarefa}')
#             else:
#                 print('Nenhuma tarefa cadastrada.')

#         elif escolha == 3:
#             os.system('cls')
#             if tarefas:
#                 try:
#                     indice = int(input('Digite o número da tarefa a ser removida: '))
#                     if 1 <= indice <= len(tarefas):
#                         tarefa_removida = tarefas.pop(indice - 1)
#                         print(f'Tarefa "{tarefa_removida}" removida!')
#                     else:
#                         print('Erro: Número inválido. Digite um número válido')
#                 except ValueError:
#                     print('Erro: Entrada inválida. Digite um número')

#         elif escolha == 4:
#             os.system('cls')
#             print('Saindo do gerenciador de tarefas. Até mais!')
#             break

#         else:
#             print('Erro: Opção inválida. Escolha uma opção entre 1 e 4')

# gerenciador_tarefas()

#===========================================================================

