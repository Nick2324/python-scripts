#! /usr/bin/python3.2


def esPalindromo(cadena):
    lcadena = len(cadena)
    for i in range(lcadena):
        if cadena[i] is not cadena[-(i + 1)]:
            return False
    return True


def main():
    if esPalindromo(input()):
        print ("Es palindromo")
    else:
        print ("No es palindromo")

if __name__ == '__main__':
    main()
