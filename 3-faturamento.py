import json

def analisa_faturamento(faturamento_diario):
    faturamento_validos = [item['valor'] for item in faturamento_diario if item['valor'] > 0]
    
    if not faturamento_validos:
        return "Não há faturamento válido para análise."

    menor_faturamento = min(faturamento_validos)
    
    maior_faturamento = max(faturamento_validos)
    
    total_faturamento = sum(faturamento_validos)
    dias_validos = len(faturamento_validos)
    media_mensal = total_faturamento / dias_validos
    
    dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }

def carregar_dados_json(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
        return dados['faturamento']

faturamento_diario = carregar_dados_json('faturamento.json')

resultado = analisa_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: R${resultado['menor_faturamento']:.2f}")
print(f"Maior valor de faturamento: R${resultado['maior_faturamento']:.2f}")
print(f"Número de dias acima da média mensal: {resultado['dias_acima_media']}")