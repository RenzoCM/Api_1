import random

class Candidato():
    def __init__(self, nombre, votos):
        self.nombre = nombre
        self.votos = votos


def getVotos(lista_de_candidatos:list, cantidad_votos:int) -> list:
    """
    Función auxiliar para obtener los votos de los candidatos

    params:
        lista_de_candidatos (list): lista de candidatos sin votos
        cantidad_votos (int): cantidad de votos a darse 

    output:
        list: retorna la misma lista de candidatos, pero con los votos obtenidos
        
    """
    for i in range(cantidad_votos):
        voto = random.randint(1,5)
        match voto:
            case 1:
                lista_de_candidatos[0].votos += 1
            case 2:
                lista_de_candidatos[1].votos += 1
            case 3:
                lista_de_candidatos[2].votos += 1
            case 4:
                lista_de_candidatos[3].votos += 1
            case 5:
                lista_de_candidatos[4].votos += 1
                
        
    return lista_de_candidatos
            
    

def obtenerResultadoEscrutinio(numero_electores:int) -> str:
    
    """
    Funcion para obtener los resultados de votación de x número de electores sobre 5 candidatos
    
    params:
    
    numero_electores:int -> Número de electores a votar
    
    output:
    
    string -> "El candidato ganador es x con un total de x votos"
    
    """
    
    lista_de_candidatos:list = [Candidato("Luis", 0), Candidato("Carlos", 0),Candidato("Alberto", 0),Candidato("Marcos", 0),Candidato("Jesús", 0)]
    
    
    #*Obtención de votos
    lista_de_candidatos:list = getVotos(lista_de_candidatos, numero_electores)
    
    
    #*Conteo de votos
    candidato_ganador:Candidato
    cantidad_maxima = 0
    
    for candidato in lista_de_candidatos:
        if candidato.votos > cantidad_maxima:
            cantidad_maxima = candidato.votos
            candidato_ganador = candidato
            
    return f"El candidato ganador es {candidato_ganador.nombre} con un total de {candidato_ganador.votos} votos"

print(obtenerResultadoEscrutinio(500))