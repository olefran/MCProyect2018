# Programa para búsqueda de cadenas utilizando AFD
# Matemáticas Computacionales - 09/Feb/2018
# Equipo:
# - Eduardo Larios Fernández - A00569364
# - Oswaldo David García Rodríguez - A01026725
# - Oscar Israel Lerma Franco - A01380817 

# What the fuck is this, someone please explain
NUM_CHARS = 256

def siguiente_estado():
    pass

def crear_TF(patron, pat_len):
    estado = 0
    num_estado = 0

    for estado in range(pat_len + 1):
        for num_estado in range(NUM_CHARS):
            TF[estado][num_estado] = siguiente_estado()
    return TF

def buscar(patron, texto):
    pat_len = len(patron)
    txt_len = len(texto)
    estado = 0

    # Creación de la tabla de transiciones
    TF = crear_TF(patron, pat_len)

    # Procesa el texto utilizando la tabla de transiciones
    for i in range(txt_len):
        estado = TF[estado][texto[i]]
        if (estado == pat_len):
            print("\nPatrón encontrado en la locación: {}".format(i - pat_len + 1))

# Función de entrada del programa, espera por el input y manda a llamar la función de búsqueda.    
def main():
    # Cadena sobre la que se buscará el patrón
    print("Introduce el texto sobre el que buscar el patrón")
    texto = input()

    # Patrón a encontrar
    print("Introduce un patrón a buscar")
    patron = input()

    buscar(patron, texto)

if __name__ == '__main__':
    main()