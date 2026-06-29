def calcular_minimo_ingredientes(ingredientes_valores, target):
    dp = [float('inf')] * (target + 1)
    historico_escolhas = [-1] * (target + 1)
    
    dp[0] = 0

    for i in range(1, target + 1):
        for valor in ingredientes_valores:
            if i - valor >= 0 and dp[i - valor] + 1 < dp[i]:
                dp[i] = dp[i - valor] + 1
                historico_escolhas[i] = valor

    if dp[target] == float('inf'):
        return None, []

    ingredientes_ideais = []
    peso_aux = target
    while peso_aux > 0:
        ingrediente_usado = historico_escolhas[peso_aux]
        ingredientes_ideais.append(ingrediente_usado)
        peso_aux -= ingrediente_usado

    return dp[target], ingredientes_ideais