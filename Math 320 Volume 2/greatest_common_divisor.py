# Exercise 1.51
def gcd(n,d):
    print(n,d)
    q=0
    r=0
    counter = 0
    if(abs(n)<abs(d) or n==0):
        c=n
        n=d
        d=c
    if(d==0):
        G_C_D =  abs(n)
    elif(n<0) and (d>0):
        while((d*q) >= n):
            q-=1
        
        r=n-(d*q)
        print(f'{n}={q}*{d} + {r}')
        G_C_D = gcd(d,r)
    elif(n<0) and (d<0):
        while ((d*q)>=n):
            q+=1
        
        r=n-(d*q)
        print(f'{n}={q}*{d} + {r}')
        G_C_D =  gcd(d,r)

    elif(n>0) and (d<0):
        while ((d*q)<=n):
            q-=1
        q+=1
        r=n-(d*q)
        print(f'{n}={q}*{d} + {r}')
        G_C_D = gcd(d,r)
    
    else:
        q=int(n/d)
        r=n%d
        print(f'{n}={q}*{d} + {r}')
        G_C_D = gcd(d,r)
    
    return G_C_D

def euclid(a,b):
    """Code up the extended Euclidean algorithm from scratch, without importing any additional libraries or methods. Return gcd(a,b)
    as well as x, y, satisfying ax + by = gcd(a,b).

    Inputs: a, b

    Outputs: gcd(a,b), x, y

    """
    
    switched_ab = False
    if(abs(a)-abs(b)) < 0:
        #print("switching a,b")
        c=a
        a=b
        b=c
        switched_ab = True
    alt0 = False
    if(a<0):
        a*=-1
        #print("a<0")
        alt0 = True
    blt0 = False
    if b <0:
        #print("b<0")
        blt0=True
        b*=-1
    q, r = -1, -1
    #arrs = [a,b]
    queues = []
    #ayys = []
    #beez = []
    while r != 0:
        q = int(a/b)
        queues.append(q)
        r=a%b
        #arrs.append(r)
        #ayys.append(a)
        #beez.append(b)
        a=b
        b=r
        #print(f'a:{a}, b:{b}, r:{r}')
    if a< 0:
        a*=-1
    '''print(f'arrs: {arrs}')
    print(f'ayys: {ayys}')
    print(f'beez: {beez}')
    print(f'queues: {queues}')'''
    i =1
    queues = queues[::-1]
    y=1
    x=queues[1]*-1
    #print(len(queues))
    while i+2<len(queues):
        #print(f'x:{x}, y:{y}, queues[i+1]:{queues[i+1]}')
        y-=x*queues[i+1]
        #print(f'x:{x}, y:{y}, queues[i+2]:{queues[i+2]}')
        x-=y*queues[i+2]
        i+=2
    #print(f'x:{x}, y:{y}, queues[i]:{queues[i]}')
    if(len(queues)%2 != 0):
        #print("entered final y update")
        y-=x*queues[-1]
    else:
        switched_ab = not switched_ab
    #print(f'{a} = {ayys[-2]} - {beez[-2]} * {queues[-2]}: {a == ayys[-2] - beez[-2] * queues[-2]}')

    if alt0:
        x*=-1
    if blt0:
        y*=-1


    if(switched_ab):
        #print("switching x,y")
        return a, y, x
    return a, x, y



if __name__ == "__main__":
    # You can run test code in this block
    a=int(input("enter a: "))
    b = int(input('enter b: '))

    print(f'GCD({a}, {b}): {gcd(a,b)}')
    G_C_D, x, y = euclid(a,b)
    print(f'GCD({a}, {b}) = {G_C_D} and {G_C_D} = {a}*{x} + {b}*{y}: {G_C_D == a*x + b*y}')
