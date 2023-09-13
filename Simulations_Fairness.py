import pandas as pd

from Simulations import *
from Distributions import *
from Exposure_Metrics import *
from Loading_param import *
import matplotlib.pyplot as plt
import numpy as np
from Distributions import adjust_rel
from Exposure_Metrics import Measuring_fairness


# param = Load("Parameters.txt")


def generate_r(param):  # p represent the proportion of protected group individuals in the ranking
    # f is fairness probability (see paper Measuring Fairness in Ranked Outputs)
    # n is the size of the ranking
    # When f > 0.5, members of the protected group (1) are preferred
    l = [0 if random.random() > float(param["Proportion_of_protected_group"]) else 1 for i in
         range(0, int(param["Ranking_length"]))]
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


#param = Load("Parameters Fairness.txt")
#print(param)
#group = generate_r(param)
#print(group)

def disparate_relevance(param_dict, group, mean1_prot=0, std1_prot=0, a_0=0, b_0=0, shape_param_prot=0,
                        scale_param_prot=0, shape_param1_prot=0, shape_param2_prot=0, mean2_prot=0, std2_prot=0,
                        mean1_non_prot=0, std1_non_prot=0, a_1=0, b_1=0, shape_param_non_prot=0,
                        scale_param_non_prot=0, shape_param1_non_prot=0, shape_param2_non_prot=0, mean2_non_prot=0,
                        std2_non_prot=0):
    rel_multiple = list()
    # For a si
    for nbr_rankings in range(0, int(param_dict["Number_of_rankings"])):
        rel = list()
        for G_i in group:
            if G_i == 0:
                rel.extend(Distribution_Fairness(param_dict, mean1_prot, std1_prot, a_0, b_0, shape_param_prot,
                                                 scale_param_prot, shape_param1_prot, shape_param2_prot, mean2_prot,
                                                 std2_prot))

            elif G_i == 1:
                rel.extend(Distribution_Fairness(param_dict, mean1_non_prot, std1_non_prot, a_1, b_1,
                                                 shape_param_non_prot, scale_param_non_prot, shape_param1_non_prot,
                                                 shape_param2_non_prot, mean2_non_prot, std2_non_prot))
        rel_multiple.append(rel)
    return rel_multiple

# test = disparate_relevance(param,group,mean1_prot=10,std1_prot=1,mean1_non_prot=50,std1_non_prot=1)
# print(test)
#test = [[[50.07094943008064, 10.872421470247616], [49.537538430388175, 10.900063162238549], [47.7874436131975, 10.124181612446355]],
#[[50.07094943008064, 10.872421470247616], [49.537538430388175, 10.900063162238549], [47.7874436131975, 10.124181612446355]]]


# print(Measuring_fairness(group,test,"DTR"))


def order_by_rel_within_group_desc(rel_list,group_list):
    rel_list0 = list()
    rel_list1 = list()
    rel_list_ordered = list()
    for g in range(0,len(group_list)):
        if group_list[g] == 0:
            rel_list0.append(rel_list[g])
        elif group_list[g] == 1:
            rel_list1.append(rel_list[g])

    rel_list0.sort(reverse=True)
    #print(rel_list0)
    rel_list1.sort(reverse=True)

    for g in range(0,len(group_list)):
        if group_list[g] == 0:
            rel_list_ordered.append(rel_list0[0])
            rel_list0.pop(0)
        elif group_list[g] == 1:
            rel_list_ordered.append(rel_list1[0])
            rel_list1.pop(0)
    return rel_list_ordered


def order_by_rel_within_group_asc(rel_list,group_list):
    rel_list0 = list()
    rel_list1 = list()
    rel_list_ordered = list()
    for g in range(0,len(group_list)):
        if group_list[g] == 0:
            rel_list0.append(rel_list[g])
        elif group_list[g] == 1:
            rel_list1.append(rel_list[g])

    rel_list0.sort()
    #print(rel_list0)
    rel_list1.sort()

    for g in range(0,len(group_list)):
        if group_list[g] == 0:
            rel_list_ordered.append(rel_list0[0])
            rel_list0.pop(0)
        elif group_list[g] == 1:
            rel_list_ordered.append(rel_list1[0])
            rel_list1.pop(0)
    return rel_list_ordered


def order_by_rel_within_group_rand(rel_list,group_list):
    rel_list0 = list()
    rel_list1 = list()
    rel_list_ordered = list()
    for g in range(0,len(group_list)):
        if group_list[g] == 0:
            rel_list0.append(rel_list[g])
        elif group_list[g] == 1:
            rel_list1.append(rel_list[g])

    random.shuffle(rel_list0)
    #print(rel_list0)
    random.shuffle(rel_list1)

    for g in range(0,len(group_list)):
        if group_list[g] == 0:
            rel_list_ordered.append(rel_list0[0])
            rel_list0.pop(0)
        elif group_list[g] == 1:
            rel_list_ordered.append(rel_list1[0])
            rel_list1.pop(0)
    return rel_list_ordered



def disparate_order_by_relevance_within_group(param_dict, group, mean1_prot=0, std1_prot=0, a_0=0, b_0=0, shape_param_prot=0,
                        scale_param_prot=0, shape_param1_prot=0, shape_param2_prot=0, mean2_prot=0, std2_prot=0,
                        mean1_non_prot=0, std1_non_prot=0, a_1=0, b_1=0, shape_param_non_prot=0,
                        scale_param_non_prot=0, shape_param1_non_prot=0, shape_param2_non_prot=0, mean2_non_prot=0,
                        std2_non_prot=0):
    rel_multiple_asc = list()
    rel_multiple_desc = list()
    rel_multiple_rand = list()
    rel_multiple_3_order = dict()
    #print("group", group)
    # For a si
    for nbr_rankings in range(0, int(param_dict["Number_of_rankings"])):
        rel = list()
        for G_i in group:
            if G_i == 0:

                rel.extend(Distribution_Fairness(param_dict, mean1_prot, std1_prot, a_0, b_0, shape_param_prot,
                                                 scale_param_prot, shape_param1_prot, shape_param2_prot, mean2_prot,
                                                 std2_prot))

            elif G_i == 1:
                rel.extend(Distribution_Fairness(param_dict, mean1_non_prot, std1_non_prot, a_1, b_1,
                                                 shape_param_non_prot, scale_param_non_prot, shape_param1_non_prot,
                                                 shape_param2_non_prot, mean2_non_prot, std2_non_prot))

        #print("group:",group)
        rel_asc = order_by_rel_within_group_asc(rel,group)
        #print("rel_asc",rel_asc)

        rel_desc = order_by_rel_within_group_desc(rel,group)
        #print("rel_desc",rel_desc)

        rel_rand = order_by_rel_within_group_rand(rel,group)
        #print("rel_rand",rel_rand)

        rel_multiple_asc.append(rel_asc)
        rel_multiple_desc.append(rel_desc)
        rel_multiple_rand.append(rel_rand)

    rel_multiple_3_order["asc"] =  rel_multiple_asc
    rel_multiple_3_order["desc"] = rel_multiple_desc
    rel_multiple_3_order["rand"] = rel_multiple_rand

    return rel_multiple_3_order