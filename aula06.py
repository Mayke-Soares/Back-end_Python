#ATIVIDADE CONDICIONAL - PYTHON

"""6. O Cinemas Teresina Shopping lhe contratou para desenvolver um algoritmo para
saber se uma pessoa tem direito a meia-entrada do cinema:
● Solicite ao usuário que informe sua idade.
● Verifique se a idade é menor ou igual a 12 ou se é maior ou igual a 60.
● Se atender a qualquer uma das condições, exiba uma mensagem informando que a
pessoa tem direito a meia-entrada. Caso contrário, informe que não tem direito."""

#Guardando idade na variável idade
idade = int(input("Digite sua idade: "))

#Verificando se a idade atende as condiçoes pedidadas.
if idade <= 12: or idade >= 60:
    print("Você tem direito a meia entrada. ")
else:
    print("Você não tem direito a meia entrada. ")

