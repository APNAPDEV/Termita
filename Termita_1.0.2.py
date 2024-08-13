#Complementos del codigo para color usar Fore.color + variable + Style.RESET_ALL

from colorama import Fore,Style, init
import time
import random
import os
import subprocess

#Codigo de Termita
pre1 = input( Fore.BLUE + "Bienvenido al software Termita este software esta diseñado para desistalar cualquier programa o aplicacion de su dispositivo pulse 1 para continuar" + Style.RESET_ALL)
if pre1 == "1" :
    print(Fore.RED + "Error" + Style.RESET_ALL)
segundos = 3
while segundos > 0:
    time.sleep(1)
    segundos -= 1
    pre2 = input(Fore.YELLOW + "Termita necesita ejecutarse como administrador, estos permisos seran retirados al finalizar la operación para darselos pulse 1" + Style.RESET_ALL)
    if pre2 == "1" : 
            print(Fore.BLUE + "Reintentando" + Style.RESET_ALL)
    segundos = 3
    while segundos > 0:
            print(segundos)
            time.sleep(1)
            segundos -= 1
            if segundos == 0 :
                print(Fore.BLUE + "Analizando dispositivo le pedimos que no lo desconecte" + Style.RESET_ALL)
                segundos = 3
                while segundos > 0:
                    time.sleep(1)
                    segundos -= 1
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
                    print(Fore.GREEN + "Listando aplicaciones instaladas..." + Style.RESET_ALL)
                    aplicaciones = listar_aplicaciones()
                    
                    # Filtrar aplicaciones vacías y enumerar
                    aplicaciones = [app for app in aplicaciones if app.strip()]
                    for i, app in enumerate(aplicaciones, start=1):
                        print(f"{i}. {app.strip()}")

                    # Solicitar al usuario que elija una aplicación
                    try:
                        seleccion = int(input(Fore.BLUE + "Ingrese el número de la aplicación que desea desinstalar: " + Style.RESET_ALL ))
                        if 1 <= seleccion <= len(aplicaciones):
                            app_a_desinstalar = aplicaciones[seleccion - 1].strip()
                            print(f"Desinstalando {app_a_desinstalar}...")
                            desinstalar_aplicacion(app_a_desinstalar)
                            print("Aplicación desinstalada con éxito.")
                        else:
                            print(Fore.RED + "Número de aplicación no válido." + Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED + "Por favor, ingrese un número válido." + Style.RESET_ALL )

                if __name__ == "__main__":
                    main()

    else :
        pass

else :
    pass