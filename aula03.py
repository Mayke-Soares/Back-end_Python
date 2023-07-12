#ATIVIDADE CONDICIONAL - PYTHON

"""3. Receba um número e retorno se ele é maior, menor ou igual a zero:
● Solicite ao usuário que insira um número.
● Verifique se o número é maior que zero.
● Se for maior que zero, exiba uma mensagem informando que o número é maior que
zero. Se for igual a zero, informe que é igual a zero. Caso contrário, informe que é
menor que zero."""

numero = int(input("Digite um número! "))

if numero > 0: 
    print("Este número é maior que zero.")
elif numero == 0:
    print("Este núemro é igual a zero. ")
else:
    print("Esten núemro não é menor que zero. ")


