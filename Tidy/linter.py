def lint_code(code):
    # Función que verifica errores básicos
    errors = []
    if "==" in code:
        errors.append("Posible error de comparación")
    return errors

