def operador_xor(texto, clave):
    resultado = ""
    longitud_clave = len(clave)
    for i in range(len(texto)):
        char_texto = texto[i]    
        char_clave = clave[i % longitud_clave]       
        valor_xor = ord(char_texto) ^ ord(char_clave)
        resultado += chr(valor_xor)
    return resultado


cadena_sin_cifrar = input("Introduzca la cadena a cifrar: ").strip()
clave = input("Introduzca la clave: ").strip()

mensaje_cifrado = operador_xor(cadena_sin_cifrar, clave)
print("Resultado codificado: "+ mensaje_cifrado)