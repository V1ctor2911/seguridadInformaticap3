import base64

# La cadena de prueba que te dio la profesora
mensaje_cifrado = input("introduzca manin:\n")

# 1. Decodificamos (la librería espera bytes o strings ASCII y devuelve bytes)
bytes_decodificados = base64.b64decode(mensaje_cifrado)

# 2. Convertimos los bytes crudos a texto normal legible
texto_final = bytes_decodificados.decode('utf-8')

print(f"El mensaje oculto es: {texto_final}")