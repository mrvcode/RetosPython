import os
import subprocess


def run_command(command: str):
    try:
        result = subprocess.run(
            command, shell=True, check=True, text=True, capture_output=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e.stderr}")


def show_current_directory():
    if os.name == "nt":  # Windows
        run_command("echo %cd%")
    else:  # Unix-like
        run_command("pwd")


def set_working_directory():
    path = input("Introduce la ruta del directorio de trabajo:\n")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"\nDirectorio de trabajo ha cambiado a:\n{path}")
    else:
        print("El directorio introducido no existe.")


def create_repository():
    if os.path.isdir(".git"):
        print("El repositorio ya existe.")
    else:
        run_command("git init")
        run_command("git branch -M main")
        print("Repositorio creado con éxito.")


def create_branch():
    branch_name = input("Nombre de la nueva rama: ")
    run_command(f"git branch {branch_name}")


def switch_branch():
    branch_name = input("Nombre de la rama a la que quieres cambiar: ")
    run_command(f"git checkout {branch_name}")


def show_pending_files():
    run_command("git status -s")


def make_commit():
    message = input("Introduce el mensaje del commit: ")
    run_command("git add .")
    run_command(f'git commit -m "{message}"')


def show_commit_history():
    run_command("git log --oneline")


def delete_branch():
    branch_name = input("Nombre de la rama a eliminar: ")
    run_command(f"git branch -d {branch_name}")


def list_remotes():
    print("\nRepositorios remotos configurados:")
    run_command("git remote -v")


def set_remote_repository():
    remote_url = input("Introduce la URL del repositorio remoto: ")
    # Verificar si 'origin' ya existe
    try:
        result = subprocess.run(
            "git remote -v", shell=True, check=True, text=True, capture_output=True
        )
        if "origin" in result.stdout:
            print("\n¿Quieres reemplazar el remoto existente? (s/n)")
            respuesta = input().lower()
            if respuesta == "s":
                run_command("git remote remove origin")
                run_command(f"git remote add origin {remote_url}")
                print("Remoto actualizado correctamente.")
            else:
                print("Operación cancelada.")
                return
        else:
            run_command(f"git remote add origin {remote_url}")
    except subprocess.CalledProcessError:
        run_command(f"git remote add origin {remote_url}")

    # Intentar establecer la rama upstream de forma segura
    try:
        run_command("git fetch")
        run_command("git branch --set-upstream-to=origin/main main")
    except:
        print("No se pudo establecer la rama upstream. Si deseas hacer push, utiliza:")
        print(f"git push -u origin main")


def make_pull():
    run_command("git pull")


def make_push():
    branch = subprocess.run(
        "git rev-parse --abbrev-ref HEAD",
        shell=True,
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()

    print(f"Haciendo push de la rama '{branch}'...")
    try:
        run_command(f"git push -u origin {branch}")
    except:
        print(
            f"Error al hacer push. Intenta manualmente con: git push -u origin {branch}"
        )


while True:
    print("\nDirectorio actual de trabajo:")
    show_current_directory()

    print("\nGit y GitHub CLI - Opciones:")
    print("1. Establecer el directorio de trabajo")
    print("2. Crear un nuevo repositorio")
    print("3. Crear una nueva rama")
    print("4. Cambiar de rama")
    print("5. Mostrar ficheros pendientes de hacer commit")
    print("6. Hacer commit (+add)")
    print("7. Mostrar el historial de commits")
    print("8. Eliminar rama")
    print("9. Establecer/Actualizar repositorio remoto")
    print("10. Listar repositorios remotos")
    print("11. Hacer pull")
    print("12. Hacer push")
    print("13. Salir")

    choice = input("Selecciona una opción (1 al 13): ")

    match choice:
        case "1":
            set_working_directory()
        case "2":
            create_repository()
        case "3":
            create_branch()
        case "4":
            switch_branch()
        case "5":
            show_pending_files()
        case "6":
            make_commit()
        case "7":
            show_commit_history()
        case "8":
            delete_branch()
        case "9":
            set_remote_repository()
        case "10":
            list_remotes()
        case "11":
            make_pull()
        case "12":
            make_push()
        case "13":
            print("Salir")
            break
        case _:
            print("Opción no válida")
