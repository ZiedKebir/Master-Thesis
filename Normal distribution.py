import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns





s1 = np.random.normal(0, 1, 10000000)
s2 = np.random.normal(4,1,10000000)



fig = plt.figure()
#plt.hist(s1, edgecolor='black', weights=np.ones_like(s1) / len(s1))
#plt.hist(s2, edgecolor='red', weights=np.ones_like(s2) / len(s2))
#plt.hist(s3, edgecolor='red', weights=np.ones_like(s3) / len(s3))

sns.distplot(s1, hist=False, kde=True,
             kde_kws={'linewidth': 1})

sns.distplot(s2, hist=False, kde=True,
             kde_kws={'linewidth': 1})

#sns.distplot(s3, hist=False, kde=True,
#             kde_kws={'linewidth': 1})

plt.legend(["mean = 0, s=1","mean = 4, s=1"], loc="upper right", prop={'size':8})
plt.title("Varying Relevance Score Distribution: Normal Distribution")
plt.axvline(x = 0, color = 'r', label = 'axvline - full height', ls="--")

plt.show()



