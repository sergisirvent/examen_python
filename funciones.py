import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    #El fallo es que estas comparando en el if, dos strings con el comparador logico <
    #Para arreglar este fallo se debe comparar clave con la posicion de la letra por parametro en el abecedario en el abecedario

    abecedario = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    indice = -1
    for i in range(0,len(abecedario)):
      indice = 0
      if letra.upper() == abecedario[i]:
        indice = i
        return indice
      

    for clave in diccionario:
        for palabra in diccionario[clave]:

            if palabra < indice:
                resultado=[]
                resultado.append(palabra)
    #return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    #el fallo era que accedia a la clave con [nif], pero ademas en la asigancion volvia a repetir nif
    #La solucion para esta funcion es quitar el nif de dentro de los corchetes , ya que con la linea 43 ya estamos accediendo a la informacion asociada a esa clave
    clients_list[nif] = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email
    }

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """   
    #El error era que al eliminar las cartas para que no se repitieran, se eliminaban de la lista y no podian volver a ser elegidas en otra combinacion distinta
    #Como solucion he cambiado la manera en que se vuelven a añadir las cartas a la lista de cartas disponibles para las combinaciones
    combinaciones={}
    cartas_aleatorias = []
    for i in range(1,repeticiones+1):
      for carta in cartas_iniciales:
        cartas_aleatorias.append(carta)
        
      combinaciones["repeticion"+str(i)]=[]
      
      for j in range(0,5):
          carta=random.choice(cartas_aleatorias)
          combinaciones["repeticion"+str(i)].append(carta)
          cartas_aleatorias.remove(carta)

    return combinaciones


