# def pertence_a_fibonacci(n):
#     fib = [0, 1]
#     while fib[-1] < n:
#         fib.append(fib[-1] + fib[-2])
#     return n in fib


# print(pertence_a_fibonacci(10))

def pertence_a_fibonacci(numero):
    fib_1, fib_2 = 0,1
    if numero in (0,1):
        return True
    
    while fib_2 < numero:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        if fib_2 == numero:
            return True

numero_predefinido = 21

try:
    numero_informado = int(input("Informe um número(ou pressione enter para usar o número predefinido): "))
except ValueError:
    numero_informado = numero_predefinido

resultado = pertence_a_fibonacci(numero_informado)       
print(resultado)
