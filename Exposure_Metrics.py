from Prefix_Metrics import position_bias
import math
import numpy as np


def Measuring_fairness (Group,Rel,metric_func:str):
    if metric_func.upper() == "DTD":
        func = DTD
    elif metric_func.upper() == "DTR":
        func = DTR
    elif metric_func.upper() == "DID":
        func = DID
    elif metric_func.upper() == "DIR":
        func = DIR

    Metric_list_per_ranking_nbr = list()
    for i in Rel:
        # print("Ranking nbr ",i)
        sub_l = list()
        for j in i:
            # print("++++++++++++++++++++++++++++++",j)
            sub_l.append(func(Group, j))
        Metric_list_per_ranking_nbr.append(sub_l)

    return [np.mean(i) for i in Metric_list_per_ranking_nbr]



    ######## Exposure ######
def Exp(l,G):
    b_indices = [position_bias(i+1) for i, x in enumerate(l) if x == G] #this computes the b(r-1(d))
    nr_G = l.count(G)
    #print("nr_g",nr_G)
    return sum(b_indices)/nr_G

def ED(l):
    return Exp(l,1)-Exp(l,0)


def ER(l):
    return Exp(l,1)/Exp(l,0)


#Test
#l = [0,0,0,1]
#print("ER = ",ER(l))
#print("ED =", ED(l))

########### Ground Truth Relevance Y(G) ################

def Y(l,G,y):
    nr_G = l.count(G)
    return sum([y[i] for i in range(0,len(y)) if l[i] == G])/nr_G

def DTD(l,y):
    #try:
    return (Exp(l,1)/Y(l,1,y)) - (Exp(l,0)/Y(l,0,y))
    #except:
    #    return 0


def DTR(l,y):
    return (Exp(l,1)/Exp(l,0)) * (Y(l,0,y)/Y(l,1,y))

def CTR(l,G,y):
    b_indices_y = [position_bias(i+1)*y[i] for i, x in enumerate(l) if x == G] #this computes the b(r-1(d))
    nr_G = l.count(G)
    return sum(b_indices_y)/nr_G


def DID(l,y):
    #print("DID_non_prot=",CTR(l,1,y)/Y(l,1,y))
    #print("DID_prot=",CTR(l,0,y)/Y(l,0,y))
    return (CTR(l,1,y)/Y(l,1,y)) - (CTR(l,0,y)/Y(l,0,y))


def DIR (l,y):
    return (CTR(l,1,y)/CTR(l,0,y)) * (Y(l,0,y)/Y(l,1,y))


#y = [1,1,1,1]
#l = [0,1,0,1]

#print("ED :",ED(l))
#print("DID :",DID(l,y))

#print("ER :", ER(l))
#print("DIR :",DIR(l,y))


#function that helps to count psp
def occ(l,G): ## counts the nbr of occurence of element G starting from index i+1
    indices = [j for j, x in enumerate(l) if x == G]
    if G==1:
        sum_count = sum([l[j:len(l)].count(0) for j in indices])
    elif G==0:
        sum_count = sum([l[j:len(l)].count(1) for j in indices])
    return sum_count


def PSP(l):
   return (occ(l,1) - occ(l,0))/(l.count(0)*l.count(1))


s  = [0,1,0,0,1]

#print("PSP: ",PSP(s))

