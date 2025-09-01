#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("La factorielle n'est pas définie pour les entiers négatifs.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <entier>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)