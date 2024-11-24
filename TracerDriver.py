import subprocess
import time 
import colorama



def listar_drivers_activos():
    try:
        # Ejecutamos el comando 'driverquery' para obtener la lista de drivers
        resultado = subprocess.run(['driverquery'], capture_output=True, text=True, check=True)
        
        # Mostramos la salida del comando
        print(colorama.Fore.BLUE + "Drivers activos en el sistema:\n" + colorama.Style.RESET_ALL)
        print(colorama.Fore.BLUE + resultado.stdout + colorama.Style.RESET_ALL)
        
    except subprocess.CalledProcessError as e:
        print(colorama.Fore.RED + f"Ocurrió un error al intentar listar los drivers: {e}" + colorama.Style.RESET_ALL)

# Llamamos a la función
print( colorama.Fore.GREEN + "Analizando dispositivo, no lo desconecte..." + colorama.Style.RESET_ALL)
time.sleep(3)
print(listar_drivers_activos())
input(colorama.Fore.BLUE + "Pulse cualquier tecla para cerrar la consola." + colorama.Style.RESET_ALL)

