import math

# Calculo de entropia para uma fonte de markov de 1 ordem
def entropyCalc1Markov(byte2DArray):
    entropy = 0
    countColum = [0] * 256
    countLines = [0] * 256
    line = 0
    for linha in byte2DArray:
        col = 0
        for sym in linha:
            countColum[col] += sym
            col += 1

            countLines[line] += sym

        line += 1

    counTotal = 0
    for v in countColum:
        counTotal += v

    line = 0
    for v in countColum:
        if(v != 0 and countLines[line] != 0):
            entropy += (v/counTotal) * \
                calcEntropy(byte2DArray[line], countLines[line])
        line += 1

    return entropy

# Calculo entropia passo
def calcEntropy(line, lineTotal):
    entropy = 0
    index = 0
    for state in line:
        if(state != 0 and lineTotal != 0):
            prob = (state/lineTotal)
            entropy += prob * math.log(1/prob, 2)
        index += 1
    return entropy
