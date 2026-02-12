import matematica

print("=" * 50)
print(" Calculadora ".center(50, "-"))
print("=" * 50)

while True:
    opcao = str(input("Digite o simbolo do tipo da operação \033[32m[+,-,*,/]\033[m: "))
    print(f"\033[42m N1 {opcao} N2 = Resp \033[m".center(50, "~"))
    num1 = int(input("Digite o primeiro numero: "))
    print(f"\033[42m {num1} {opcao} N2 = Resp \033[m".center(50, "~"))
    num2 = int(input("Digite o segundo numero: "))
    if opcao == "+":
        print(f"\033[42m {num1} {opcao} {num2} = {matematica.soma(num1, num2)} \033[m".center(50, "~"))
    elif opcao == "-":
        print(f"\033[42m {num1} {opcao} {num2} = {matematica.sub(num1, num2)} \033[m".center(50, "~"))
    elif opcao == "*":
        print(f"\033[42m {num1} {opcao} {num2} = {matematica.multiplicar(num1, num2)} \033[m".center(50, "~"))
    else:
        print(f"\033[42m {num1} {opcao} {num2} = {matematica.dividir(num1, num2)} \033[m".center(50, "~"))
    while True:
        cont = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
        if cont in "SN":
            break
        print("Resposta errada!")
    if cont == "N":
        print("\033[31mEncerrando...\033[m")
        break
