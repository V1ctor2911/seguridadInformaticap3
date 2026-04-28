def operador_xor(texto, clave):

    resultado = ""
    longitud_clave = len(clave)
    
    for i in range(len(texto)):
        char_texto = texto[i]    
        char_clave = clave[i % longitud_clave]       
        valor_xor = ord(char_texto) ^ ord(char_clave)
        resultado += chr(valor_xor)
    return resultado

def codificador_xor(texto, clave):
    return operador_xor(texto, clave)

def decodificador_xor(texto, clave):
    return operador_xor(texto, clave)


cadena_cifrada = input("Introduzca la cadena_cifrada: ").strip()
clave = input("Introduzca la clave: ").strip()

print("--- Ejecución del Decodificador ---")
mensaje_descifrado = decodificador_xor(cadena_cifrada, clave)
print(f"Texto cifrado: {cadena_cifrada}")
print(f"Clave usada:   {clave}")
print(f"Resultado decodificado: '{mensaje_descifrado}'")

print("\n--- Ejecución del Codificador (Verificación) ---")
mensaje_recodificado = codificador_xor(mensaje_descifrado, clave)
print(f"Texto original: {mensaje_descifrado}")
print(f"Clave usada:    {clave}")
print(f"Resultado recodificado: '{mensaje_recodificado}'")