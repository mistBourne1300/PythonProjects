import numpy as np

def coin_toss():
    return np.random.choice([0,1])
    
def at_least_one_heads():
    toss = [coin_toss(), coin_toss()]
    while 1 not in toss:
        toss = [coin_toss(), coin_toss()]
    return toss
        

if __name__ == "__main__":
    two_heads = []
    for i in range(50000):
        toss=at_least_one_heads()
        print(toss)
        two_heads.append(sum(toss)==2)
    
    print(f'percent of tosses that are both heads: {sum(two_heads)/len(two_heads)}')
