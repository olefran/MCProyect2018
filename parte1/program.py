# -*- coding: UTF-8 -*-
# Compilar con python3
# Programa para búsqueda de cadenas utilizando AFD
# Matemáticas Computacionales - 09/Feb/2018
# Equipo:
# - Eduardo Larios Fernández - A00569364
# - Oswaldo David García Rodríguez - A01026725
# - Oscar Israel Lerma Franco - A01380817 

def siguiente_estado(patron, pat_len, estado, caracter):
    # Esta función obtiene el estado siguiente
    # Si el caracter es igual al encontrado en el patrón
    # incrementamos el estado (nos movemos hacia adelante)
    # sig_est guarda temporalmente el resultado.
    i = 0 

    if estado < pat_len and caracter == ord(patron[estado]):
        return estado + 1
    
    for sig_est in range(estado, 0, -1): 
        if ord(patron[sig_est - 1]) == caracter:
            for i in range(sig_est - 1):   
                if patron[i] != patron[estado - sig_est + 1 + i]:   
                    break
                i += 1
            if i == (sig_est - 1):
                return sig_est
    return 0

def crear_TF(patron, pat_len, alfabeto_len):
    # Esta función construye la tabla de transiciones, 
    # la cual representa el AFD para el patrón dado

    # Inicialización de una tabla de transiciones de tamaño PAT_LEN X ALFABETO con valores vacíos
    TF = [[0 for i in range(alfabeto_len)] for i in range(pat_len + 1)]
    # creación de la tabla de transición 
    for estado in range(pat_len + 1):
        for caracter in range(alfabeto_len):
            TF[estado][caracter] = siguiente_estado(patron, pat_len, estado, caracter)

    return TF

def buscar(patron, texto, alfabeto):
    # Esta función simplemente imprime las ocurrencias del patrón
    # en el texto y el lugar donde aparecen (contando desde 1)
    alfabeto_len = len(alfabeto)
    pat_len = len(patron)
    txt_len = len(texto)
    estado = 0
    total = 0

    # Creación de la tabla de transiciones
    TF = crear_TF(patron, pat_len, alfabeto_len)
    # print(TF)

    # Procesa el texto utilizando la tabla de transiciones
    for i in range(txt_len):
        estado = TF[estado][ord(texto[i])]
        if (estado == pat_len):
            total = total+1
    return total
    
def main():
    # Función de entrada del programa, espera por el input y manda a llamar la función de búsqueda.
    # Alfabeto indicado por el usuario
    alfabeto = input()
    
    # Patrón indicado por el usuario
    patron = input()

    # Cadena sobre la cual se buscará el patrón
    texto = input()

    # Llamada a función de búsqueda, regresa el total de encuentros
    print(buscar(patron, texto, alfabeto))

if __name__ == '__main__':
    main()
