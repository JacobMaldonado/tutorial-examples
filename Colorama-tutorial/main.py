from colorama import Fore, Style, Back, init

init(autoreset=True)

# Color de texto
print(Fore.YELLOW + "Esto es un Warning")
print(Fore.RED + "Esto es un Error")
print(Fore.GREEN + "Esto es un Texto exitoso")

# Color de fondo

print(Back.WHITE + "Esto es un fondo blanco")

print("Esto es más texto"+ Style.RESET_ALL)
print(Style.RESET_ALL)
print(Fore.RED + Back.GREEN + "Esto es una prueba" + Style.RESET_ALL)
print(Style.RESET_ALL)

# Tonos

print(Fore.RED + Style.DIM + "Esto es un texto tenue")
print(Fore.RED + Style.NORMAL + "Esto es un texto normal")
print(Fore.RED + Style.BRIGHT + "Esto es un texto brillante")
print(Fore.RED + Back.GREEN + Style.DIM + "Esto es una prueba" + Style.RESET_ALL)
print(Fore.RED + Back.GREEN + Style.NORMAL + "Esto es una prueba" + Style.RESET_ALL)
print(Fore.RED + Back.GREEN + Style.BRIGHT + "Esto es una prueba" + Style.RESET_ALL)
print(Style.RESET_ALL)

# Colores
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

