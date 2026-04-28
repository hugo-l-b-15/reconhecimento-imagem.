def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros (list): Lista contendo números inteiros ou floats.
    
    Returns:
        tuple: Uma tupla contendo (total, media, maximo, minimo).
    
    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    
    # Calcula o total usando a função built-in sum()
    total = sum(numeros)
    
    # Calcula a média aritmética
    media = total / len(numeros)
    
    # Encontra o valor máximo usando a função built-in max()
    maximo = max(numeros)
    
    # Encontra o valor mínimo usando a função built-in min()
    minimo = min(numeros)
    
    return total, media, maximo, minimo


# Lista de números para análise
lista_numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Desempacota os resultados retornados pela função
total, media, maximo, minimo = calcular_estatisticas(lista_numeros)

# Exibe os resultados de forma clara
print("Total:  ", total)
print("Média:  ", media)
print("Máximo: ", maximo)
print("Mínimo: ", minimo)