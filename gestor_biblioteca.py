# Solicitar la opinión del usuario
opinion = input("Ingrese su opinión sobre el libro: ")

opinion_limpia = opinion.strip()

opinion_limpia = opinion_limpia.lower()

veces_recomiendo = opinion_limpia.count("recomiendo")

# Mostrar resultados
print("\nOpinión limpia:")
print(opinion_limpia)
print(f"\nLa palabra 'recomiendo' aparece {veces_recomiendo} veces.")