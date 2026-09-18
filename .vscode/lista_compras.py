compras = []

def novas_compras():
    nova_compra = (input('Adicione o produto: '))
    compras.append (nova_compra)

    for compra in compras:
        print (f'Suas compras são: {compra}')

def exclusao_compras():
    excluir = (input('Digite o nome da compra para excluir: '))
    compras.remove (excluir)
    
    for compra in compras:
        print (f'Suas compras são: {compra}')
        

def modificar_compras():
    antigo = input('Qual item você deseja mudar? ')
    if antigo in compras:
        item = compras.index(antigo)
        mudanca = input(f'Digite qual compra deseja mudar a {antigo}? ')
        compras [item] = mudanca
        print ('Lista Atualizada!')

    elif antigo not in compras:
        print ('Produto Não Identificado. Tente Novamente.')

    for compra in compras:
            print (f'Suas compras são: {compra}')


opcoes = ['1', '2', '3', '4', '0']

while True:
    print ('1 - Mostrar Lista')
    print ('2 - Cadastrar Item')
    print ('3 - Excluir Lista')
    print ('4 - Modificar Item da Lista')
    print ('0 - Sair')

    escolha = input('Escolha dentre 0 a 4: ')
    if escolha not in opcoes:
        print ('Escolha dentre 0 a 4')
    if escolha == '1':
        for compra in compras:
            print (f'Suas compras são: {compra}')

    elif escolha == '2':
        novas_compras()

    elif escolha == '3':
        exclusao_compras()

    elif escolha == '4':
        modificar_compras()
    elif escolha == '0':
        break