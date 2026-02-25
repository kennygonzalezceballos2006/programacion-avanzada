categoria = input("Ingrese el nombre de la nueva categoría: ")

if 5 <= len(categoria) <= 12:
    
    categoria_mayus = categoria.upper()
    print(f"Categoría registrada exitosamente: {categoria_mayus}")
else:
    print("Nombre inválido. Debe tener entre 5 y 12 caracteres.")