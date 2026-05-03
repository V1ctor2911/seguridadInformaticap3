import base64

mensaje_cifrado = input("introduzca el mensaje cifrado:\n")

# 1. Decodificamos 
bytes_decodificados = base64.b64decode(mensaje_cifrado)

# 2. Convertimos los bytes crudos a texto normal legible
texto_final = bytes_decodificados.decode('utf-8')

print("El mensaje oculto es:" + texto_final)