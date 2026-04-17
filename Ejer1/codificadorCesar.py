
def function(n):    
    nombre = input().upper()
    cadena = ""
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  
    for i in range(len(nombre)):
        j = 0
        while j<26 and abecedario[j] != nombre[i]:
            j += 1
        if j == 26:
            cadena = cadena + nombre[i]
        else:
            index = (j-n) % 26
            cadena = cadena + abecedario[index] 
    print(cadena)  







desplazamiento = int(input("Escriba su clave (numero de desplazamiento):"))
function(desplazamiento)