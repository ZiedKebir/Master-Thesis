from numpy import random
from scipy.stats import uniform
import numpy as np
from scipy.stats import uniform
from Loading_param import *

def adjust_rel(rel_scores):
    l = list()
    if rel_scores<0:
        l.append(0)
        return l
    elif rel_scores>=0:
        l.append(rel_scores)
        return l


def adjust_rel_qual(rel_scores):
    return [i if i > 0 else 0 for i in rel_scores]



def generate_bimodal_value(mean1=0, std1=1, mean2=0, std2=1, p=0.5):
    # Sample a value from each of the two normal distributions
    value1 = np.random.normal(mean1, std1)
    value2 = np.random.normal(mean2, std2)

    # Decide which distribution to choose based on the proportion 'p'
    if np.random.random() < p:
        bimodal_value = value1
    else:
        bimodal_value = value2


    return bimodal_value


def Distribution(param_dict,mean1=0,std1=0,a=0,b=0,shape_param=0,scale_param=0,shape_param1=0,shape_param2=0,mean2=0,std2=0):
   #d = Load(filename)
    #param_dict replaces the d variable
    if param_dict["Type_distribution"].upper() == "NORMAL":
        return adjust_rel_qual(np.random.normal(float(mean1), float(std1), int(param_dict["Ranking_length"])))
    elif param_dict["Type_distribution"].upper() == "UNIFORM":
        return adjust_rel_qual(uniform.rvs(a, b, size=int(param_dict["Ranking_length"])))
    elif param_dict["Type_distribution"].upper() == "GAMMA":
        return adjust_rel_qual(random.gamma(shape=shape_param,scale=scale_param,size=int(param_dict["Ranking_length"])))
    elif param_dict["Type_distribution"].upper() == "BETA":
        return adjust_rel_qual(random.beta(shape_param1,shape_param2,size=int(param_dict["Ranking_length"])))

    elif param_dict["Type_distribution"].upper() == "BIMODAL":
        return adjust_rel_qual(np.concatenate((np.random.normal(mean1, std1, int(round((float(param_dict["Ranking_length"]) * float(param_dict["p"]))))), np.random.normal(mean2, std2, int(round((float(param_dict["Ranking_length"]) * (1-float(param_dict["p"])))))))))


def Distribution_Fairness(param_dict, mean1=0, std1=0, a=0, b=0, shape_param=0, scale_param=0, shape_param1=0,
                          shape_param2=0, mean2=0, std2=0):
    # d = Load(filename)
    # param_dict replaces the d variable
    if param_dict["Type_distribution"].upper() == "NORMAL":
        #print("+++",type(adjust_rel(np.random.normal(float(mean1), float(std1), size=1))))

        #print(adjust_rel(np.random.normal(float(mean1), float(std1), size=1)))
        return adjust_rel(np.random.normal(float(mean1), float(std1), size=1))


    elif param_dict["Type_distribution"].upper() == "UNIFORM":
        return adjust_rel(uniform.rvs(a, b, size=1))

    elif param_dict["Type_distribution"].upper() == "GAMMA":
        return adjust_rel(random.gamma(shape=shape_param, scale=scale_param, size=1))

    elif param_dict["Type_distribution"].upper() == "BETA":
        return adjust_rel(random.beta(shape_param1, shape_param2, size=1))


    elif param_dict["Type_distribution"].upper() == "BIMODAL":
        return adjust_rel(generate_bimodal_value(mean1=mean1, std1=std1, mean2=mean2, std2=std2,p=param_dict["p"]))

#param = Load("Parameters Fairness.txt")
#print(Distribution_Fairness(param, mean1=-100,std1=1))