def exponenciacion_binaria(M, e, n):
    C = 1
    M = M % n

    while e > 0:
        if e % 2 == 1:      # Si el bit actual del exponente es 1
            C = (C * M) % n
        
        M = (M * M) % n     # Cuadrado modular
        e = e // 2          # Desplazamiento del exponente en binario

    return C


# Programa principal
M = int(input("Base M: "))
e = int(input("Exponente e: "))
n = int(input("Modulo n: "))

resultado = exponenciacion_binaria(M, e, n)

print(f"\nResultado: {M}^{e} mod {n} = {resultado}")