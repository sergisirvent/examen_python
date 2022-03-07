from functools import partial
import imp
from random import random
from random import randint


def choose_secret(filename):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    f = open(filename, mode="rt", encoding="utf-8")
    lista_lineas = f.readlines()
    numero_random = randint(0,len(lista_lineas))
    palabra = ""
    palabra += lista_lineas[numero_random][0]
    palabra += lista_lineas[numero_random][1]
    palabra += lista_lineas[numero_random][2]
    palabra += lista_lineas[numero_random][3]
    palabra += lista_lineas[numero_random][4]
    return palabra

    
def compare_words(word,secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position = []
    same_letter = []
    for i in range(0,len(word)):
      for j in range(0,len(secret)):
        if word[i] == secret[j]:
          if i == j:
            same_position.append(i)
          else:
            same_letter.append(i)

    return same_position,same_letter

def print_word(word,same_letter_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    posiciones_tocadas = []
    transform = ["c","i","n","c","o"]
    

    for i in range(0,len(same_letter)):
      posicion_a_cambiar = same_letter[i]
      posiciones_tocadas.append(same_letter[i])
      transform[posicion_a_cambiar] = word[posicion_a_cambiar].lower()
      

    for i in range(0,len(same_letter_position)):
      posicion_a_cambiar = same_letter_position[i]
      posiciones_tocadas.append(same_letter_position[i])
      transform[posicion_a_cambiar] = word[posicion_a_cambiar].upper()
      
      
    for i in range(0,len(word)):
      esta = False
      for j in range(0,len(posiciones_tocadas)):
        if i == posiciones_tocadas[j]:
          esta = True
      if not esta:
        transform[i] = "-"
        

    palabra_transform = ""
    for letra in transform:
      palabra_transform += letra

    return str(palabra_transform)

      

def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """

    f = open(filename, mode="rt", encoding="utf-8")
    lista_prohibidas = ["á","é","í","ó","ú"]
    lista_lineas_buenas = []
    for linea in f:
      acento = False
      for i in range(0,5):
        for j in range(len(lista_prohibidas)):
          if linea[i] == lista_prohibidas[j]:
            acento = True
        if not acento:
          lista_lineas_buenas.append(linea)

    selected = []
    for i in range(0,15):
      numero_random = randint(0,len(lista_lineas_buenas))
      #print(lista_lineas_buenas)
      palabra = ""
      palabra += lista_lineas_buenas[numero_random][0]
      palabra += lista_lineas_buenas[numero_random][1]
      palabra += lista_lineas_buenas[numero_random][2]
      palabra += lista_lineas_buenas[numero_random][3]
      palabra += lista_lineas_buenas[numero_random][4]
      selected.append(palabra)

    secret = selected[randint(0,15)]
    print(selected)
    return selected,secret



 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    correcta = False
    while not correcta:
      word = word = input("Introduce una palabra de la lista: ")
      for palabra in selected:
        if palabra == word:
          correcta = True

if __name__ == "__main__":

    selected,secret=choose_secret_advanced("palabras_reduced.txt")
    
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        
        same_position, same_letter = compare_words(word,secret)
        resultado=print_word(word,same_position,same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
