from scipy.stats import binom
from scipy import integrate

class BayesFactor:
    def __init__(self, n, k):
        #should do type and range checks 
        self.n = n
        self.k = k 

        attributes = [n, k]
        if not all(isinstance(x, (int)) for x in attributes):
            raise TypeError("all inputs must be integers")
        
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
    
    def evidence_slab(self, a=0, b=1):
        attributes = [a, b]
        if not all(isinstance(x, (int, float)) for x in attributes):
            raise TypeError("all inputs must be floats or integers")
        
        if a < 0 or a > 1:
            raise ValueError("a must be between 0 - 1 (inclusive)")
        if b < 0 or b > 1:
            raise ValueError("b must be between 0 - 1 (inclusive)")
        if a >= b:
            raise ValueError("a must be less than b")
        slab, error = integrate.quad(self.likelihood, a, b)
        return slab
    
    def evidence_spike(self, a=0.4999, b=0.5001):
        attributes = [a, b]
        if not all(isinstance(x, (int, float)) for x in attributes):
            raise TypeError("all inputs must be floats or integers")
    
        if a < 0 or a > 1:
            raise ValueError("a must be between 0 - 1 (inclusive)")
        if b < 0 or b > 1:
            raise ValueError("b must be between 0 - 1 (inclusive)")
        
        if a >= b:
            raise ValueError("a must be less than b")
        c = b - a 
        result, error = integrate.quad(self.likelihood, a, b)
        spike = (1 / c) * result
        return spike
    
    def bayes_factor(self, a_slab=0, b_slab=1, a_spike=0.4999, b_spike=0.5001):
        slab = self.evidence_slab(a_slab, b_slab)
        spike  = self.evidence_spike(a_spike, b_spike)
        return spike / slab