#!/usr/bin/env python3

# Módulos seguros para generación aleatoria 
import secrets
import string
import random
from typing import List

# Usamos SystemRandom para operaciones de mezcla 
_sysrand = random.SystemRandom()

# Longitud fija
PASSWORD_LENGTH = 10

def generar_contrasena(length: int = PASSWORD_LENGTH) -> str:
  
    if length < 4:
        raise ValueError("La longitud debe ser al menos 4 para incluir cada tipo de carácter.")

    # Conjuntos de caracteres
    mayusculas = string.ascii_uppercase             # ABC...Z
    minusculas = string.ascii_lowercase             # abc...z
    digitos = string.digits                         # 0123456789
    especiales = "!@#$%^&*()-_=+[]{};:,.<>?/|~"     # conjunto de especiales (se puede ajustar)

    # Seleccionar al menos un carácter de cada tipo
    password_chars: List[str] = [
        secrets.choice(mayusculas),
        secrets.choice(minusculas),
        secrets.choice(digitos),
        secrets.choice(especiales)
    ]

    # Combinar todos los conjuntos para llenar el resto de la contraseña
    todos = mayusculas + minusculas + digitos + especiales

    # Añadir caracteres aleatorios hasta alcanzar la longitud requerida
    while len(password_chars) < length:
        password_chars.append(secrets.choice(todos))

    # Mezclar la lista de caracteres de forma segura para que la posición de los obligatorios no sea predecible
    _sysrand.shuffle(password_chars)

    # Unir lista en string final
    contraseña = "".join(password_chars)
    return contraseña

def main():
    
    pwd = generar_contrasena()
    print(f'Nombre: Elian Erazo\nCarrera: ING. Ciberseguridad\nMateria: lógica de Programación\n\nSu contraseña segura es: {pwd}')

if __name__ == "__main__":
    main()
