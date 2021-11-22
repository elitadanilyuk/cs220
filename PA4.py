import itertools
import sys

def make_postage(money) :
    if money == 8:
        return (1,1)
    
    f,t = make_postage(money - 1)
        
    if f > 0:
        return (f-1, t+2)
    else:
        return (f+2, t-3)

def permutations(s) :
    return{i for i in itertools.permutations(s)}

if __name__=='__main__' :
    print("change for ", sys.argv[1], " : ", make_postage(int(sys.argv[1])))
    print("permutations:  ", permutations((1, 2)))