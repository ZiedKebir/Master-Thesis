import pandas as pd

from Simulations import *
from Distributions import *
from Quality_metrics import *
from Loading_param import *
import matplotlib.pyplot as plt
import numpy as np

d = Load("Parameters.txt")

############################
### Normal Distribution ####
############################


######## Change Mean #################
d["Type_distribution"] = "Normal"
for std in [1]:
    d["Ranking_length"] = 500
    print("std = ", std)
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for mean in range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"])):
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", mean1=mean, std1=std))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", mean1=mean, std1=std))
        Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", mean1=mean, std1=std))

    for K in [250]:
        d["K"] = K
        print("K= ", K)
        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"])), average_precision_mean_random,
                 color="red", label="Random Rank Allocation")
        plt.plot(range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"])), average_precision_mean_Asc,
                 color="blue", label="Ascending Rank Allocation")
        plt.plot(range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"])), average_precision_mean_Desc,
                 color="green", label="Descending Rank Allocation")
        plt.xlabel("Mean")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title("average_precision: Vary mean: std= " + str(std) + " K= " + str(d["K"]) + " R length= " + str(
            d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Normal Distribution/average_precision/Mean/vary mean std=" + str(
                std) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"]) + "bt =" + d[
                "Type_position_bias"] + ".png")
        plt.show()
"""
######################### change std ##########################
for mean in [100, 500]:
    print("mean = ", mean)
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    d["Ranking_length"] = 500
    for std in range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"])):
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", mean1=mean, std1=std))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", mean1=mean, std1=std))
        Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", mean1=mean, std1=std))

    for K in [100, 200, 300]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"])), average_precision_mean_random,
                 color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"])), average_precision_mean_Asc,
                 color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"])), average_precision_mean_Desc,
                 color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        # plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("std")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title("average_precision: Vary std(higher range): mean= " + str(mean) + " K= " + str(
            d["K"]) + " R length= " + str(
            d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Normal Distribution/average_precision/std/vary std mean=" + str(
                mean) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"]) + "bt =" + d[
                "Type_position_bias"] + ".png")
        plt.show()
"""

