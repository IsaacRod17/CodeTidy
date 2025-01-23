from cleaner import clean_code
from formatter import format_code
from linter import lint_code

def main():
    file_path = "examples/sample_code.py"  # Ruta al archivo que deseas procesar

    print("Procesando el archivo:", file_path)
    
    # Leer el archivo con el código Python
    try:
        with open(file_path, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no se encontró.")
        return  # Termina la ejecución si el archivo no se encuentra
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return
    
    # Limpieza del código
    cleaned_code = clean_code(code)
    print("\nCódigo limpio:")
    print(cleaned_code)
    
    # Formateo del código
    formatted_code = format_code(cleaned_code)
    print("\nCódigo formateado:")
    print(formatted_code)
    
    # Verificación de errores
    lint_result = lint_code(formatted_code)
    print("\nErrores detectados:")
    if lint_result:
        print(lint_result)
    else:
        print("No se detectaron errores.")

if __name__ == "__main__":
    main()