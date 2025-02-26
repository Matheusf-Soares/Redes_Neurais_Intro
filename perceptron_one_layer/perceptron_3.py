import numpy as np

entradas = np.array(
    [
        [0, 0], 
        [0, 1], 
        [1, 0], 
        [1, 1],
    ]
)

saidas = np.array([0, 1, 1, 1]) # Saida OR
# saidas = np.array([0, 1, 1, 0]) # Saida XOR
pesos = np.array([0.0, 0.0])
taxa_aprendizagem = 0.1

def step_function(soma):
    if (soma >= 1):
        return 1
    return 0

def calcula_saida(registro):
    s = registro.dot(pesos)
    return step_function(s)

def treinar():
    erro_total = 1
    while (erro_total != 0):
        erro_total = 0
        for i in range(len(saidas)):
            saida_calculada = calcula_saida(entradas[i])
            erro = abs(saidas[i] - saida_calculada)
            erro_total += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erro_total))

treinar()
print('Rede Neural Treinada')
print(pesos)