"""
############################
### Uniform Distribution ####
############################
d = Load("Parameters.txt")
d["Type_distribution"] = "Uniform"

print(d)
s1 = dict(dict())
data_asc = pd.DataFrame(columns =["range","K","average_precision"])
data_random = pd.DataFrame(columns = ["range","K","average_precision"])
data_desc = pd.DataFrame(columns = ["range","K","average_precision"])

row_nbr = 0
interval_size = 10
a = 0#0,0,150
b = 1000#150,1000,300
range_gap = 100#5,100,5
str_range = "range = range(" + str(a) + "," + str(b) + "," + str(d["range_gap"])+")"
for rank_length in [100,500]:
    print(rank_length)
    d["Ranking_length"] = rank_length
    for a_b in [[i, i + interval_size] for i in range(a, b, range_gap)]:
        print("range",a_b)
        Ranking_change_interval_random = list()
        Ranking_change_interval_Asc = list()
        Ranking_change_interval_Desc = list()

        Ranking_change_interval_random.append(rankings(d, Order_by="Random", a=a_b[0], b=a_b[1]))
        Ranking_change_interval_Asc.append(rankings(d, Order_by="Ascending", a=a_b[0], b=a_b[1]))
        Ranking_change_interval_Desc.append(rankings(d, Order_by="Descending", a=a_b[0], b=a_b[1]))

        for K in [i * rank_length for i in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]]:
            d["K"] = K
            print("K= ", K)

            average_precision_interval_random = Measuring_quality(Ranking_change_interval_random, "average_precision", d)
            # print("average_precision_mean_random",average_precision_mean_random)
            average_precision_interval_Asc = Measuring_quality(Ranking_change_interval_Asc, "average_precision", d)
            # print("average_precision_mean_Asc", average_precision_mean_Asc)
            average_precision_interval_Desc = Measuring_quality(Ranking_change_interval_Desc, "average_precision", d)
            # print("average_precision_mean_Desc",average_precision_mean_Desc)

            data_asc.loc[row_nbr] = [a_b, K, average_precision_interval_Asc[0] ]
            data_random.loc[row_nbr] = [a_b, K,average_precision_interval_random[0]]
            data_desc.loc[row_nbr] = [a_b, K,average_precision_interval_Desc[0]]
            row_nbr+=1


    #print(data_asc)
    #data_asc.to_csv(path_or_buf="C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/data_asc.csv", sep=';')
    #data_desc.to_csv(path_or_buf="C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/data_desc.csv", sep=';')
    #data_random.to_csv(path_or_buf="C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/data_random.csv", sep=';')

    ## ASC ###
    #point_size = np.array(data_asc["average_precision"]) * 350
    plt.figure(figsize=(20,10))
    sc = plt.scatter([str(i) for i in data_asc["range"]], round(data_asc["K"]/rank_length,1), c= data_asc["average_precision"])
    cbar = plt.colorbar(sc)
    plt.title("Uniform: asc " + str_range+ " ranking length= "+str(rank_length)+"bias type= "+ d["Type_position_bias"], fontsize = 18)
    cbar.set_label("average_precision")
    plt.xlabel("Range of Uniform Distribution ",fontsize = 21)
    plt.ylabel("Proportion of the ranking considered",fontsize = 21)
    plt.xticks(rotation = 90)
    plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/Asc/ "+"ASC "+str_range+"bt "+ d["Type_position_bias"] + " K= "  +str(d["K"]) + " R length= " +str(rank_length)+".png")
    plt.show()

    #### Rand ####
    #point_size = np.array(data_asc["average_precision"]) * 300
    plt.figure(figsize=(20,10))
    sc = plt.scatter([str(i) for i in data_random["range"]], round(data_random["K"]/rank_length,1), c= data_random["average_precision"])
    cbar = plt.colorbar(sc)
    plt.title("Uniform: rand " + str_range+ " ranking length= "+str(rank_length) +"bias type= "+ d["Type_position_bias"]+"interval size="+str(interval_size), fontsize = 18)
    cbar.set_label("average_precision")
    plt.xlabel("Range of Uniform Distribution ",fontsize = 21)
    plt.ylabel("Proportion of the ranking considered",fontsize = 21)
    plt.xticks(rotation = 90)
    plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/Rand/ "+"Rand "+str_range+"bt "+ d["Type_position_bias"] + " K= "  +str(d["K"]) + " R length= " +str(rank_length)+".png")
    plt.show()

   ### DESC ###
    #point_size = np.array(data_desc["average_precision"]) * 300
    plt.figure(figsize=(20,10))
    sc = plt.scatter([str(i) for i in data_desc["range"]], round(data_desc["K"]/rank_length,1), c= data_desc["average_precision"])
    cbar = plt.colorbar(sc)
    plt.title("Uniform: DESC " + str_range+ " ranking length= "+str(rank_length)+"bias type= "+ d["Type_position_bias"], fontsize = 18)
    cbar.set_label("average_precision")
    plt.xlabel("Range of Uniform Distribution ", fontsize = 21)
    plt.ylabel("Proportion of the ranking considered", fontsize = 21)
    plt.xticks(rotation = 90)
    plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/DESC/ "+"DESC "+str_range+"bt "+ d["Type_position_bias"] + " K= "  +str(d["K"]) + " R length= " +str(rank_length)+".png")
    plt.show()

"""

