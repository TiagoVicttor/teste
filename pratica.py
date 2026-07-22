# valor = float(input('Digite o valor da conta: '))
# porcentagem = int(input('Digite a porcentagem da gorjeta: '))

# gorjeta = (porcentagem/100)*valor
# total = valor + gorjeta

# print(f'Valor da gorjeta: R${gorjeta:.2f}')
# print(f'Total a pagar: R${total:.2f}')

#=======================================================

def verificar(cpf):
    if not cpf.isdigit():
        return 'Erro: O CPF de conter apenas dígitos'
    elif len(cpf) > 11 or len(cpf) < 11:
        return 'Erro: O CPF deve ter exatamente 11 dígitos'
    else:
        return 'CPF válido'


cpf = input('Digite seu CPF: ')
cpf_verificado = verificar(cpf)

print(cpf_verificado)




