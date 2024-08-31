#Codigo de Termita
import time
import subprocess
import winreg
from colorama import Fore, Back, Style, init
init(autoreset=True)
#Complementos del codigo para color usar Fore.color + variable + Style.RESET_ALL


pre1 = input("Bienvenido al software Termita este software esta diseñado para desistalar cualquier programa o aplicacion  de su dispositivo pulse 1 para continuar")
if pre1 == "1" :
    print("Error")
    segundos = 3
    while segundos > 0:
        time.sleep(1)
        segundos -= 1
        pre2 = input("Termita necesita ejecutarse como administrador, estos permisos seran retirados al finalizar la operación para darselos pulse 1")
        if pre2 == "1" : 
                print( "Reintentando")
        segundos = 3
        while segundos > 0:
                print(segundos)
                time.sleep(1)
                segundos -= 1
                if segundos == 0 :
                    print("Analizando dispositivo le pedimos que no lo desconecte" )
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
                                        print( f"{nombre_aplicacion} ha sido desinstalada.")
                                        return
                            except FileNotFoundError:
                                continue
                        
                        winreg.CloseKey(clave)
                        print( f"No se encontró la aplicación: {nombre_aplicacion}" )

                    if __name__ == "__main__":
                        print( "Aplicaciones instaladas:")
                        aplicaciones = listar_aplicaciones()
                        for app in aplicaciones:
                            print(app)
                        
                        app_a_desinstalar = input("Ingrese el nombre de la aplicación a desinstalar: ")
                        desinstalar_aplicacion(app_a_desinstalar) 
                    ultima_var = input("Pulse cualquier tecla para cerrar la consola")
    
    
    
    
    
        else :
            exit()

else :
    exit()