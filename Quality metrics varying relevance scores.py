import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
from Quality_metrics import *
NDCG1 = list()
NDCG2 = list()
NDCG3 = list()
NDCG4 = list()
NDCG5 = list()
NDCG6 = list()

r = np.arange(10, 500)
for i in list(r):
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    v6 = 0
    for j in range(0,1000):

        #s1 = np.random.normal(0, 1, round(i))
        s2 = np.random.normal(20, 1, round(i))
        s3 = np.random.normal(40, 1, round(i))
        s4 = np.random.normal(60, 1, round(i))
        s5 = np.random.normal(80, 1, round(i))


        #v1+= NDCG(s1,round(i*0.3))
        v2+= NDCG(s2,round(i*0.3))
        v3+= NDCG(s3,round(i*0.3))
        v4+= NDCG(s4,round(i*0.3))
        v5+= NDCG(s5,round(i*0.3))

    #NDCG1.append(v1/1000)
    NDCG2.append(v2 / 1000)
    NDCG3.append(v3 / 1000)
    NDCG4.append(v4 / 1000)
    NDCG5.append(v5 / 1000)


#NDCG1n = [(i-min(NDCG1))/(max(NDCG1)-min(NDCG1))*(1+1)-1 for i in NDCG1]
#NDCG2n = [(i-min(NDCG2))/(max(NDCG2)-min(NDCG2))*(1+1)-1 for i in NDCG2]
#NDCG3n = [(i-min(NDCG3))/(max(NDCG3)-min(NDCG3))*(1+1)-1 for i in NDCG3]
#NDCG4n = [(i-min(NDCG4))/(max(NDCG4)-min(NDCG4))*(1+1)-1 for i in NDCG4]

#plt.plot(r,[0 if i<0 else i for i in NDCG1],color ="blue", label ="mean=0 std=1")
plt.plot(r,[0 if i<0 else i for i in NDCG2],color ="red", label ="mean=20 std=1")
plt.plot(r,[0 if i<0 else i for i in NDCG3],color ="green", label="mean=40 std=1")
plt.plot(r,[0 if i<0 else i for i in NDCG4],color ="yellow", label="mean=60 std=1")
plt.plot(r,[0 if i<0 else i for i in NDCG5],color ="orange", label="mean=80 std=1")

plt.legend()
plt.xlabel("ranking length")
plt.ylabel("NDCG")
plt.title("NDCG: variation of relevance score distribution")
plt.show()





