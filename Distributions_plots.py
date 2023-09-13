import numpy as np
import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt


# Uniform distribution


# Unifrom distribution

# importing library

from scipy.stats import uniform

numargs = uniform.numargs
a, b = 0, 1
rv = uniform(a, b)

print("RV : \n", rv)

import numpy as np

quantile = np.arange(0.01, 1, 0.1)

# Random Variates
R = uniform.rvs(a, b, size=10)
print("Random Variates : \n", R)

# PDF
x = np.linspace(uniform.ppf(0.01, a, b),
                uniform.ppf(0.99, a, b), 10)
R = uniform.pdf(x, 1, 3)
print("\nProbability Distribution : \n", R)

import numpy as np
import matplotlib.pyplot as plt

distribution = np.linspace(0, np.minimum(rv.dist.b, 3))
print("Distribution : \n", distribution)

plot = plt.plot(distribution, rv.pdf(distribution))

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 2, 100)

# Varying positional arguments
y1 = uniform.pdf(x, a, b)
y2 = uniform.pdf(x, a, b)
plt.plot(x, y1, x, y2, color = "#1f77b4")
plt.xlim(-0.5,1.5)
plt.xlabel("Relevance Score")
plt.ylabel("Density")
plt.title("Varying Relevance Score Distribution: Uniform Distribution")
plt.show()

# Normal distribution

N = np.random.normal(0, 1, 10000000)

fig = plt.figure()


sns.distplot(N, hist=False, kde=True,
             kde_kws={'linewidth': 1})
plt.title("Varying Relevance Score Distribution: Normal Distribution")
plt.xlabel("Relevance Score")
plt.axvline(x = 0, color = 'r', label = 'axvline - full height', ls="--")

plt.show()

# Exponential distribution
sns.distplot(random.exponential(size=10000), hist=False)
plt.title("Varying Relevance Score Distribution: Exponential Distribution")
plt.xlabel("Relevance Score")
plt.show()


# Gamma distribution

sns.distplot(random.gamma(2,2,10000), hist=False)
plt.title("Varying Relevance Score Distribution: Gamma Distribution")
plt.xlabel("Relevance Score")
plt.show()



# beta distribution


sns.distplot(random.beta(2,2,10000), hist=False)
plt.title("Varying Relevance Score Distribution: beta Distribution")
plt.xlabel("Relevance Score")
plt.show()

# Bimodal Distribution


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Generate 10000 random numbers from a bimodal distribution
bimodal_data = np.concatenate((np.random.normal(3, 1, 5000), np.random.normal(10, 1, 5000)))

# Estimate the probability density function using kernel density estimation
pdf = gaussian_kde(bimodal_data)

# Generate x-values to plot the estimated PDF
x_values = np.linspace(0, 14, 1000)

# Plot the estimated PDF as a line plot
plt.plot(x_values, pdf(x_values))
plt.xlabel('Relevance Score')
plt.ylabel('Density')
plt.title('Varying Relevance Score Distribution: Bimodal Distribution')
plt.show()