 
import time
import subprocess
import winreg
import colorama

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
    print(colorama.Fore.RED + f"No se encontró la aplicación: {nombre_aplicacion}" + colorama.Style.RESET_ALL)

if __name__ == "__main__":
    colorama.init()
    print(colorama.Fore.BLUE + "Bienvenido al software Termita. Este software está diseñado para desinstalar cualquier programa o aplicación de su dispositivo. Pulse 1 para continuar." + colorama.Style.RESET_ALL)
    
    pre1 = input()
    if pre1 == "1":
        print(colorama.Fore.GREEN + "Analizando dispositivo, le pedimos que no lo desconecte." + colorama.Style.RESET_ALL)
        time.sleep(3)
        
        print(colorama.Fore.BLUE + "Aplicaciones instaladas:" + colorama.Style.RESET_ALL)
        aplicaciones = listar_aplicaciones()
        
        for index, app in enumerate(aplicaciones, start=1):
            print(f"{index}. {app}")
        
        app_num = int(input(colorama.Fore.YELLOW + "Ingrese el número de la aplicación a desinstalar: " + colorama.Style.RESET_ALL))
        
        if 1 <= app_num <= len(aplicaciones):
            desinstalar_aplicacion(aplicaciones[app_num - 1])
        else:
            print(colorama.Fore.RED + "Número de aplicación no válido." + colorama.Style.RESET_ALL)
        
        input(colorama.Fore.BLUE + "Pulse cualquier tecla para cerrar la consola." + colorama.Style.RESET_ALL)
    else:
        exit()