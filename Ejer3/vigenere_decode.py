limite = 52
alfabeto = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
vigenere = []

print(alfabeto)
print(vigenere)
for i in range(0,limite):
    vigenere.append(alfabeto.copy())
    alfabeto.append(alfabeto.pop(0))

clave = input().strip()
mensaje = input().strip()

claves = []

n = len(mensaje)//len(clave) 
if (len(mensaje) % len(clave)) != 0:
    for i in range(n):
        for j in range(len(clave)):
            claves.append(clave[j])
    for i in range(len(mensaje) % len(clave)):
        claves.append(clave[i])
else:
    print("si")
print(claves)
