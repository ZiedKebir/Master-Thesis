import math
import itertools
import random

def position_bias(k): #compute the position bias
    return 1/math.log2(1+k)

def pG_k(l,k,G):  #list that contians the ranking
    return l[0:k].count(G)/k  #k is the cut-off (i first element in the ranking)
                      #G is the group type : protected or non-protected

######### Normalized Discount difference #####################

def fun_ND(l,I,G):
    ND_Z = 0
    pG1 = l.count(1) / len(l)
    for k in I:
        ND_Z += position_bias(k) * abs(pG_k(l, k, G) - pG1)
    return ND_Z


def fun_ZND(l:list,I:list,G):
    pG1 = l.count(1) / len(l)
    list_opt = list()
    l.sort(reverse=False)
    x = l.copy()
    list_opt.append(x)
    l.sort(reverse=True)
    list_opt.append(l)
    print("8888888",list_opt)
    Z_l = list()
    Z_l.append(fun_ND(list_opt[0],I,G))
    Z_l.append(fun_ND(list_opt[1], I, G))
    print("++++++",Z_l)
    return  max(Z_l)

def fun_rND(l,I):
    rND = 1 - (fun_ND(l, I, 1) / fun_ZND(l, I, 1))
    return rND


# 0: protected group ---> non discriminated
# 1: non-protected group ---> discriminated

#l = [1,0,1,1,0,0,0,0]
#I = [2,4,6,8]
#rND = fun_rND(l,I)

#print("rND =" ,rND)


######### Normalized Discount difference ###############

def fun_RD(l,I):
    RD_Z = 0
    PG0 = l.count(0) / len(l)
    PG1 = l.count(1) / len(l)
    for k in I:
        try:
            ratio = pG_k(l, k, 1) / pG_k(l, k, 0)
        except ZeroDivisionError:
            ratio = 0
        else:
            ratio = pG_k(l, k, 1) / pG_k(l, k, 0)
        RD_Z += abs(ratio-(PG1/PG0))*position_bias(k)
    return RD_Z




def fun_ZRD(l,I):
    PG0 = l.count(0) / len(l)
    PG1 = l.count(1) / len(l)
    list_opt = list()
    l.sort(reverse=False)
    x = l.copy()
    list_opt.append(x)
    l.sort(reverse=True)
    list_opt.append(l)
    Z_l = [fun_RD(list_opt[0],I),fun_RD(list_opt[1],I)]
    return max(Z_l)



def fun_rRD(l,I):
    rRD = 1 - fun_RD(l, I) / fun_ZRD(l, I)
    return rRD

#l = [0 for i in range(0,480)]
#I = [i for i in range(2,len(l)+2,2)]

#for i in range(0,round(len(l)*0.3)):
#    l[i] = 1
#l.reverse()
#print(l)


#rRD = fun_rRD(l,I)
#print("rRD =", rRD)


######### normalized Kullback-Leibler divergence (rKl) ###############

## ????



