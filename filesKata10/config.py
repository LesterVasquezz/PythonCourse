def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No es posible encontrar el archivo config.txt")

    except IsADirectoryError:
        print("Encontramos el archivo config.txt, pero es un directorio y no es posible leerlo ")


if __name__ == '__main__':
    main()