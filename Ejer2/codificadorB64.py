import base64

# Pedimos el mensaje normal al usuario
mensaje_claro = input("Introduce el mensaje a codificar:\n")

# 1. Convertimos el texto normal a Bytes usando encode
bytes_normales = mensaje_claro.encode('utf-8')

# 2. Codificamos a Base64 usando la función b64encode de la librería base64
bytes_codificados = base64.b64encode(bytes_normales)

# 3. Convertimos los bytes resultantes a texto legible para imprimirlo usando decode
texto_base64 = bytes_codificados.decode('utf-8')

print("Tu mensaje en Base64 es: " + texto_base64)