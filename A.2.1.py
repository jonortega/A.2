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
        return "El archivo no se encontró."

if __name__ == "__main__":
    nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
    resumen_sha256 = calcular_sha256(nombre_archivo)
    print(f"Resumen SHA-256 del archivo {nombre_archivo}:")
    print(resumen_sha256)
