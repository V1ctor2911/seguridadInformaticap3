# 🛡️ Práctica 3: Seguridad Informática - URJC

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Universidad](https://img.shields.io/badge/URJC-Seguridad_Informática-red)

Este repositorio contiene la **Práctica número 3** de la asignatura de Seguridad Informática impartida en la Universidad Rey Juan Carlos (URJC). 

El objetivo principal de esta práctica es comprender la base de la criptografía mediante el desarrollo en Python de scripts capaces de **codificar y decodificar** información utilizando diferentes algoritmos y métodos de cifrado clásicos y modernos.

## 📂 Estructura del Proyecto

El repositorio consta de 4 ejercicios principales (distribuidos en 5 partes), cada uno en su respectivo directorio:

* **`Ejer1/` - Cifrado César**
    * `codificadorCesar.py`: Cifra un texto desplazando sus caracteres un número de posiciones en el alfabeto.
    * `decodificadorCesar.py`: Descifra un texto cifrado con César aplicando el desplazamiento inverso.

* **`Ejer2/` - Codificación Base64**
    * `codificadorB64.py`: Convierte un texto plano a formato Base64.
    * `decodificarB64.py`: Decodifica un mensaje oculto en Base64 de vuelta a texto legible.

* **`Ejer3/` - Cifrado Vigenère**
    * `vigenere_decode.py`: Descifra un mensaje cifrado mediante el algoritmo polialfabético de Vigenère, dada una clave específica.

* **`Ejer4/` - Cifrado XOR**
    * `cifrado_xor.py`: Aplica la operación lógica XOR entre los caracteres de un texto y una clave para cifrar el mensaje.
    * `descifrado_xor.py`: Revierte la operación XOR utilizando la misma clave para recuperar el texto original.

## 🚀 Requisitos y Ejecución

Para ejecutar cualquiera de los scripts de este repositorio, únicamente necesitas tener instalado **Python 3.x** en tu sistema. No se requieren librerías externas adicionales, ya que se hace uso de módulos integrados en Python como `base64`.

**Instrucciones de ejecución:**
1. Clona el repositorio en tu máquina local:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd seguridadInformaticap3

2. Ejecuta el script deseado usando la terminal. Por ejemplo, para el codificador César:
   ```bash
   python Ejer1/codificadorCesar.py
3. Sigue las instrucciones que aparecerán en la consola (introducir texto, claves, etc.).

## 👨‍💻 Desarrolladores

Práctica desarrollada por:
* Víctor Omar Llantoy Núñez del Arco
* Adam El Kassmi Serroukh




Universidad Rey Juan Carlos (URJC) - Grado en Ingeniería Informática / Seguridad Informática
