def calcula_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
        
    return SOMA

resultado = calcula_soma()
print(f"O valor final de SOMA é: {resultado}")