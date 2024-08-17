
#Complementos del codigo para color usar Fore.color + variable + Style.RESET_ALL

from colorama import Fore,Style, init 
import time
import random
import winreg

#Codigo de Termita

pre1 = input( Fore.BLUE + "Bienvenido al asistente de Termita para más datos pulse 1 y para ejecutar el programa pulse 2" + Style.RESET_ALL)
if pre1 == "1" :
    print("Termita es software de desistalacion que a diferencia de otros es capaz de evadir los sitemas de algunas aplicaciones para no ser desistaladas")
    pre2 = input("Si quiere saber más sobre la politica de este software pulse 1 si quiere ejecutar Termita pulse 2")
    if pre2 == "1" :
        print("Termita va atener acceso a los archivos de su dispositivo y va a poder modificarlos")
        pre3 = input("Pulse 1 para ejecutar Termita o pulse 2 para cerrarlo")
        if pre3 == "1" :
            print(Fore.RED + "Error" + Style.RESET_ALL)
        segundos = 3
        while segundos > 0:
            time.sleep(1)
            segundos -= 1
            pre4 = input("Termita necesita ejecutarse como administrador, estos permisos seran retirados al finalizar la operación para darselos pulse 1 para cerrar Termita pulse 2 ")
            if pre4 == "1" : 
                print(Fore.BLUE + "Reintentando" + Style.RESET_ALL)
                segundos = 3
            while segundos > 0:
                print(segundos)
                time.sleep(1)
                segundos -= 1
                if segundos == 0 :
                    print(Fore.BLUE + "analizando dispositivo le pedimos que no lo desconecte" + Style.RESET_ALL)
                    segundos = 3
                    while segundos > 0:
                        time.sleep(1)
                        segundos -= 1
                    def get_installed_apps():
                        apps = []
                        uninstall_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key_path) as uninstall_key:
                            for i in range(winreg.QueryInfoKey(uninstall_key)[0]):
                                subkey_name = winreg.EnumKey(uninstall_key, i)
                                with winreg.OpenKey(uninstall_key, subkey_name) as subkey:
                                    try:
                                        app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                        apps.append(app_name)
                                    except FileNotFoundError:
                                        continue
                        return apps

                    if __name__ == "__main__":
                        installed_apps = get_installed_apps()
                        for app in installed_apps:
                            print(app)
                    var1 = input("Gracias por usar Termita")



            else :
               pass
        else:
            print(Fore.RED + "Error" + Style.RESET_ALL)
            segundos = 3
            while segundos > 0:
                time.sleep(1)
                segundos -= 1
            pre5 = input("Termita necesita ejecutarse como administrador, estos permisos seran retirados al finalizar la operación para darselos pulse 1 para cerrar Termita pulse 2 ")
            if pre5 == "1" : 
                print(Fore.BLUE + "Reintentando" + Style.RESET_ALL)
                segundos = 3
            while segundos > 0:
                print(segundos)
                time.sleep(1)
                segundos -= 1

            if segundos == 0 :
                print(Fore.BLUE + "analizando dispositivo le pedimos que no lo desconecte " + Style.RESET_ALL)
                segundos = 3
                while segundos > 0:
                    time.sleep(1)
                    segundos -= 1
                def get_installed_apps():
                    apps = []
                    uninstall_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key_path) as uninstall_key:
                        for i in range(winreg.QueryInfoKey(uninstall_key)[0]):
                            subkey_name = winreg.EnumKey(uninstall_key, i)
                            with winreg.OpenKey(uninstall_key, subkey_name) as subkey:
                                try:
                                    app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                    apps.append(app_name)
                                except FileNotFoundError:
                                    continue
                    return apps

                if __name__ == "__main__":
                    installed_apps = get_installed_apps()
                    for app in installed_apps:
                        print(app)

                var2 = input("Gracias por usar Termita")
else :
        print(Fore.RED + "Error" + Style.RESET_ALL)
        segundos = 3
        while segundos > 0:
            time.sleep(1)
            segundos -= 1
        pre6 = input("Termita necesita ejecutarse como administrador, estos permisos seran retirados al finalizar la operación para darselos pulse 1 para cerrar Termita pulse 2 ")
        if pre6 == "1" : 
            print(Fore.BLUE + "Reintentando" + Style.RESET_ALL)
            segundos = 3
        while segundos > 0:
            print(segundos)
            time.sleep(1)
            segundos -= 1

            if segundos == 0 :
                print(Fore.BLUE + "analizando dispositivo le pedimos que no lo desconecte" + Style.RESET_ALL)
                segundos = 3
                while segundos > 0:
                    time.sleep(1)
                    segundos -= 1
                def get_installed_apps():
                    apps = []
                    uninstall_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key_path) as uninstall_key:
                        for i in range(winreg.QueryInfoKey(uninstall_key)[0]):
                            subkey_name = winreg.EnumKey(uninstall_key, i)
                            with winreg.OpenKey(uninstall_key, subkey_name) as subkey:
                                try:
                                    app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                    apps.append(app_name)
                                except FileNotFoundError:
                                    continue
                    return apps

                if __name__ == "__main__":
                    installed_apps = get_installed_apps()
                    for app in installed_apps:
                        print(app)
                