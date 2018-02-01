
# Central Limit Theorem Illustration

# THEOREM
# ==========
# Tells us that the sampling distribution of the sample mean is, at least approximately, 
# normally distributed, regardless of the distribution of the underlying random sample.
# The maean of this distribution of samples means is EQUAL to the population mean
# The variance of this (new) mean of distributions is EQUAL to the (population variance / N)
# [The error with respect to the population mean decreases as N increases]
# where N is the sample size
# NOTE:
# (1) The larger the sample size N, the smaller the variance of the sample mean.
# (2) If the underlying distribution is skewed, then you need a larger sample size, typically N > 30
#     for the results to hold
# (3) This is only applicable to the Mean, variances follow the Chi-squared distribution
#
# https://onlinecourses.science.psu.edu/stat414/node/177
# EXTRA:
# The sampling distribution of the sample variance is a chi-squared distribution with degree of 
# freedom equals to N−1, where N is the sample size
# The chi-squared distribution looks skewed compared to normal distribution
# http://onlinestatbook.com/2/chi_square/distribution.html
#

# population size
P = 50000
# sample size --> Increase this to getter closer to ideal results
N = 40
# sample count --> This is also important in practise
C = 1000



## ----- Setup the population ----
# Select any probability function and convert it to discrete form with P points

# (1) Exponential function - change the factor from 1 - 100 to increase skew
# Sequential sampling of the PD function
pd = exp(seq(from = 0.0, to = 10.0, by = 10.0/P))
# Random sampling of the PD function
#pd = exp(runif(P, 0.0, 10.0))

# (2) Ramp function
#pd = seq(from = 0.0, to = 10.0, by = 10.0/P)

# (3) Sine function
#pd = sin(seq(from = 0.0, to = 2*pi, by = 2*pi/P))

# Allocate a matrix to hold the subsample data
s = matrix(0,C,N)

## ----- Take C subsamples of same size from the population ----
for (i in 1:C) {
  # Create a matrix of random indices with subsample size
  idx = matrix(sample(c(1:P), size = N, replace = TRUE))
  # Select random samples from our probability function
  s[i,] = pd[idx]
  s[i,]
}

# Now s[] contains C subsamples from the population pd
# Lets do some statistics on the subsamples

par(mfrow=c(3,1))
plot(pd,main="Probability Distribution")
## MEAN
hist(rowMeans(s), plot = TRUE, main = sprintf("Histogram of sample means (N=%i)", N))
## Lets calculate the variance of all the samples
v_s = apply(s, 1, var)
hist(v_s, plot = TRUE, main = "Histogram of sample variances")

print("==========================\n")
buf = sprintf("Population:\t Mean = %f, Variance = %f, Variance/N = %f\n", mean(pd), var(pd), var(pd)/(N))
cat(buf)
buf = sprintf("Sample Means:\t Mean = %f, Variance = %f\n", mean(rowMeans(s)), var(rowMeans(s)))
cat(buf)
print("==========================\n")
