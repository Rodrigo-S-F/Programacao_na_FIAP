numero1 = float(input("Primeiro numero: "))
numero2 = float(input("Segundo numero: "))
operacao = str(input("qual operação deseja usar? soma, subtração, divisão, multiplicação "))

if operacao == 'soma':
    resultado = numero1 + numero2
    print (f" Resultado {resultado}")
elif operacao == 'subtração':
    resultado = numero1 - numero2
    print(f" Resultado {resultado}")
elif operacao == 'divisão':
    resultado = numero1 / numero2
    print(f" Resultado {resultado}")
elif operacao == 'multiplicação':
    resultado = numero1 * numero2
    print(f" Resultado {resultado}")

valor = float(input("valor da casa? "))
salario = float(input("salario? "))
anos = float(input("quantos anos pra pagar? "))

prestacao = valor / (anos * 12)

if prestacao > salario * 0.30:
    print("Você não foi liberado")
else:
    print("Você foi liberado")

