def calcular_minimo_ingredientes(ingredientes_valores, target):
    """
    Resolve o problema dos selos (Coin Change) usando Programação Dinâmica.
    Retorna uma tupla: (min_movimentos, lista_de_pesos_ideais)
    Retorna (None, []) se for impossível atingir o valor exato.
    """
    # Tabela para guardar o número mínimo de ingredientes para cada peso
    dp = [float('inf')] * (target + 1)
    # Tabela para rastrear o último ingrediente usado para chegar a cada peso
    historico_escolhas = [-1] * (target + 1)
    
    dp[0] = 0  # 0 movimentos para atingir peso 0

    # Preenche a tabela de PD
    for i in range(1, target + 1):
        for valor in ingredientes_valores:
            if i - valor >= 0 and dp[i - valor] + 1 < dp[i]:
                dp[i] = dp[i - valor] + 1
                historico_escolhas[i] = valor

    # Se o valor continuar infinito, não há solução
    if dp[target] == float('inf'):
        return None, []

    # Reconstrói a lista de ingredientes ideais de trás para frente
    ingredientes_ideais = []
    peso_aux = target
    while peso_aux > 0:
        ingrediente_usado = historico_escolhas[peso_aux]
        ingredientes_ideais.append(ingrediente_usado)
        peso_aux -= ingrediente_usado

    return dp[target], ingredientes_ideais