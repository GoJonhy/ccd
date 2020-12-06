import math
# Estima a entropia associada ao ficheiro com base nas contagens fornecidas
def entropyCount(symList, byteTotal: int) -> float:
    entropy = 0
    for sym in symList:
        prob = sym[1]/byteTotal
        entropy += prob * math.log(1/prob, 2)
    return entropy

# Auto informaç~ao de um simbolo 
def selfInformation(prob: float) -> float:
    return math.log(1/prob, 2)