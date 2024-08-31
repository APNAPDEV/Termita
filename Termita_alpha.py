#Codigo de Termita
import time
import subprocess
import winreg
import colorama

pre1 = input(colorama.Fore.BLUE + "Bienvenido al software Termita este software esta diseñado para desistalar cualquier programa o aplicacion  de su dispositivo pulse 1 para continuar" + colorama.Style.RESET_ALL)
if pre1 == "1" :
    print(colorama.Fore.RED + "Error" + colorama.Style.RESET_ALL)
    segundos = 3
    while segundos > 0:
        time.sleep(1)
        segundos -= 1
        pre2 = input(colorama.Fore.YELLOW + "Termita necesita ejecutarse como administrador, estos permisos seran retirados al finalizar la operación para darselos pulse 1" + colorama.Style.RESET_ALL)
        if pre2 == "1" : 
                print(colorama.Fore.BLUE +"Reintentando"+ colorama.Style.RESET_ALL)
        segundos = 3
        while segundos > 0:
                print(segundos)
                time.sleep(1)
                segundos -= 1
                if segundos == 0 :
                    print(colorama.Fore.GREEN +"Analizando dispositivo le pedimos que no lo desconecte"+ colorama.Style.RESET_ALL)
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
                                        print(colorama.Fore.BLUE + f"{nombre_aplicacion} ha sido desinstalada." + colorama.Style.RESET_ALL)
                                        return
                            except FileNotFoundError:
                                continue
                        
                        winreg.CloseKey(clave)
                        print(colorama.Fore.RED +  f"No se encontró la aplicación: {nombre_aplicacion}" + colorama.Style.RESET_ALL )

                    if __name__ == "__main__":
                        print(colorama.Fore.BLUE + "Aplicaciones instaladas:" + colorama.Style.RESET_ALL)
                        aplicaciones = listar_aplicaciones()
                        for app in aplicaciones:
                            print(app)
                        
                        app_a_desinstalar = input( colorama.Fore.YELLOW + "Ingrese el nombre de la aplicación a desinstalar: " + colorama.Style.RESET_ALL)
                        desinstalar_aplicacion(app_a_desinstalar) 
                    ultima_var = input(colorama.Fore.BLUE + "Pulse cualquier tecla para cerrar la consola" + colorama.Style.RESET_ALL)
    
    
    
    
    
        else :
            exit()

else :
    exit()