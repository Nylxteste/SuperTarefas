'''

Atividade Estrutura de Repetição;

Usar estrutura de repetição para a realização do trabalho.

1 - Imprima na tela os números de 1 até 100.
'''
def imprimir_faixa():
    tamanho = int(input('Digite o tamanho da faixa desejada: '))
    for x in range(1,tamanho+1):
        print(x)

'''
2 - Faça um programa que percorra todos os número de 1 até 100. Para os números ímpares, deve
ser impresso um“*”, e para os números pares, deve ser impresso dois “**”. Veja o exemplo abaixo:

// Saída
'''
def achar_impar_par():
    for x in range(1,101):
        if x % 2 == 0:
            print('**')
        else:
            print('*')

'''
*
**
*
**
*
**

3 - Faça um programa que percorra todos os número de 1 até 100. Para os números múltiplos de 4,
imprima a palavra “PI”, e para os outros, imprima o próprio número. Veja o exemplo abaixo:

// Saída
1
2
3
PI
5
6
7
PI
'''
def achar_multiplo_4():
    cont=0
    for i in range(1,101):
        if i %4 == 0:
            print('PI')
        else:
            print(i)

'''

4 - Crie umprograma que imprima na tela um triângulo de “*”. Veja o exemplo abaixo:

// Saída
*
**
***
****
*****
'''
def criar_um_triangulo():
    tamanho = int(input('Digite o tamanho do triangulo:'))
    cont = 0
    for x in range(tamanho):
        cont += 1
        for i in range(cont):

            if i != cont-1:
                print('*', end='')
            else:
                print('*')

'''

5 - Crie umprograma que imprima na tela vários triângulos de “*”. Observe o padrão abaixo.

// Saída
*
**
***
****
*
**
***
****
'''

def criar_triangulos():
    cont = 0
    triangulos = int(input('Quantos triangulos você precisa?'))
    tamanho = int(input('Qual o tamanho dos triangulos?'))
    for n in range(triangulos):
        cont = 0
        for x in range(tamanho):
            cont += 1
            for i in range(cont):

                if i != cont-1:
                    print('*', end='')
                else:
                    print('*')

'''

6 - Crie umprograma que imprima na tela um quadrado perfeito.Observe o padrão abaixo.

// Saída
*****
*****
*****
*****
*****
'''
def criar_quadrado():
    tamanho = int(input('Digite o tamanho do quadrado desejado: '))
    for i in range(tamanho):
        for x in range(tamanho):
            if x < tamanho-1:
                print('*  ', end='')
            else:
                print('*')
'''

7 - Use seus conhecimentos para criar um programa que mostre um menu de atalho para os 6
padrões que acabamos ver. Desenvolva um programa GerarPadroes com um menu com todas as opções acima.
'''



continuar = 'sim'

def gerar_padroes(x):
     return x

while continuar != 'n':
    print('''
    Selecione uma das pções disponíveis para uso:
    1 - Imprimir uma faixa
    2 - * para impar ** para par
    3 - Achar múltiplos de 4
    4 - Imprimir um triângulo
    5 - Imprimir vários triângulos (de acordo com sua necessidade)
    6 - Imprimir um quadrado (de acordo com sua necessidade)''')

    continuar = input('''PARA PARAR DIGITE "n"  
Digite o valor correspondente à atividade: ''')



    if continuar == '1':
        gerar_padroes(imprimir_faixa())
    elif continuar == '2':
        gerar_padroes(achar_impar_par())
    elif continuar == '3':
        gerar_padroes(achar_multiplo_4())
    elif continuar == '4':
        gerar_padroes(criar_um_triangulo())
    elif continuar == '5':
        gerar_padroes(criar_triangulos())
    elif continuar == '6':
        gerar_padroes(criar_quadrado())



