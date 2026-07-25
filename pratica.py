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

texto = input('Digite um texto: ')

palavras_longas = []

for palavra in texto.split():
    if len(palavra)>10:
        palavras_longas.append(palavra)

if palavras_longas:
    print(f'Palavras longas encontradas: {", ".join(palavras_longas)}')
else:
    print('Nenhuma palavra longa encontrada.')