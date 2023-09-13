
import numpy as np
import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(6,4))

sns.distplot(random.gamma(1,1,10000), hist=False)
sns.distplot(random.gamma(1,2,10000), hist=False)
sns.distplot(random.gamma(1,3,10000), hist=False)
sns.distplot(random.gamma(1,6,10000), hist=False)
sns.distplot(random.gamma(1,10,10000), hist=False)


fig.legend(labels=['Scale=1','Scale=2',"Scale=3","Scale=6","Scale=10"], bbox_to_anchor=(0.8, 0.85))
plt.title("Varying Relevance Score Distribution: Gamma Distribution")
plt.xlabel("Relevance Score")
plt.show()







