import zipfile
import os


def zip_file(path: str, file: str) -> str:
    file_path = os.path.join(path, file)
    if os.path.exists(file_path):
        zip_file = f"{file}.zip"
        zip_path = os.path.join(path, zip_file)
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipp:
            zipp.write(file_path, file)
            print(f"Archivo {file} comprimido en {zip_file}.")
            return zip_file
    else:
        print(f"El archivo {file} no existe en el directorio {path}.")
    return None


def unzip_file(path: str, file: str):
    file_path = os.path.join(path, file)
    if os.path.exists(file_path):
        zip_path = os.path.join(path, file)
        with zipfile.ZipFile(zip_path) as zipp:
            zipp.extractall(path)
            print(f"Archivo {file} descomprimido en {path}.")
    else:
        print(f"El archivo {file} no existe en el directorio {path}.")


path = os.path.dirname(os.path.abspath(__file__))
file = "notasComprimir.txt"
zip = zip_file(path, file)

if zip != None:
    # Borro el fichero original antes de descomprimir el zip
    os.remove(os.path.join(path, file))
    unzip_file(path, zip)
