README file for test_bayes_factor.py unit testing of bayes_factor.py 
Rochelle Kaper rkaper@uci.edu 

The unit test script is test_bayes_factor.py which is in COGS205-complabskills/bayes_factor/tests. It tests the validation of input,
range of numbers, etc., and generally whether the different functions in test_bayes_factor.py are working 
as intended. 

You can test the functions in various ways:

1) Under setUp, there is an BayesFactor class used that can be accessed in the different functions using n=20 and k = 4. These numbers can be changed.

2) Where this global BayesFactor class is used (defined as bf and referenced as self.bf), other functions outside of init are tested
(e.g., evidence_spike, evidence_slab, bayes_factor). When these functions are tested, they take in different a and b parameters as input. These can be changed to be tested (i.e., changing numbers, testing non-numeric inputs, etc.). For instance def test_theta_between_0_to_1(self) tests self.bf.likelihood(theta) -- whatever theta you decide to test. 

3) In several of the functions, a new BayesFactor class is defined to test the input of n and k. You can try different numbers, non-numeric inputs, etc. 

Whenever a test fails, the code will output telling you what function failed and why, and these are titled specifically so you can see what went wrong. 

There are 2 purposefully failing tests:
a. test_bayes_factor_returns_spike_over_slab_ratio that returns slab over spike erroneously, 
b. test_evidence_spike_multiplied_by_1_over_c that does not mulitply by 1/c erroneously. 

To run the unit testing, you cd into the folder where the files are stored:
`cd /COGS205-complabskills/bayes_factor`

and run the Dockerfile. Put this lines in your terminal (without the backticks): 
`docker build -t bayes_factor .`