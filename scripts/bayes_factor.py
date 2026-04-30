from scipy.stats import binom
from scipy import integrate
from copy import deepcopy

class BayesFactor:
    def __init__(self, n, k):
        #should do type and range checks 
        self.n = n
        self.k = k 

        attributes = [n, k]
        if not all(isinstance(x, (int)) for x in attributes):
            raise ValueError("all inputs must be integers")
        
        if n < 0:
            raise ValueError("number of trials (n) must be larger than 0")
        
        if k < 0:
            raise ValueError("number of successes (k) must be larger than 0")
        
        if k > n:
            raise ValueError("number of successes (k) cannot be larger than number of trials (n)")

    def likelihood(self, theta):
        if theta < 0 or theta > 1:
            raise ValueError("theta must be between 0 - 1 (inclusive)")
        
        return binom.pmf(self.k, self.n, theta)
    
    def evidence_slab(self):
        return integrate.quad(self.likelihood, 0, 1)
    
    def evidence_spike(self, a = 0.4999, b = 0.5001):
        c = b - a 
        return (1 / c) * (integrate.quad(self.likelihood, a, b))
    
    def bayes_factor(self):
        
        return self.evidence_spike() / self.evidence_slab()