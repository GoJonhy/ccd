import random

def betGenerator() -> bytearray:
    betlist = list();
    bet=bytearray(7);
    betSize=7;
    currentBetSize=0;
    while(True):
        if(currentBetSize>betSize):
            break;
        if(currentBetSize<=5):
            number=random.randrange(1,50)
        else:
            number=random.randrange(1,12)
        if(betlist.count(number)==0):
            betlist.append(number)
            currentBetSize+=1;
    bet=bytearray(betlist);
    #print("List:",betlist);
    return bet;