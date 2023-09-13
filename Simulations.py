import random
from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import random
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.stats import skewnorm
from Distributions import Distribution
from Loading_param import *
from Exposure_Metrics import Measuring_fairness
from Quality_metrics import Measuring_quality

def generate_r(param):  # p represent the proportion of protected group individuals in the ranking
    # f is fairness probability (see paper Measuring Fairness in Ranked Outputs)
    # n is the size of the ranking
    # When f > 0.5, members of the protected group (1) are preferred
    l = [0 if random.random() > float(param["Proportion_of_protected_group"]) else 1 for i in range(0, int(param["Ranking_length"]))]
    s_prot = [i for i in l if i == 1]
    s_non_prot = [i for i in l if i == 0]
    r = list()
    while (len(s_prot) != 0 and len(s_non_prot) != 0):
        x = random.random()
        if x < float(param["Fairness_level"]):
            s_prot.pop()
            r.append(1)
        else:
            s_non_prot.pop()
            r.append(0)
    r = r + s_prot
    r = r + s_non_prot
    return r


def generate_rel(param,Order_by,mean1,std1,a,b,shape_param,scale_param,shape_param1,shape_param2,mean2,std2):
    rank = list()
    if Order_by.upper() == "ASCENDING":
        rel = sorted(Distribution(param,mean1,std1,a,b,shape_param,scale_param,shape_param1,shape_param2,mean2,std2))
    elif Order_by.upper() == "DESCENDING":
        rel = sorted(Distribution(param,mean1,std1,a,b,shape_param,scale_param,shape_param1,shape_param2,mean2,std2), reverse=True)
    elif Order_by.upper() == "RANDOM":
        rel = Distribution(param,mean1,std1,a,b,shape_param,scale_param,shape_param1,shape_param2,mean2,std2)
    return rel




def rankings(param,Order_by = "Random",mean1=0,std1=1,a=0,b=0,shape_param=0,scale_param=0,shape_param1=0,shape_param2=0,mean2=0,std2=1):
    rank = list()
    rel_rank = list()
    fairness_rank = list()
    if param["Ranking_type"].upper() == "QUALITY":
        #1st: Ranking for Quality metrics: generate a ranking of relevance scores
        for i in range(0,int(param["Number_of_rankings"])):
            #print("Ranking" + str(i) + "generated over "+ param["Number_of_rankings"])
            rank.append(generate_rel(param,Order_by,mean1,std1,a,b,shape_param,scale_param,shape_param1,shape_param2,mean2,std2))
        return rank
    elif param["Ranking_type"].upper() == "FAIRNESS":
        if param["Order_by"].upper() == "RELEVANCE":
            param["Fairness_level"] = 0.5 ## In this we eliminate the impact of group belonging by assigning it randomly
            param["Proportion_or_protected_group"] = 0.5##We also assigns the same proportion of protected and non protected groups
            for i in range(0, int(param["Number_of_rankings"])):
                # print("Ranking" + str(i) + "generated over "+ param["Number_of_rankings"])
                rank.append(generate_rel(param, Order_by, mean1, std1, a, b, shape_param, scale_param, shape_param1,
                                         shape_param2, mean2, std2))
                fairness_rank.append(generate_r(param))

                rel_rank.append(generate_rel(param, Order_by, mean1, std1, a, b, shape_param, scale_param, shape_param1,
                                             shape_param2, mean2, std2))
        return [fairness_rank, rel_rank]


