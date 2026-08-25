cp = []
sp = []
for notas in range(0,3):
    notas = float(input("Digite a nota das cps do segundo semestre: "))

    cp.append(notas)

for notas in range(0,2):
    notas = float(input("Digite a nota das sps do segundo semestre: "))

    sp.append(notas)
gs = float(input("Digite a nota da gs segundo semestre: "))

menor_cp = 0

for i in range(len(cp)):
    if cp[i] < cp[menor_cp]:
        i =  menor_cp
media = ((cp[0] + cp[1] + sp[0] + sp[1]) / 4) * 0.4 + gs * 0.6

print(f"\nA menor nota dos Checkpoints foi: {menor_cp:.1f}")
print(f"A média do segundo semestre é: {media:.1f}")
