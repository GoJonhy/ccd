import sys, os
import random

def main(argv):

    stdout = os.fdopen(sys.stdout.fileno(), 'wb')
    outputSize=716288;
    betSize=7;
    index=1;totalSize=0;
    betnumber = list();betstar=list();
    while(True):
        if(index>=betSize):
            totalSize+=index;
            if(totalSize>outputSize-7):
                break;
            index=0;
            betnumber.clear();
            betstar.clear();
        if(index<=5):
            number=random.randrange(1,50);
            if(betnumber.count(number)==0):
                betnumber.append(number);
                index+=1;
        else:
            number=random.randrange(1,12);
            if(betstar.count(number)==0):
                betstar.append(number);
                index+=1;
        #print(number)
        stdout.write(number.to_bytes(1, byteorder="big"));
        #print(number.to_bytes(1, byteorder="big"));

if __name__ == "__main__":
    main(sys.argv[1:])