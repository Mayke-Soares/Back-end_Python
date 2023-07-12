#ATIVIDADE CONDICIONAL - PYTHON

"""2. Receba um número e retorne se é par ou ímpar:
● Solicite ao usuário que insira um número.
● Verifique se o número é divisível por 2.
● Se for divisível por 2, exiba uma mensagem informando que o número é par. Caso
contrário, informe que é ímpar"""

numero = int(input("Digite um número! "))

if numero %2 == 0:
    print("Este número é par.")
else:
    print("Este número é impar.")
    