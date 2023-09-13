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
#######################################################################################################################
# 04/09/2023 Normal DISTRIBUTIONS HAS BEEN PROPERLY FORMATTED
#######################################################################################################################
d = Load("Parameters.txt")
d["Type_distribution"] = "Normal"
"""
d = Load("Parameters.txt")
d["Type_distribution"] = "Normal"
def change_mean_norm(std_l=list(),RL=[100],Pos=[0.5]):
    ######## Change Mean #################
    d["mean_lower_limit"] = 0
    d["mean_upper_limit"] = 300
    for l in RL:
        d["Ranking_length"] = l
        for std in std_l:
            print("std = ", std)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            for mean in range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"])):
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", mean1=mean, std1=std))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", mean1=mean, std1=std))
                Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", mean1=mean, std1=std))

            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)
                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                #print("Random: ", MRR_mean_random)
                #print("ASC: ", MRR_mean_Asc)
                #print("DESC: ", MRR_mean_Desc)
                plt.plot(range(int(d["mean_lower_limit"]),int(d["mean_upper_limit"])), MRR_mean_random, color="red", label="Random Rank Allocation")
                plt.plot(range(int(d["mean_lower_limit"]),int(d["mean_upper_limit"])), MRR_mean_Asc, color="blue", label="Ascending Rank Allocation")
                plt.plot(range(int(d["mean_lower_limit"]),int(d["mean_upper_limit"])), MRR_mean_Desc, color="green", label="Descending Rank Allocation")
                plt.xlabel("Mean")
                plt.ylabel("MRR")
                #plt.xlim(80,300)
                plt.legend()
                plt.title("Normal:std=" + str(std) + " Pos="  +str(d["pos"]) + " Rl= " +str(d["Ranking_length"]))
                plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Normal Distribution/MRR/New vary mean std="+ str(std) + " pos= "  +str(d["pos"]) + " R length= " +str(d["Ranking_length"])+"bt =" + d["Type_position_bias"]+ "xlim" + ".png")
                plt.show()

change_mean_norm(std_l=[1,5],Pos=[0.5,0.7])
change_mean_norm(std_l=[1,5],Pos=[0.5],RL=[500])



######################### change std ##########################
def change_std_norm(mean_l=list(), RL=[100],Pos=[0.5]):
    d["std1_lower_limit"] = 1
    d["std1_upper_limit"] = 60
    for l in RL:
        d["Ranking_length"] = l
        for mean in mean_l:
            print("mean = ", mean)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            for std in range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"])):
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", mean1=mean, std1=std))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", mean1=mean, std1=std))
                Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", mean1=mean, std1=std))
            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)

                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                #print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)
                plt.plot(range(int(d["std1_lower_limit"]),int(d["std1_upper_limit"])), MRR_mean_random, color="red", label="Random Rank Allocation")
                plt.plot(range(int(d["std1_lower_limit"]),int(d["std1_upper_limit"])), MRR_mean_Asc, color="blue", label="Ascending Rank Allocation")
                plt.plot(range(int(d["std1_lower_limit"]),int(d["std1_upper_limit"])), MRR_mean_Desc, color="green", label="Descending Rank Allocation")
                #plt.axhline(y=0.5, color='black', linestyle='-')
                #plt.axhline(y=0, color='black', linestyle='-')
                plt.xlabel("std")
                plt.ylabel("MRR")
                plt.legend()
                plt.title("Normal:Mean=" + str(mean) + " Pos="  +str(d["pos"]) + " Rl=" +str(d["Ranking_length"]))
                plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Normal Distribution/MRR/New vary std mean="+ str(mean) + " pos= "  +str(d["pos"]) + " R length= " +str(d["Ranking_length"])+"bt =" + d["Type_position_bias"]+".png")
                plt.show()

change_std_norm(mean_l=[100])






###################################################################################################################################################################################################################################################################################
#######################################################################################################################
# 04/09/2023 UNIFORM DISTRIBUTIONS HAS BEEN PROPERLY FORMATTED
#######################################################################################################################

#############################
### Uniform Distribution ####
#############################
### vary mean ###
d = Load("Parameters.txt")
d["Type_distribution"] = "Uniform"

def change_mean_unif(interval_size, Pos=[0.5], Rl=[100]):
    #interval_size = 3
    a = 0#0,0,100,50
    b = 300 #500,400,300,350
    range_gap = interval_size
    str_range = "range=" + "["+str(a) + "," + str(b)+"]"+" size_diff="+ str(range_gap)
    for rank_length in Rl:
        print("rank_length = ", rank_length)
        d["Ranking_length"] = rank_length
        Ranking_change_interval_random = list()
        Ranking_change_interval_Asc = list()
        Ranking_change_interval_Desc = list()

        for a_b in [[i, i + interval_size] for i in range(a, b, range_gap)]:
            print("range", a_b)
            Ranking_change_interval_random.append(rankings(d, Order_by="Random", a=a_b[0], b=a_b[1]))
            #print(Ranking_change_interval_random)
            Ranking_change_interval_Asc.append(rankings(d, Order_by="Ascending", a=a_b[0], b=a_b[1]))
            Ranking_change_interval_Desc.append(rankings(d, Order_by="Descending", a=a_b[0], b=a_b[1]))


        for pos in Pos:
            d["pos"] = pos
            print("pos= ", pos)

            MRR_interval_random = Measuring_quality(Ranking_change_interval_random, "MRR", d)
            # print("MRR_mean_random",MRR_mean_random)
            MRR_interval_Asc = Measuring_quality(Ranking_change_interval_Asc, "MRR", d)
            # print("MRR_mean_Asc", MRR_mean_Asc)
            MRR_interval_Desc = Measuring_quality(Ranking_change_interval_Desc, "MRR", d)
            # print("MRR_mean_Desc",MRR_mean_Desc)


            plt.plot([round((i[0] + i[1]) / 2) for i in [[i, i + interval_size] for i in range(a, b, range_gap)]], MRR_interval_Asc,color="blue", label="Ascending Rank Allocation")
            plt.plot([round((i[0] + i[1]) / 2) for i in [[i, i + interval_size] for i in range(a, b, range_gap)]], MRR_interval_Desc,color="green", label="Descending Rank Allocation")
            plt.plot([round((i[0] + i[1]) /2) for i in [[i, i + interval_size] for i in range(a, b, range_gap)]], MRR_interval_random,color="Red", label="Random Rank Allocation")
            plt.legend()

            # sc = plt.scatter([str(i) for i in data_asc["range"]], data_asc["Pos"], c= data_asc["MRR"], s=point_size)
            plt.title("Uniform:"+str_range + " Rl=" + str(rank_length)+" Pos="+str(pos))
            plt.xlabel("Mean", fontsize=10)
            plt.ylabel("MRR", fontsize=10)
            x_ticks = np.arange(a, b+50, 50)
            #print([str(round((i[0] + i[1]) / 2)) for i in [[i, i + interval_size] for i in range(a, b, range_gap)]])
            # Set the new x-axis tick values
            plt.xticks(x_ticks, x_ticks)
            plt.savefig(
                "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/MRR/New MRR line " + str_range + "bt " +
                d["Type_position_bias"] + " pos= " + str(d["pos"]) + " R length= " + str(rank_length) + ".png")
            plt.show()

change_mean_unif(interval_size=3, Pos=[0.5,0.7], Rl=[100])
change_mean_unif(interval_size=3, Pos=[0.5], Rl=[500])
change_mean_unif(interval_size=17, Pos=[0.5], Rl=[100])





d = Load("Parameters.txt")
d["Type_distribution"] = "Uniform"
#variance##
def change_std_unif(Rl=[100],Pos=[0.5]):
        d = Load("Parameters.txt")
        d["Type_distribution"] = "Uniform"
        initial_interval = [100,105] # [100,105],[300,305]
        a =100#300.100
        b =105#305,105
        range_gap = 1
        str_range = "range=" + str(initial_interval) + " size_diff=" + str(range_gap)
        for rank_length in Rl:
            print("rank_length = ", rank_length)
            d["Ranking_length"] = rank_length
            Ranking_change_interval_random = list()
            Ranking_change_interval_Asc = list()
            Ranking_change_interval_Desc = list()

            for interval_size in range(0,int(a/range_gap)+1,range_gap):
                print("Interval size", interval_size)
                a_b = [a-interval_size,b+interval_size]
                print(a_b)
                Ranking_change_interval_random.append(rankings(d, Order_by="Random", a=a_b[0], b=a_b[1]))
                # print(Ranking_change_interval_random)
                Ranking_change_interval_Asc.append(rankings(d, Order_by="Ascending", a=a_b[0], b=a_b[1]))
                Ranking_change_interval_Desc.append(rankings(d, Order_by="Descending", a=a_b[0], b=a_b[1]))

            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)

                MRR_interval_random = Measuring_quality(Ranking_change_interval_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_interval_Asc = Measuring_quality(Ranking_change_interval_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_interval_Desc = Measuring_quality(Ranking_change_interval_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                ## ASC ###
                # point_size = np.array(data_asc["MRR"]) * 350
                plt.plot([math.sqrt(pow((2*i+b-a),2)/12)for i in range(0,int(a/range_gap)+1,range_gap)],
                         MRR_interval_Asc, color="blue", label="Ascending Rank Allocation")
                plt.plot([math.sqrt(pow((2*i+b-a),2)/12)for i in range(0,int(a/range_gap)+1,range_gap)],
                         MRR_interval_Desc, color="green", label="Descending Rank Allocation")
                plt.plot([math.sqrt(pow((2*i+b-a),2)/12)for i in range(0,int(a/range_gap)+1,range_gap)],
                         MRR_interval_random, color="Red", label="Random Rank Allocation")
                #plt.axhline(y=0.5, color='black', linestyle='-')
                plt.legend()
                # sc = plt.scatter([str(i) for i in data_asc["range"]], data_asc["Pos"], c= data_asc["MRR"], s=point_size)
                plt.title("Uniform:" + str_range + " Rl=" + str(rank_length) + " Pos=" + str(pos))
                plt.xlabel("Std", fontsize=10)
                plt.ylabel("MRR", fontsize=10)
                plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Uniform Distribution/MRR/New MRR var " + str_range + "bt " +d["Type_position_bias"] + " pos= " + str(d["pos"]) + " RL= " + str(rank_length) + ".png")
                plt.show()

change_std_unif(Rl=[100],Pos=[0.5])




######################################################################################################################################################

############################
### Gamma Distribution #####
############################
d["Type_distribution"] = "GAMMA"


###Vary the shape####
### RANKING LENGTH 100 ###

def change_shape_gamma(Scale,RL=[100], Pos=[0.5]):
    for l in RL:
        d["Ranking_length"] = l
        for scale in Scale:
            print("scale = ", scale)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            d["shape_lower_limit"] = 1
            d["shape_upper_limit"] = 300
            for shape in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])):
                print("shape = ", shape)
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param=shape, scale_param=scale))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param=shape, scale_param=scale))
                Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param=shape, scale_param=scale))
            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)
                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), MRR_mean_random, color="red",
                         label="Random Rank Allocation")
                plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), MRR_mean_Asc, color="blue",
                         label="Ascending Rank Allocation")
                plt.plot(range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])), MRR_mean_Desc, color="green",
                         label="Descending Rank Allocation")

                plt.xlabel("Mean")
                plt.ylabel("MRR")
                plt.legend()
                plt.title("Gamma:Scale=" + str(scale) + " Pos=" + str(d["pos"]) + " Rl=" + str(
                    d["Ranking_length"]))
                plt.savefig(
                    "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Gamma Distribution/MRR/New Mean x axis MRR Gamma dist scale=" + str(
                        scale) + " pos= " + str(d["pos"]) + " R length= " + str(d["Ranking_length"]) + ".png")
                plt.show()

change_shape_gamma(Scale=[1,3], RL=[100], Pos=[0.5,0.7])
change_shape_gamma(Scale=[1], RL = [500])


####### vary the scale #####

def change_scale_gamma(Shape=list(),Pos=[0.5],RL=[100]):
    for l in RL:
        d["Ranking_length"] = l
        for shape in Shape:
            d["shape_lower_limit"]=1
            d["shape_upper_limit"]=60
            print("shape = ", shape)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            for scale in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"])):
                print("scale = ", scale)
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param=shape, scale_param=scale))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param=shape, scale_param=scale))
                Ranking_change_mean_Desc.append(
                    rankings(d, Order_by="Descending", shape_param=shape, scale_param=scale))


            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)

                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                plt.plot([np.sqrt(shape*i*i) for i in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"]))], MRR_mean_random, color="red",
                         label="Random Rank Allocation")
                plt.plot([np.sqrt(shape*i*i) for i in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"]))], MRR_mean_Asc, color="blue",
                         label="Ascending Rank Allocation")
                plt.plot([np.sqrt(shape*i*i) for i in range(int(d["shape_lower_limit"]), int(d["shape_upper_limit"]))], MRR_mean_Desc, color="green",
                         label="Descending Rank Allocation")
                plt.xlabel("Std")
                plt.ylabel("MRR")
                plt.legend()
                plt.title(
                    "Gamma:Shape=" + str(shape) + " Pos=" + str(d["pos"]) + " Rl=" + str(
                        d["Ranking_length"]))
                plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Gamma Distribution/MRR/New MRR Gamma Vary Scale shape=" + str(shape) + " pos= " + str(d["pos"]) + " R length= " + str(d["Ranking_length"]) + ".png")
                plt.show()

change_scale_gamma(Shape=[1],Pos=[0.5],RL=[100])




############################################################################################################################################################
#######################################################################################################################
# 04/09/2023 BETA DISTRIBUTIONS HAS BEEN PROPERLY FORMATTED
#######################################################################################################################

############################
### Beta Distribution #####
############################

# relation between alpha and beta determines the shape of the distribution
d["Type_distribution"] = "BETA"

### fix alpha and vary beta ###
### Ranking lenght 100 ##

def change_beta_mean (Alpha,RL=[100], Pos=[0.5]):
    for l in RL:
        d["Ranking_length"] = l
        for alpha in Alpha:
            print("alpha = ", alpha)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            d["beta_lower_limit"] = 1
            d["beta_upper_limit"] = 500
            r = list(range(1,500))
            for beta in r:
                print("beta = ", beta)
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)

                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                plt.plot([alpha/(i+alpha) for i in r], MRR_mean_random, color="red",
                         label="Random Rank Allocation")
                plt.plot([alpha/(i+alpha) for i in r], MRR_mean_Asc, color="blue",
                         label="Ascending Rank Allocation")
                plt.plot([alpha/(i+alpha) for i in r], MRR_mean_Desc, color="green",
                         label="Descending Rank Allocation")
                #plt.axhline(y=0.5, color='black', linestyle='-')
                plt.xlabel("Mean_beta")
                plt.ylabel("MRR")
                plt.legend()
                plt.title(
                    "Beta:Alpha=" + str(alpha) + " Pos=" + str(d["pos"]) + " Rl=" + str(
                        d["Ranking_length"]))
                plt.savefig(
                    "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/MRR/New MRR Beta Vary beta_mean alpha=" + str(
                        alpha) + " pos= " + str(d["pos"]) + " R length= " + str(d["Ranking_length"]) + ".png")
                plt.show()

change_beta_mean(Pos=[0.5],RL=[100],Alpha=[0.5,50])
change_beta_mean(Pos=[0.5],RL=[100],Alpha=[500]) #New


def std_beta_dist (alpha,beta):
    return np.sqrt((alpha*beta)/(((alpha+beta)**2)*(alpha+beta+1)))


def change_beta_std (Alpha,RL=[100], Pos=[0.5]):
    for l in RL:
        d["Ranking_length"] = l
        for alpha in Alpha:
            print("alpha = ", alpha)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            d["beta_lower_limit"] = 1
            d["beta_upper_limit"] = 500
            r = list(range(1,500))
            for beta in r:
                print("beta = ", beta)
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)

                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                plt.plot([std_beta_dist(alpha,i) for i in r], MRR_mean_random, color="red",
                         label="Random Rank Allocation")
                plt.plot([std_beta_dist (alpha,i) for i in r], MRR_mean_Asc, color="blue",
                         label="Ascending Rank Allocation")
                plt.plot([std_beta_dist (alpha,i) for i in r], MRR_mean_Desc, color="green",
                         label="Descending Rank Allocation")
                #plt.axhline(y=0.5, color='black', linestyle='-')
                plt.xlabel("Std_beta")
                plt.ylabel("MRR")
                plt.legend()
                plt.title(
                    "Beta:Alpha=" + str(alpha) + " Pos=" + str(d["pos"]) + " Rl=" + str(
                        d["Ranking_length"]))
                plt.savefig(
                    "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/MRR/New MRR Beta Vary beta alpha=" + str(
                        alpha) + " pos= " + str(d["pos"]) + " R length= " + str(d["Ranking_length"]) + ".png")
                plt.show()

change_beta_std(Pos=[0.5],RL=[100],Alpha=[0.5,50])




### fix beta and vary alpha ###

def change_alpha_mean(Beta=list(),RL=[100], Pos=[0.5]):
    for l in RL:
        d["Ranking_length"] = l
        for beta in Beta:
            print("beta = ", beta)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            d["alpha_lower_limit"]=1
            d["alpha_upper_limit"]=500
            r = list(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])))

            for alpha in r:
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)

                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                plt.plot([i/(i+beta)for i in r], MRR_mean_random, color="red",
                         label="Random Rank Allocation")
                plt.plot([i/(i+beta)for i in r], MRR_mean_Asc, color="blue",
                         label="Ascending Rank Allocation")
                plt.plot([i/(i+beta)for i in r], MRR_mean_Desc, color="green",
                         label="Descending Rank Allocation")
                #plt.axhline(y=0.5, color='black', linestyle='-')
                plt.xlabel("Mean_alpha")
                plt.ylabel("MRR")
                plt.legend()
                plt.title(
                    "Beta:Beta=" + str(beta) + " Pos=" + str(d["pos"]) + " Rl= " + str(
                        d["Ranking_length"]))
                plt.savefig(
                    "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/MRR/New MRR Beta dist Vary alpha_mean beta=" + str(
                        beta) + " pos= " + str(d["pos"]) + " R length= " + str(d["Ranking_length"]) + ".png")
                plt.show()

change_alpha_mean(Beta=[0.5, 5], Pos=[0.5], RL=[100])
change_alpha_mean(Beta=[0.5], Pos=[0.7], RL=[100])
change_alpha_mean(Beta=[0.5], Pos=[0.5], RL=[500])

def std_beta_dist (alpha,beta):
    return np.sqrt((alpha*beta)/(((alpha+beta)**2)*(alpha+beta+1)))


def change_alpha_std(Beta=list(),RL=[100], Pos=[0.5]):
    for l in RL:
        d["Ranking_length"] = l
        for beta in Beta:
            print("beta = ", beta)
            Ranking_change_mean_random = list()
            Ranking_change_mean_Asc = list()
            Ranking_change_mean_Desc = list()
            d["alpha_lower_limit"]=1
            d["alpha_upper_limit"]=500
            r = list(range(int(d["alpha_lower_limit"]), int(d["alpha_upper_limit"])))

            for alpha in r:
                Ranking_change_mean_random.append(rankings(d, Order_by="Random", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", shape_param1=alpha, shape_param2=beta))
                Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", shape_param1=alpha, shape_param2=beta))

            for pos in Pos:
                d["pos"] = pos
                print("pos= ", pos)

                MRR_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                # print("MRR_mean_random",MRR_mean_random)
                MRR_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                # print("MRR_mean_Asc", MRR_mean_Asc)
                MRR_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                # print("MRR_mean_Desc",MRR_mean_Desc)

                plt.plot([std_beta_dist(i,beta)for i in r], MRR_mean_random, color="red",
                         label="Random Rank Allocation")
                plt.plot([std_beta_dist(i,beta)for i in r], MRR_mean_Asc, color="blue",
                         label="Ascending Rank Allocation")
                plt.plot([std_beta_dist(i,beta)for i in r], MRR_mean_Desc, color="green",
                         label="Descending Rank Allocation")
                #plt.axhline(y=0.5, color='black', linestyle='-')
                plt.xlabel("Std_alpha")
                plt.ylabel("MRR")
                plt.legend()
                plt.title(
                    "Beta:Beta=" + str(beta) + " Pos=" + str(d["pos"]) + " Rl= " + str(
                        d["Ranking_length"]))
                plt.savefig(
                    "C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Beta Distribution/MRR/New MRR Beta dist Vary alpha_std beta=" + str(
                        beta) + " pos= " + str(d["pos"]) + " R length= " + str(d["Ranking_length"]) + ".png")
                plt.show()

change_alpha_std(Beta=[0.5],RL=[100], Pos=[0.5]) ### NEW

"""
####################################################################################################################################

