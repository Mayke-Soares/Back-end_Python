#ATIVIDADE CONVENCIONAL - PYTHON

"""4. Pergunte para uma pessoa a sua idade e retorne se ele é maior de idade:
● Solicite ao usuário que insira sua idade.
● Verifique se a idade é maior ou igual a 18.
● Se for maior ou igual a 18, exiba uma mensagem informando que a pessoa é maior de
idade. Caso contrário, informe que é menor de idade."""

idade = int(input("Digite sua idade! "))

if idade >= 18:
    print("Você é maior de idade! ")
else:
    print("Você é menor de idade! ")

