from colorama import Fore, Style, Back, init

# Puedes descomentar la linea para no tener que hacer Reset a cada momento
#init(autoreset=True)

# Color del texto
print(Fore.GREEN + "Hola Mundo")
print("Una prueba")
print("Otra prueba")

# Color de fondo
print(Back.WHITE + "Verde con fondo blanco")
print("Más texto",  sep='', end='')
print(Style.RESET_ALL)

# Tonos de color
print(Style.DIM + "Texto en dim")
print(Style.NORMAL + "Texto en normal")
print(Style.BRIGHT + "Texto en bright")

# Prueba de tonos en verde
print(Fore.GREEN)
print(Style.DIM + "Texto en dim")
print(Style.NORMAL + "Texto en normal")
print(Style.BRIGHT + "Texto en bright")


print(Style.RESET_ALL)