##############################
### Bimodal Distribution #####
##############################
d = Load("Parameters.txt")

d["Type_distribution"] = "Bimodal"
## Same standard deviation vary mean: set standard deviation to 5, mean goes from 0 to 500 first with a gap of 50
#between the two normal distribution adn then a gap of 100. Porportion 0.5 at first then a proportion of 0.8 to the first
# and then a proportion of 0.9 to the second
                                        ##################### vary MEAN ###########################


##################### SAME STD ##############################
def change_mean_bim (std1,std2,RL=[100],Prop_dist=[0.5],Mean_diff=[10,50], Pos=[0.5]):
    for l in RL:
        d["Ranking_length"] = l
        #std1 = 5
        #std2 = 5
        d["mean_lower_limit"] = 0
        d["mean_upper_limit"] = 300
        for prop_dist in Prop_dist:
            print(prop_dist)
            d["p"] = prop_dist
            for mean_diff in Mean_diff:
                Ranking_change_mean_random = list()
                Ranking_change_mean_Asc = list()
                Ranking_change_mean_Desc = list()
                print(mean_diff)
                for mean in range(d["mean_lower_limit"],d["mean_upper_limit"]):
                    Ranking_change_mean_random.append(rankings(d, Order_by="Random", mean1=mean, std1=std1, mean2=mean+mean_diff, std2=std2))
                    Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", mean1=mean, std1=std1, mean2=mean+mean_diff, std2=std2))
                    Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", mean1=mean, std1=std1, mean2=mean+mean_diff, std2=std2))

                #print(MRR_change_mean_Asc)
                for pos in Pos:
                    d["pos"] = pos
                    print("pos= ", pos)
                    MRR_change_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                    # print("MRR_mean_random",MRR_mean_random)
                    MRR_change_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                    # print("MRR_mean_Asc", MRR_mean_Asc)
                    MRR_change_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                    # print("MRR_mean_Desc",MRR_mean_Desc)
                    #print(MRR_change_mean_random)

                    plt.plot([i*prop_dist+(1-prop_dist)*(i+mean_diff) for i in range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"]))], MRR_change_mean_random, color="red",
                             label="Random Rank Allocation")
                    plt.plot([i*prop_dist+(1-prop_dist)*(i+mean_diff) for i in range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"]))], MRR_change_mean_Asc, color="blue",
                             label="Ascending Rank Allocation")
                    plt.plot([i*prop_dist+(1-prop_dist)*(i+mean_diff) for i in range(int(d["mean_lower_limit"]), int(d["mean_upper_limit"]))], MRR_change_mean_Desc, color="green",
                             label="Descending Rank Allocation")
                    plt.xlabel("Mean")
                    plt.ylabel("MRR")
                    plt.legend()
                    plt.title("Bimod:"+"P= "+str(d["p"])+" Mean_diff="+ str(mean_diff) + " Std1=" + str(std1)+ " Std2="+ str(std2) + " Pos=" + str(d["pos"]) + " Rl=" + str(d["Ranking_length"]))
                    plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Bimodal Distribution/MRR/"+"New MRR BI"+"prop_dist="+str(d["p"])+"mean_range="+str([d["mean_lower_limit"],d["mean_upper_limit"]])+"mean_diff="+ str(mean_diff) + "std1=" + str(std1)+ "std2="+ str(std2) + " pos=" + str(d["pos"]) + " RL= " + str(d["Ranking_length"])+".png")
                    plt.show()

#change_mean_bim (1,7,RL=[100],Prop_dist=[0.5],Mean_diff=[10], Pos=[0.5])
#change_mean_bim (1,1,RL=[100],Prop_dist=[0.5],Mean_diff=[50], Pos=[0.5,0.7])
#change_mean_bim (1,20,RL=[100],Prop_dist=[0.5],Mean_diff=[50], Pos=[0.5])

#change_mean_bim(1,1,RL=[100],Prop_dist=[0.5],Mean_diff=[10], Pos=[0.5]) # New
change_mean_bim (1,1,RL=[500],Prop_dist=[0.5],Mean_diff=[50], Pos=[0.5]) # New
#change_mean_bim(1,7,RL=[100],Prop_dist=[0.5],Mean_diff=[50], Pos=[0.5]) #New



#Vary STD
def std_bim(std1,std_diff,p):
    return np.sqrt(p*(std1**2) + (1-p)*((std1+std_diff)**2))


def change_std_bim(mean1,mean2,std_diff=[5],RL=[100],Pos=[0.5],P=[0.5]):
    for l in RL:
        d["rank_length"] = l
        #mean1 = 100
        #mean2 = 100
        d["std1_lower_limit"] = 1
        d["std1_upper_limit"] = 60
        for prop_dist in P:
            d["p"] = prop_dist
            for std_diff in std_diff:
                Ranking_change_mean_random = list()
                Ranking_change_mean_Asc = list()
                Ranking_change_mean_Desc = list()
                print(std_diff)
                for std in range(d["std1_lower_limit"],d["std1_upper_limit"]):
                    Ranking_change_mean_random.append(rankings(d, Order_by="Random", mean1=mean1, std1=std, mean2=mean2, std2=std+std_diff))
                    Ranking_change_mean_Asc.append(rankings(d, Order_by="Ascending", mean1=mean1, std1=std, mean2=mean2, std2=std+std_diff))
                    Ranking_change_mean_Desc.append(rankings(d, Order_by="Descending", mean1=mean1, std1=std, mean2=mean2, std2=std+std_diff))

                #print(MRR_change_mean_Asc)
                for pos in Pos:
                    d["pos"] = pos
                    print("pos= ", pos)
                    MRR_change_mean_random = Measuring_quality(Ranking_change_mean_random, "MRR", d)
                    # print("MRR_mean_random",MRR_mean_random)
                    MRR_change_mean_Asc = Measuring_quality(Ranking_change_mean_Asc, "MRR", d)
                    # print("MRR_mean_Asc", MRR_mean_Asc)
                    MRR_change_mean_Desc = Measuring_quality(Ranking_change_mean_Desc, "MRR", d)
                    # print("MRR_mean_Desc",MRR_mean_Desc)
                    #print(MRR_change_mean_random)

                    plt.plot([std_bim(i,std_diff,prop_dist) for i in range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"]))], MRR_change_mean_random, color="red",
                             label="Random Rank Allocation")
                    plt.plot([std_bim(i,std_diff,prop_dist) for i in range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"]))], MRR_change_mean_Asc, color="blue",
                             label="Ascending Rank Allocation")
                    plt.plot([std_bim(i,std_diff,prop_dist) for i in range(int(d["std1_lower_limit"]), int(d["std1_upper_limit"]))], MRR_change_mean_Desc, color="green",
                             label="Descending Rank Allocation")
                    plt.xlabel("Std")
                    plt.ylabel("MRR")
                    plt.legend()
                    plt.title("Bimod:"+"P="+str(d["p"])+" Std_diff="+ str(std_diff) + " Mean1=" + str(mean1)+ " Mean2="+ str(mean2) + " Pos=" + str(d["pos"]) + " Rl=" + str(d["Ranking_length"]))
                    plt.savefig("C:/Users/ziedk/PycharmProjects/Master Thesis/Plots/Bimodal Distribution/MRR/"+"New MRR BI"+"prop_dist="+str(d["p"])+"std_range="+str([d["std1_lower_limit"],d["std1_upper_limit"]])+"std_diff="+ str(std_diff) + "mean1=" + str(mean1)+ "mean2="+ str(mean2) + " pos=" + str(d["pos"]) + " RL= " + str(d["Ranking_length"])+".png")
                    plt.show()
#change_std_bim(90,100,std_diff=[5],RL=[100],Pos=[0.5],P=[0.5]) #New

