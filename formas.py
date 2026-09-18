def area_quadrado():
    lado = float(input('Digite o valor de lado desejado: '))
    area = lado * lado
    print (area)

def area_circulo():
    raio = float(input('Digite o valor de raio desejado: '))
    area = 3.14 * raio * raio
    print (area)

def area_triangulo():
    altura = float(input('Digite o valor de altura desejado: '))
    base = float(input('Digite o valor de base desejado: '))
    area = base * altura /2
    print (area)

def area_retangulo():
    altura = float(input('Digite o valor de altura desejado: '))
    base = float(input('Digite o valor de base desejado: '))
    area = base * altura
    print (area)

def area_paralelogramo():
    base = float(input('Digite o valor de base desejado: '))
    altura = float(input('Digite o valor de altura desejado: '))
    area = base * altura
    print (area)

def area_losango():
    d1 = float(input('Digite o valor de diagonal maior desejado: '))
    d2 = float(input('Digite o valor de diagonal menor desejado: '))
    area = d1 * d2 /2
    print (area)

def area_trapezio():
    B = float(input('Digite o valor de diagonal desejado: '))
    b = float(input('Digite o valor de diagonal desejado: '))
    altura = float(input('Digite o valor de altura desejado: '))
    area = (B + b) * altura /2
    print (area)

while True:
    print ('1 - Círculo')
    print ('2 - Triângulo')
    print ('3 - Quadrado')
    print ('3 - Retângulo')
    print ('4 - Paralelogramo')
    print  ('5 - Losango')
    print ('6 - Trapézio')

    opcao = input('Escolha uma opção (1/2/3/4/5/6/7/0): ')
    if opcao == '1':
        area_circulo()

    elif opcao == '2':
        area_triangulo()

    elif opcao == '3':
        area_quadrado()

    elif opcao == '4':
        area_paralelogramo()

    elif opcao == '5':
        area_losango()

    elif opcao == '6':
        area_trapezio()

    elif opcao == '0':
        break