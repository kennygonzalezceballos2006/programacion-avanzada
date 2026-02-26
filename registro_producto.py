while True:#ciclo para repetir la pregunta hasta que se cumpla las condiciones
    categoria = input("Ingrese el nombre de la nueva categoría: ")
    if 5 <= len(categoria) <= 12:
        categoria_mayus = categoria.upper()
        print(f"Categoría registrada exitosamente: {categoria_mayus}")
        print(f'el numero de letras es: {len(categoria)}')
        break
    else:
        print("Nombre inválido. Debe tener entre 5 y 12 caracteres.")