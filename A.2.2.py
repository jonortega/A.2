import hashlib

def calcular_sha256(nombre_archivo):
    sha256 = hashlib.sha256()

    try:
        with open(nombre_archivo, "rb") as archivo:
            while True:
                data = archivo.read(65536)  # Leer en bloques de 64 KB
                if not data:
                    break
                sha256.update(data)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def agregar_resumen_al_archivo(entrada, salida):
    try:
        # Leer el contenido del archivo de entrada
        with open(entrada, "r") as archivo_entrada:
            contenido = archivo_entrada.read()

        # Calcular el resumen SHA-256
        resumen_sha256 = calcular_sha256(entrada)

        # Abrir el archivo de salida para escribir
        with open(salida, "w") as archivo_salida:
            # Copiar el contenido del archivo de entrada al archivo de salida
            archivo_salida.write(contenido)

            # Agregar la línea con el resumen SHA-256
            archivo_salida.write(f"\nhex:{resumen_sha256}")

        print(f"Se ha creado el archivo {salida} con el resumen SHA-256.")
    except FileNotFoundError:
        print("El archivo de entrada no se encontró.")

if __name__ == "__main__":
    nombre_archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
    nombre_archivo_salida = input("Ingrese el nombre del archivo de salida: ")
    agregar_resumen_al_archivo(nombre_archivo_entrada, nombre_archivo_salida)
