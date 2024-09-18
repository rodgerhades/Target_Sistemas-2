def inverter_string(s):
    resultado = ""
    
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

string_original = "exemplo"

string_invertida = inverter_string(string_original)

print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")