# steve has a list of possible products, Paul has a list of possible sums. Find one product such that 

def find_products(s):
    products = []
    for i in range(2,int(s/2)):
        products.append(i*(s-i))
    return products

def find_factors(p):
    factors = []
    for i in range(2,p/2):
        if p % i == 0:
            factors.append(p)
    return factors


def find_sums(p):
    factors = find_factors(p)
    sums_list = []
    for i in range(len(factors)/2): #will range from 0 to the middle of the array
        sums_list.append(factors[i] + factors[len(factors)-i])
        


poss_sums=[11,17,23,27,29,35,37,41,47,51,53,57,59,65,67,71,77,79,83,87,89,93,95,97]



for sum in poss_sums:
    poss_products = []
    for sum in poss_sums:
        poss_products.append()
