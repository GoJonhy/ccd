# Main 
import os
import sys, zlib
from random import choices
import math
#from lib.FontGenerator import FontGenerator

def markovGeneretor(transationProb: float,state: int) -> int:
        prob_jump_previous_state=(transationProb/3);
        prob_jump_next_state=(transationProb/3);
        prob_stay_state=(transationProb/3);

        prob_double_jump_next_state=((1-transationProb)/2);
        prob_double_jump_previous_state=((1-transationProb)/2);
        jump_state=['previous','next','stay','double_previous','double_next'];
        probabilities=[prob_jump_previous_state,prob_jump_next_state,prob_stay_state,prob_double_jump_next_state,prob_double_jump_previous_state];

        step=''.join(choices(jump_state, probabilities));
        switcher = {
            'previous': state-1,
            'next': state+1,
            'stay': state,
            'double_previous': state-2,
            'double_next': state+2
        };
        state = switcher.get(step)
        if state < 0 :
            state =  state + 256;
        elif state > 255 :
            state =  state - 256;
        #print (step)
        return state;

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

# Criar array auxiliar [linha|estado][coluna|simbolo]
def create2DArray():
    return [[0] * 256 for i in range(256)]

def main(argv):
    state = 255;
    prob = 0.5;
    resultset=''

    lenght=2000;

    byte2DArray = create2DArray();

    total=0;

    while(True):
        prev_state = state
        state=markovGeneretor(prob,state);
        resultset += str(state) ;
        if(prev_state != None):
            byte2DArray[prev_state][state] += 1
        total += 1
        if total >= lenght:
            break
    
    print (resultset)
    #compressed=zlib.compress(resultset.encode());
    entropia = entropyCalc1Markov(byte2DArray);
    
    #print ("Size of original string:",sys.getsizeof(resultset))
    #print ("Size of compressed string:",sys.getsizeof(compressed))
    
    #print("Entropia 1ª Ordem Markov: ", entropia)

if __name__ == "__main__":
    main(sys.argv[1:])