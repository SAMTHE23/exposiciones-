class EdadError(Exception):
    pass

try:
    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        raise EdadError("La edad no puede ser negativa")

    if edad < 18:
        raise EdadError("Debes ser mayor de edad")

    print("Puedes ingresar")

except EdadError as error:
    print("Error:", error)

except ValueError:
    print("Debes ingresar un número")