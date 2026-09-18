notas = []

def novas_notas():
    nova_nota = float(input('Adicione a nota: '))
    notas.append (nova_nota)

    for nota in notas:
        print (f'Sua nota é: {nota}')

def exclusao_notas():
    excluir = float(input('Exclua a nota: '))
    notas.remove (excluir)

    for nota in notas:
        print (f'Sua nota é: {nota}')

opcoes = ['nao', 'não', 'sim']

while True:
    escolha = input('Deseja adicionar uma nota? ')
    if escolha not in opcoes:
        print ('Responda com sim ou não')

    elif escolha == 'sim':
        novas_notas()

    elif escolha == 'nao':
        escolha2 = input('Deseja excluir uma nota? ')
        if escolha2 == 'sim':
            print (notas)
            exclusao_notas()
        elif escolha2 == 'nao' or escolha2 == 'não':
            break