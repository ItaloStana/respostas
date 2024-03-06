def pertence_fibonacci(num):
    if num < 0:
        return False
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return num in fib

numero = int(input("Digite um número: 1,7,9,21,"))
if pertence_fibonacci(numero):
    print(f"O número {1,21} pertence à sequência de Fibonacci.")
else:
    print(f"O número {1,7,9} não pertence à sequência de Fibonacci.")

    print(pertence_fibonacci)