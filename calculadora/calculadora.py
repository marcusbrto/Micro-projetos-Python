import matematica

print("=" * 50)
print(" Calculadora ".center(50, "-"))
print("=" * 50)

while True:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    opcao = str(input("Digite o simbolo do tipo da operação \033[32m[+,-,*,/]\033[m: "))
    if opcao == "+":
        matematica.soma(num1, num2)
        print("=" * 50)
    elif opcao == "-":
        result = abs(num1 - num2)
        print(f"Resultado: {result}")
    elif opcao == "*":
        print("Resultado:",num1 * num2)
    else:
        if opcao == "/" and num2 == 0:
            print("Não pode ser dividido por zero!")
        else:
            print("Resultado:",num1 / num2)
    while True:
        cont = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
        if cont in "SN":
            break
        print("Resposta errada!")
    if cont == "N":
          break