#!/usr/bin/python3
import sys


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # décrémentation pour éviter la boucle infinie
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <nombre>")
        sys.exit(1)

    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Erreur : l'argument doit être un entier.")
        sys.exit(1)
