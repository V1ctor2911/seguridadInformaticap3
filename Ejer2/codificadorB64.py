import base64

# Pedimos el mensaje normal al usuario
mensaje_claro = input("Introduce el mensaje a codificar:\n")

# 1. Convertimos el texto normal (String) a datos crudos (Bytes) usando encode
bytes_normales = mensaje_claro.encode('utf-8')

# 2. Codificamos a Base64 (Usamos b64encode para ocultar el mensaje)
bytes_codificados = base64.b64encode(bytes_normales)

# 3. Convertimos los bytes resultantes a texto legible para imprimirlo bonito
texto_base64 = bytes_codificados.decode('utf-8')

print(f"Tu mensaje en Base64 es: {texto_base64}")