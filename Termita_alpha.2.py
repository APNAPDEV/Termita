#Codigo de Termita

from colorama import Fore,Style, init
import time
import random
import os
import subprocess
import winreg

#Complementos del codigo para color usar Fore.color + variable + Style.RESET_ALL

#codigo en bruto
#Presentacion + permisos de admministrador
pre1 = input( Fore.BLUE + "Bienvenido al software Termita este software esta diseñado para desistalar cualquier programa o aplicacion de su dispositivo pulse 1 para continuar" + Style.RESET_ALL)
if pre1 == 1 :
    print(Fore.RED + "Error" + Style.RESET_ALL)
    segundos = 3
    while segundos > 0:
        time.sleep(1)
        segundos -= 1
        pre2 = input(Fore.YELLOW + "Termita necesita ejecutarse como administrador, estos permisos seran retirados al finalizar la operación para darselos pulse 1" + Style.RESET_ALL)
        if pre2 == 1 : 
                print(Fore.BLUE + "Reintentando" + Style.RESET_ALL)
        segundos = 3
        while segundos > 0:
                print(segundos)
                time.sleep(1)
                segundos -= 1
                if segundos == 0 :
                    print(Fore.GREEN + "Analizando dispositivo le pedimos que no lo desconecte" + Style.RESET_ALL)
                    segundos = 3
                    while segundos > 0:
                        time.sleep(1)
                        segundos -= 1
                    def listar_aplicaciones():
                        aplicaciones = []
                        clave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
                        
                        for i in range(winreg.QueryInfoKey(clave)[0]):
                            try:
                                subclave = winreg.EnumKey(clave, i)
                                subclave_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\\' + subclave
                                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subclave_path) as app_clave:
                                    nombre = winreg.QueryValueEx(app_clave, 'DisplayName')[0]
                                    aplicaciones.append(nombre)
                            except FileNotFoundError:
                                continue
                        
                        winreg.CloseKey(clave)
                        return aplicaciones
                
                    def desinstalar_aplicacion(nombre_aplicacion):
                        clave = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
                        
                        for i in range(winreg.QueryInfoKey(clave)[0]):
                            try:
                                subclave = winreg.EnumKey(clave, i)
                                subclave_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\\' + subclave
                                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subclave_path) as app_clave:
                                    nombre = winreg.QueryValueEx(app_clave, 'DisplayName')[0]
                                    if nombre == nombre_aplicacion:
                                        uninstall_string = winreg.QueryValueEx(app_clave, 'UninstallString')[0]
                                        subprocess.call(uninstall_string, shell=True)
                                        print(Fore.YELLOW + f"{nombre_aplicacion} ha sido desinstalada." + Style.RESET_ALL)
                                        return
                            except FileNotFoundError:
                                continue
                        
                        winreg.CloseKey(clave)
                        print(Fore.RED + f"No se encontró la aplicación: {nombre_aplicacion}" + Style.RESET_ALL)

                    if __name__ == "__main__":
                        print(Fore.LIGHTBLUE_EX + "Aplicaciones instaladas:" + Style.RESET_ALL)
                        aplicaciones = listar_aplicaciones()
                        for app in aplicaciones:
                            print(app)
                        
                        app_a_desinstalar = input(Fore.BLUE + "Ingrese el nombre de la aplicación a desinstalar: " + Style.RESET_ALL)
                        desinstalar_aplicacion(app_a_desinstalar) 
                    ultima_var = input(Fore.BLUE + "Pulse cualquier tecla para cerrar la consola" + Style.RESET_ALL)
    
    
    
    
    
        else :
            exit()

else :
    exit()