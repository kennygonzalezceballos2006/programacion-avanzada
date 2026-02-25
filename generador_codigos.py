codigo = input("Ingrese el código del libro: ")

if not codigo.startswith("LIB-"):
    partes = codigo.split("-", 1)
    if len(partes) > 1:
        codigo = "LIB-" + partes[1]
    else:
        codigo = "LIB-" + codigo


parte_restante = codigo[4:]

if len(parte_restante) == 10 or len(parte_restante) == 13:
    print(f"Código válido: {codigo}")
else:
    print(f"Código inválido. La parte después de 'LIB-' debe tener 10 o 13 caracteres, actualmente tiene {len(parte_restante)}.")