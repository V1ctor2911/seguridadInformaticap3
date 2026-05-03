def operador_xor(texto, clave):
    resultado = ""
    longitud_clave = len(clave)
    for i in range(len(texto)):
        char_texto = texto[i]    
        char_clave = clave[i % longitud_clave]       
        valor_xor = ord(char_texto) ^ ord(char_clave)
        resultado += chr(valor_xor)
    return resultado


cadena_cifrada = input("Introduzca la cadena cifrada: ").strip()
clave = input("Introduzca la clave: ").strip()

mensaje_descifrado = operador_xor(cadena_cifrada, clave)
print("Resultado decodificado:  " + mensaje_descifrado)