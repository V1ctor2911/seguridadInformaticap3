def function(n):    
    nombre = input("Escriba la palabra a codificar:\n").upper()
    cadena = ""
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  
    for i in range(len(nombre)):
        j = 0
        while j<len(abecedario) and abecedario[j] != nombre[i]:
            j += 1
        if j == len(abecedario):
            cadena = cadena + nombre[i]
        else:
            index = (j-n) % len(abecedario)
            cadena = cadena + abecedario[index] 
    print(cadena)  



desplazamiento = int(input("Escriba su clave (numero de desplazamiento):\n"))
function(desplazamiento)
