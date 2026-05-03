limite = 52
alfabeto = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
vigenere = []

for i in range(0,limite):
    vigenere.append(alfabeto.copy())
    alfabeto.append(alfabeto.pop(0))

clave = input("introduce la clave: ").strip()
mensaje = input("introduzca el mensaje a cifrar:  ").strip()

claves = []

n = len(mensaje)//len(clave) 
if (len(mensaje) % len(clave)) != 0:
    for i in range(n):
        for j in range(len(clave)):
            claves.append(clave[j])
    for i in range(len(mensaje) % len(clave)):
        claves.append(clave[i])
else:
    for i in range(n):
        for j in range(len(clave)):
            claves.append(clave[j])

longClave = len(claves)

def buscar(x, y):
    i = 0
    while vigenere[i][0] != x:
        i += 1        
    j = 0
    while alfabeto[j] != y:
        j += 1
    return vigenere[i][j]

res = []
for i in range(0, longClave):
    res.append(buscar(claves[i], mensaje[i]))

resultado = "".join(res)
print("El mensaje cifrado es: " + resultado)