from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def cifrar_aes(texto, clave, vector_inicializacion):
    # Convertimos los textos a bytes
    data = texto.encode('utf-8')
    clave_bytes = clave.encode('utf-8')
    iv_bytes = vector_inicializacion.encode('utf-8')
    
    # Motor de cifrado y encriptamos
    cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
    encriptado = cipher.encrypt(pad(data, AES.block_size))
    
    return encriptado.hex().upper()

cadena_sin_cifrar = input("Introduzca la cadena a cifrar: ").strip()

# En AES-128 la clave y el IV deben tener exactamente 16 caracteres
clave_secreta = "SeguridadInforma"
iv_secreto = "SeguridadInforma"

mensaje_cifrado = cifrar_aes(cadena_sin_cifrar, clave_secreta, iv_secreto)
print("Resultado codificado: " + mensaje_cifrado)