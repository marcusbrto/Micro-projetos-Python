def soma(n1, n2):
    return (n1 + n2)

def sub(num1, num2):
    return abs(num1 - num2)

def multiplicar(num1, num2):
    return (num1 * num2)

def dividir(num1, num2):
    if num2 == 0 or num1 == 0:
        return "Zero não pode ser dividido!"
    else:
        return (num1 / num2)