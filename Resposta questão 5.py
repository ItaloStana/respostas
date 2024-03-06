def inverter_string(s):
    inverted_string = ""

    for char in s:
        inverted_string = char + inverted_string

    return inverted_string

# Exemplo de uso com a string "17"
entrada = "17"
resultado = inverter_string(entrada)

print(f"A string invertida de '{entrada}' é '{resultado}'.")