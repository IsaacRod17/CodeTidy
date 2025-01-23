def clean_code(code):
    # Función que limpia el código (eliminar comentarios y líneas vacías)
    cleaned_code = "\n".join([line for line in code.split("\n") if line.strip() and not line.strip().startswith("#")])
    return cleaned_code
