from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def descifrar_aes(texto_hexadecimal, clave, vector_inicializacion):
    # Convertimos el texto hexadecimal de vuelta a bytes
    data = bytes.fromhex(texto_hexadecimal)
    clave_bytes = clave.encode('utf-8')
    iv_bytes = vector_inicializacion.encode('utf-8')
    
    # Creamos el motor de descifrado y desencriptamos
    cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
    desencriptado = unpad(cipher.decrypt(data), AES.block_size)
    
    return desencriptado.decode('utf-8')

cadena_cifrada = input("Introduzca la cadena a descifrar (en hexadecimal): ").strip()

# Deben ser exactamente los mismos que se usaron para cifrar
clave_secreta = "SeguridadInforma"
iv_secreto = "SeguridadInforma"

mensaje_descifrado = descifrar_aes(cadena_cifrada, clave_secreta, iv_secreto)
print("Resultado descodificado: " + mensaje_descifrado)