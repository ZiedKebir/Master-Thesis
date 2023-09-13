import math
from Position_bias import *
from Loading_param import *
import numpy as np


def Measuring_quality (Rankings,metric_func:str, d):
    if metric_func.upper() == "CG":
        func = CG
    elif metric_func.upper() == "DCG":
        func = DCG
    elif metric_func.upper() == "NDCG":
        func = NDCG
    elif metric_func.upper() == "PRECISION":
        func = precision_at_k
    elif metric_func.upper() == "RECALL":
        func = recall_at_k
    elif metric_func.upper() == "AVERAGE_PRECISION":
        func = average_precision_at_k
    elif metric_func.upper() == "MRR":
        func = MRR

    Metric_list_per_ranking_nbr = list()
    for i in Rankings:
        #print("Ranking nbr ",i)
        sub_l = list()
        for j in i:
            #print("++++++++++++++++++++++++++++++",j)
            sub_l.append(func(j, d))
        Metric_list_per_ranking_nbr.append(sub_l)

    return [np.mean(i) for i in Metric_list_per_ranking_nbr]





def CG(y,d:dict): #The DCG accumulated at a particular rank position p is defined as:
    # y is the list containing the releveance score
    return sum([y[i] for i in range(0,round(float(d["pos"])*int(d["Ranking_length"])))])





def DCG(y,d:dict): #The DCG accumulated at a particular rank position p is defined as:
    # y is the list containing the releveance score

    bias_func = Position_bias(d)
    return sum([y[i-1]*bias_func(i) for i in range(1,round(float(d["pos"])*int(d["Ranking_length"]))+1)])




def NDCG(y,d):
    y_s = sorted(y,reverse = True)
    #print(DCG(y_s,d))
    return DCG(y,d)/DCG(y_s,d)



def MRR(y,d):
    return sum([y[i]/(i+1) for i in range(0,len(y))])/len(y)


def precision_at_k(y, d:dict):
    # the parameter k is the same as the parameter pos in the file
    rel_thresh = np.mean(y) #an item is considered relevant if the relevance score is greater than the average relevance score
    k = float(d["pos"])
    return sum([1 if y[rel_pos]>rel_thresh else 0 for rel_pos in range(0,round(len(y)*k))])/round(len(y)*k)


def precision_at_k_with_len(y, d:dict):
    ## This precision is computed using an integer K value not a proportion like in the previous method
    # the parameter k is the same as the parameter pos in the file
    rel_thresh = np.mean(y) #an item is considered relevant if the relevance score is greater than the average relevance score
    K = d["K"]
    return sum([1 if y[rel_pos]>rel_thresh else 0 for rel_pos in range(0,int(K))])/K





def recall_at_k(y, d): #d: dictionary that containes the parameters
    # the parameter k is the same as the parameter pos in the file
    rel_thresh = np.mean(y) #an item is considered relevant if the relevance score is greater than the average relevance score
    k = float(d["pos"])
    count_rel = sum([1 if rel>rel_thresh else 0 for rel in y])
    return sum([1 if y[rel_pos]>rel_thresh else 0 for rel_pos in range(0,round(len(y)*k))])/count_rel




def average_precision_at_k(y, d):
    # y: a list of binary relevance judgments (1 for relevant, 0 for non-relevant)

    K = int(d["K"])
    precision = 0
    for i in range(1,K+1):
        d["K"] = i
        print(d["K"])
        precision += precision_at_k_with_len(y,d)
    return precision/K

