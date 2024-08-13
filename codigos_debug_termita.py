import os
import subprocess

def listar_aplicaciones():
    # Comando para listar aplicaciones en Windows
    comando = "wmic product get name"
    aplicaciones = subprocess.check_output(comando, shell=True, text=True)
    return aplicaciones.splitlines()

def desinstalar_aplicacion(nombre_aplicacion):
    # Comando para desinstalar la aplicación
    comando = f"wmic product where name='{nombre_aplicacion}' call uninstall"
    subprocess.call(comando, shell=True)

def main():
    print("Listando aplicaciones instaladas...")
    aplicaciones = listar_aplicaciones()
    
    # Filtrar aplicaciones vacías y enumerar
    aplicaciones = [app for app in aplicaciones if app.strip()]
    for i, app in enumerate(aplicaciones, start=1):
        print(f"{i}. {app.strip()}")

    # Solicitar al usuario que elija una aplicación
    try:
        seleccion = int(input("Ingrese el número de la aplicación que desea desinstalar: "))
        if 1 <= seleccion <= len(aplicaciones):
            app_a_desinstalar = aplicaciones[seleccion - 1].strip()
            print(f"Desinstalando {app_a_desinstalar}...")
            desinstalar_aplicacion(app_a_desinstalar)
            print("Aplicación desinstalada con éxito.")
        else:
            print("Número de aplicación no válido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()