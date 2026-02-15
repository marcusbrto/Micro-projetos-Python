notas = []

print("="*40)
print("SISTEMA DE NOTAS".center(40))
print("="*40)

while True:

    try:
        nota = float(input(f"Digite a {len(notas)+1} nota: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if nota < 0 or nota > 10:
        print("Valor inválido. Digite entre 0 e 10.")
        continue

    notas.append(nota)

    if len(notas) >= 2:
        cont = input("Deseja continuar?[S/N]: ").strip().upper()[0]
        if cont == "N":
            break


maior = max(notas)
menor = min(notas)
media = sum(notas) / len(notas)

print("\nRESULTADO")
print("-"*40)

if media > 7:
    print("Situação: BOM")
elif media >= 5:
    print("Situação: RAZOAVEL")
else:
    print("Situação: HORRIVEL")

print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média: {media:.2f}")