"""
############################
### Gamma Distribution #####
############################
d["Type_distribution"] = "GAMMA"

# The more you increase shape parameter k the more shifted and symmetric to the right is the distribution
# The more you increase the scale tete the less dispersed is the curve (quite similar to standard deviation)
# Gamma distribution cannot have negative values

###Vary the shape####
### RANKING LENGTH 100 ###

for scale in [1, 50, 100]:
    print("scale = ", scale)
    d["Ranking_length"] = 100
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for shape in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])):
        print("shape = ", shape)
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param=shape, scale_param=scale))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_random, color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Asc, color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Desc, color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("Shape")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title("average_precision: Vary Shape: scale= " + str(scale) + " K= " + str(d["K"]) + " R length= " + str(
            d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Gamma Distribution/average_precision/x-axis shape/average_precision Gamma dist scale=" + str(
                scale) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"]) + ".png")
        plt.show()

    ### RANKING LENGTH 500 ###

for scale in [1, 50, 100]:
    print("scale = ", scale)
    d["Ranking_length"] = 500
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for shape in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])):
        print("shape = ", shape)
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param=shape, scale_param=scale))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_random, color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Asc, color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Desc, color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("Shape")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title("average_precision: Vary Shape: scale= " + str(scale) + " K= " + str(d["K"]) + " R length= " + str(
            d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Gamma Distribution/average_precision/x-axis shape/average_precision Gamma dist scale=" + str(
                scale) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"])+"bt= "+str(d["Type_position_bias"]) + ".png")
        plt.show()

####### vary the scale #####
### Ranking length 100
for shape in [1, 50, 100]:
    print("shape = ", shape)
    d["Ranking_length"] = 100
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for scale in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])):
        print("scale = ", scale)
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Desc.append(
            rankings(d, Order_by="Descending", shape_param=shape, scale_param=scale))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_random, color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Asc, color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Desc, color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("Scale")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title(
            "average_precision Gamma: Vary Scale: shape= " + str(shape) + " K= " + str(d["K"]) + " R length= " + str(
                d["Ranking_length"]))
        plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Gamma Distribution/average_precision/x-axis scale/average_precision Gamma Vary Scale shape=" + str(shape) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"])+"bt= "+str(d["Type_position_bias"]) + ".png")
        plt.show()

        ### Ranking length 500

for shape in [1, 50, 100]:
    print("shape = ", shape)
    d["Ranking_length"] = 100
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for scale in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])):
        print("scale = ", scale)
        Ranking_change_mean_random.append(
            rankings(d, Order_by="Random", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Asc.append(
            rankings(d, Order_by="Ascending", shape_param=shape, scale_param=scale))
        Ranking_change_mean_Desc.append(
            rankings(d, Order_by="Descending", shape_param=shape, scale_param=scale))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_random,
                 color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Asc,
                 color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), average_precision_mean_Desc,
                 color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("Scale")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title("average_precision Gamma: Vary Scale: shape= " + str(shape) + " K= " + str(
            d["K"]) + " R length= " + str(
            d["Ranking_length"]))
        plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Gamma Distribution/average_precision/x-axis scale/average_precision Gamma Vary Scale shape=" + str(scale) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"])+"bt= "+str(d["Type_position_bias"]) + ".png")
        plt.show()



############################
### Beta Distribution #####
############################

# relation between alpha and beta determines the shape of the distribution

d["Type_distribution"] = "BETA"
### fix alpha and vary beta ###
### Ranking lenght 100 ##
for alpha in [1, 50, 100]:
    print("alpha = ", alpha)
    d["Ranking_length"] = 100
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for beta in range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])):
        print("beta = ", beta)
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])), average_precision_mean_random, color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])), average_precision_mean_Asc, color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])), average_precision_mean_Desc, color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("beta")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title(
            "average_precision Beta: Vary beta: alpha= " + str(alpha) + " K= " + str(d["K"]) + " R length= " + str(
                d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/average_precision/beta x-axis/average_precision Beta Vary beta alpha=" + str(
                alpha) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"]) +"bt= "+str(d["Type_position_bias"])+ ".png")
        plt.show()

        ### Ranking length 500

for alpha in [1, 50, 100]:
    print("alpha = ", alpha)
    d["Ranking_length"] = 500
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for beta in range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])):
        print("beta = ", beta)
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Desc.append(
            rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])), average_precision_mean_random, color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])), average_precision_mean_Asc, color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["beta_lower_limit"]), int(d["beta_upper_limit"])), average_precision_mean_Desc, color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("beta")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title(
            "average_precision Beta: Vary beta: alpha= " + str(alpha) + " K= " + str(d["K"]) + " R length= " + str(
                d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/average_precision/beta x-axis/average_precision beta Vary beta alpha=" + str(
                alpha) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"]) +"bt= "+str(d["Type_position_bias"]) +".png")
        plt.show()

### fix beta and vary alpha ###

### Ranking length 100

for beta in [1, 50, 100]:
    print("beta = ", beta)
    d["Ranking_length"] = 100
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for alpha in range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])):
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])), average_precision_mean_random, color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])), average_precision_mean_Asc, color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])), average_precision_mean_Desc, color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("alpha")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title(
            "average_precision Beta dist: Vary alpha: beta= " + str(beta) + " K= " + str(d["K"]) + " R length= " + str(
                d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/average_precision/alpha x-axis/average_precision Beta dist Vary alpha beta=" + str(
                beta) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"]) + "bt= "+str(d["Type_position_bias"])+".png")
        plt.show()


### Ranking length 500

for beta in [1, 50, 100]:
    print("beta = ", beta)
    d["Ranking_length"] = 500
    Ranking_change_mean_random = list()
    Ranking_change_mean_Asc = list()
    Ranking_change_mean_Desc = list()
    for alpha in range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])):
        Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
        Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

    for K in [0.1*d["Ranking_length"], 0.5*d["Ranking_length"],0.7*d["Ranking_length"]]:
        d["K"] = K
        print("K= ", K)

        average_precision_mean_random = Measuring_quality(Ranking_change_mean_random, "average_precision", d)
        # print("average_precision_mean_random",average_precision_mean_random)
        average_precision_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "average_precision", d)
        # print("average_precision_mean_Asc", average_precision_mean_Asc)
        average_precision_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "average_precision", d)
        # print("average_precision_mean_Desc",average_precision_mean_Desc)

        plt.plot(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])), average_precision_mean_random, color="red",
                 label="Random Rank Allocation")
        plt.plot(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])), average_precision_mean_Asc, color="blue",
                 label="Ascending Rank Allocation")
        plt.plot(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])), average_precision_mean_Desc, color="green",
                 label="Descending Rank Allocation")
        plt.axhline(y=0.5, color='black', linestyle='-')
        #plt.axhline(y=0, color='black', linestyle='-')
        plt.xlabel("alpha")
        plt.ylabel("average_precision")
        plt.legend()
        plt.title(
            "average_precision Beta dist: Vary alpha: beta= " + str(beta) + " K= " + str(d["K"]) + " R length= " + str(
                d["Ranking_length"]))
        plt.savefig(
            "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/average_precision/alpha x-axis/average_precision Beta dist Vary alpha beta=" + str(
                beta) + " K= " + str(d["K"]) + " R length= " + str(d["Ranking_length"]) +"bt= "+str(d["Type_position_bias"]) +".png")
        plt.show()



##############################
### Bimodal Distribution #####
##############################
d["Type_distribution"] = "Bimodal"

for ids in [[1, 1], [10, 15], [15, 10]]:
    interval_size = 10
    d = Load("Parameters.txt")
    print(d)
    K = d["K"]
    s1 = dict(dict())



    mean1 = 0
    mean2 = 0
    std1 = ids[0]
    std2 = ids[1]
    row_nbr = 0
    range_gap = int(d["range_gap"])
    # str_range = "range = range(" + str(a) + "," + str(b) + "," + str(d["range_gap"])+")"
    for rank_length in [100, 500]:
        print(rank_length)
        d["Ranking_length"] = rank_length

        for K in [0.1,
                    0.7]:  # P is the proportion used for the first distribution to construct the bimodal dsitribution
            data_asc = pd.DataFrame(columns=["range", "p", "average_precision", "K"])
            data_random = pd.DataFrame(columns=["range", "p", "average_precision", "K"])
            data_desc = pd.DataFrame(columns=["range", "p", "average_precision", "K"])

            for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
                      0.9]:  # P is the proportion used for the first distribution to construct the bimodal dsitribution
                d["p"] = p
                print("p= ", p)

                for m1_m2 in [[20, 50], [50, 100], [10, 100], [20, 100], [100, 500], [500, 1000]]:
                    print("range", m1_m2)
                    Ranking_change_interval_random = list()
                    Ranking_change_interval_Asc = list()
                    Ranking_change_interval_Desc = list()
                    Ranking_change_interval_random.append(
                        rankings(d, Order_by="Random", mean1=m1_m2[0], std1=std1, mean2=m1_m2[0], std2=std2))
                    Ranking_change_interval_Asc.append(
                        rankings(d, Order_by="Ascending", mean1=m1_m2[0], std1=std1, mean2=m1_m2[0], std2=std2))
                    Ranking_change_interval_Desc.append(
                        rankings(d, Order_by="Descending", mean1=m1_m2[0], std1=std1, mean2=m1_m2[0], std2=std2))

                    average_precision_interval_random = Measuring_quality(Ranking_change_interval_random, "average_precision", d)
                    # print("average_precision_mean_random",average_precision_mean_random)
                    average_precision_interval_Asc = Measuring_quality(Ranking_change_interval_Asc, "average_precision", d)
                    # print("average_precision_mean_Asc", average_precision_mean_Asc)
                    average_precision_interval_Desc = Measuring_quality(Ranking_change_interval_Desc, "average_precision", d)
                    # print("average_precision_mean_Desc",average_precision_mean_Desc)

                    data_asc.loc[row_nbr] = [m1_m2, p, average_precision_interval_Asc[0], K]
                    data_random.loc[row_nbr] = [m1_m2, p, average_precision_interval_random[0], K]
                    data_desc.loc[row_nbr] = [m1_m2, p, average_precision_interval_Desc[0], K]
                    row_nbr += 1

                # print(data_asc)
                # data_asc.to_csv(path_or_buf="C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/data_asc.csv", sep=';')
                # data_desc.to_csv(path_or_buf="C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/data_desc.csv", sep=';')
                # data_random.to_csv(path_or_buf="C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/average_precision/data_random.csv", sep=';')
            print(data_desc)
            ## DESC ###
            # point_size = np.array(data_asc["average_precision"]) * 350
            plt.figure(figsize=(20, 10))
            sc = plt.scatter([str(i) for i in data_desc["range"]], [i for i in data_desc["p"]], c=data_desc["average_precision"])
            cbar = plt.colorbar(sc)
            plt.title("Bimodal: desc means m1_m2=" + str(m1_m2) + "stds = " + str([std1, std2]) + "mixing prop= " + str(
                p) + " rl= " + str(rank_length) + "bias type= " + d["Type_position_bias"] + "K = " + str(K),
                      fontsize=18)
            cbar.set_label("average_precision")
            plt.xlabel("Range of Means of Bidmodal Distribution ", fontsize=21)
            plt.ylabel("Mixing proportion ", fontsize=21)
            plt.xticks(rotation=90)
            plt.savefig(
                "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Bimodal Distribution/average_precision/DESC/std=" + str(
                    [int(std1), int(std2)]) + "/average_precision " + "DESC " + "means= " + str(m1_m2) + "stds=" + "[" + str(
                    std1) + "," + str(std2) + "]" + "bt " + d[
                    "Type_position_bias"] + " R length= " + str(rank_length) + ".png")
            plt.show()

            ## Rand ###
            # point_size = np.array(data_asc["average_precision"]) * 350
            plt.figure(figsize=(20, 10))
            sc = plt.scatter([str(i) for i in data_random["range"]], [i for i in data_random["p"]],
                             c=data_random["average_precision"])
            cbar = plt.colorbar(sc)
            plt.title("Bimodal: rand means m1_m2=" + str(m1_m2) + "stds = " + str([std1, std2]) + " rl= " + str(rank_length) + "bias type= " + d["Type_position_bias"] + "K = " + str(K),
                      fontsize=18)
            cbar.set_label("average_precision")
            plt.xlabel("Range of Means of Bidmodal Distribution ", fontsize=21)
            plt.ylabel("Mixing proportion ", fontsize=21)
            plt.xticks(rotation=90)
            plt.savefig(
                "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Bimodal Distribution/average_precision/RAND/std=" + str(
                    [int(std1), int(std2)]) + "/average_precision " + "ASC " + "means= " + str(m1_m2) + "stds=" + "[" + str(
                    std1) + "," + str(std2) + "]"  + "bt " + d[
                    "Type_position_bias"] + " K= " + str(
                    d["K"]) + " R length= " + str(rank_length) + ".png")
            plt.show()

            ## ASC ###
            # point_size = np.array(data_asc["average_precision"]) * 350
            plt.figure(figsize=(20, 10))
            sc = plt.scatter([str(i) for i in data_asc["range"]], [i for i in data_asc["p"]], c=data_asc["average_precision"])
            cbar = plt.colorbar(sc)
            plt.title("Bimodal: asc means m1_m2=" + str(m1_m2) + "stds = " + str([std1, std2]) + " rl= " + str(rank_length) + "bias type= " + d["Type_position_bias"] + "K = " + str(K),
                      fontsize=18)
            cbar.set_label("average_precision")
            plt.xlabel("Range of Means of Bidmodal Distribution ", fontsize=21)
            plt.ylabel("Mixing proportion ", fontsize=21)
            plt.xticks(rotation=90)
            plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Bimodal Distribution/average_precision/ASC/std=" + str(
                [int(std1), int(std2)]) + "/average_precision " + "ASC " + "means= " + str(m1_m2) + "stds=" + "[" + str(
                std1) + "," + str(std2) + "]" + "mixing prop= " + str(p) + "bt " + d[
                            "Type_position_bias"] + " R length= " + str(
                rank_length) + ".png")
            plt.show() """