import scipy.stats as stats

#expected value = 10, probability of observing 12 or more
prob1 = 1 - stats.poisson.cdf(11,10)
print("probability of raining for 12 or more days: ", prob1)

#expected value = 10, probability of observing 12-18
prob2 = stats.poisson.cdf(18,10) - stats.poisson.cdf(11,10)

print("probability of raining for 12-18 days: ", prob2)