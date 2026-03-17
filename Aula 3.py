# from docutils.io import Input
# # Priemira atividade
# media_final = float(input("Qual foi sua média final? "))
#
# if media_final >= 6:
#     print("Aprovado")
# else:
#  print ("Reprovado")
# print ("\n")
#  #Segunda atividade
#
# Velocidade = float(input('Em qual velocidade você estava dirigindo?'))
#
# if Velocidade > 80:
#     print(" multado \n ")
#     print(f"Multa a pagar: {(Velocidade - 80) * 5}")
# else:
#     print("Você não recebeu multa")

# Terceira atividade
#
# num1 = int(input("Digite o primeiro número "))
# num2 = int(input("Digite o segundo número "))
# num3 = int(input("Digite o terceiro número \n "))
#
# if num1 >= num2 and num1 >= num3 :
#     print(f"O maior número é {num1} \n ")
# if num2 >= num1 and num2 >= num3:
#     print(f"O maior número é {num2} \n ")
# if num3 >= num2 and num3 >= num1:
#     print(f"O maior número é {num3} \n ")
#
# if num1 <= num2 and num1 <= num3:
#     print(f"O menor número é {num1} \n")
# if num2 <= num1 and num2 <= num3:
#     print(f"O menor número é {num2} \n ")
# if num3 <= num2 and num3 <= num1:
#     print(f"O menor número é {num3} \n ")
#
# Terceira atividade

# salario = float(input("Qual o seu salário? \n"))
#
# if salario > 1250:
#     print(f"Seu salário é de {(salario * 1.10) - salario:.2f} \n")
# if salario <= 1250:
#     print (f"Seu salário é de {(salario * 1.50) - salario:.2f} \n")

distancia = int(input("distância que você deseja percorrer em km "))

if distancia <= 200:
     distanciaM = distancia * 0.5
     print(f" O preço da passagem ficou {distanciaM} \n")

else:
    distanciaM = distancia * 0.45
print(f"O preço da passagem ficou {distanciaM} \n")