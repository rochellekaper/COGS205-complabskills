from scipy import integrate
from scipy.stats import binom
import unittest
from bayes_factor import BayesFactor

class TestBayesFactor(unittest.TestCase):
    def setUp(self):
        self.bf = BayesFactor(20, 4)

    def test_n_is_integer(self):
        with self.assertRaises(TypeError):
            BayesFactor('porcupine', 10)
        BayesFactor(100, 10)
        
    def test_k_is_integer(self):
        with self.assertRaises(TypeError):
            BayesFactor(17, 0.9)
        BayesFactor(100, 10)
    
    def test_init_k_smaller_than_n(self):
        with self.assertRaises(ValueError):
            BayesFactor(3, 10)
        BayesFactor(100, 10)
        return
    
    def test_init_k_nonnegative(self):
        with self.assertRaises(ValueError):
            BayesFactor(3, -19)
        BayesFactor(100, 10)
        return
    
    def test_init_n_nonnegative(self):
        with self.assertRaises(ValueError):
            BayesFactor(-1, 6)
        BayesFactor(100, 10)
        return
    
    def test_n_and_k_are_stored_in_self(self):
        bf = BayesFactor(100, 10)
        self.assertEqual(bf.n, 100)
        self.assertEqual(bf.k, 10)
    
    def test_theta_between_0_to_1(self):
        with self.assertRaises(ValueError):
            self.bf.likelihood(-0.0001)
        self.bf.likelihood(0.5)
        return
    
    def test_likelihood_theta_at_zero(self):
        bf1 = BayesFactor(5, 0)
        expected = binom.pmf(0, 5, 0)
        actual = bf1.likelihood(0)
        self.assertAlmostEqual(actual, expected)
    
    def test_likelihood_theta_at_one(self):
        bf1 = BayesFactor(50, 50)
        expected = binom.pmf(50, 50, 1)
        actual = bf1.likelihood(1)
        self.assertAlmostEqual(actual, expected)

    def test_evidence_slab_a_is_numeric(self):
        with self.assertRaises(TypeError):
            self.bf.evidence_slab('porcupine', 0.4)
        self.bf.evidence_slab(0.4, 0.6)
        return
    
    def test_evidence_slab_b_is_numeric(self):
        with self.assertRaises(TypeError):
            self.bf.evidence_slab(0.05, '7')
        self.bf.evidence_slab(0.05, 0.1)
        return
    
    def test_evidence_slab_a_between_0_and_1(self):
        with self.assertRaises(ValueError):
            self.bf.evidence_slab(-1, 0.0004)
        self.bf.evidence_slab(0.5, 0.65)
        return
    
    def test_evidence_slab_b_between_0_and_1(self):
        with self.assertRaises(ValueError):
            self.bf.evidence_slab(0.3, 1.0001)
        self.bf.evidence_slab(0.3, 1)
        return
    
    def test_evidence_slab_a_less_than_b(self):
        with self.assertRaises(ValueError):
            self.bf.evidence_slab(0.41, 0.4)
        return

    def test_evidence_slab_nonnegative(self):
        actual = self.bf.evidence_slab()
        self.assertGreaterEqual(actual, 0)
        return
    
    def test_evidence_spike_a_is_numeric(self):
        with self.assertRaises(TypeError):
            self.bf.evidence_spike('porcupine', 0.5)
        self.bf.evidence_spike(0.4, 0.43)
        return
    
    def test_evidence_spike_b_is_numeric(self):
        with self.assertRaises(TypeError):
            self.bf.evidence_spike(0.05, '7')
        self.bf.evidence_spike(0.4, 0.43)
        return
    
    def test_evidence_spike_a_between_0_and_1(self):
        with self.assertRaises(ValueError):
            self.bf.evidence_spike(-1, 0.0004)
        self.bf.evidence_spike(0.4, 0.43)
        return
    
    def test_evidence_spike_b_between_0_and_1(self):
        with self.assertRaises(ValueError):
            self.bf.evidence_spike(0.3, 1.0001)
        self.bf.evidence_spike(0.4, 0.43)
        return
    
    def test_evidence_spike_a_less_than_b(self):
        with self.assertRaises(ValueError):
            self.bf.evidence_spike(0.41, 0.4)
        self.bf.evidence_spike(0.4, 0.43)
        return

    def test_evidence_spike_nonnegative(self):
        actual = self.bf.evidence_spike(0.001, 0.2)
        self.assertGreaterEqual(actual, 0)
        return
    
    def test_evidence_spike_multiplied_by_1_over_c(self):
        a = 0.4999
        b = 0.5001
        c = b - a 
        result, x = integrate.quad(self.bf.likelihood, a, b)
        expected = (1 / c) * result
        result_a, x = integrate.quad(self.bf.likelihood, a, b)
        actual = c * result_a
        self.assertEqual(expected, actual)
        return

    def test_bayes_factor_returns_1_if_equal_priors(self):
        bf1 = BayesFactor(20, 4)
        self.assertAlmostEqual(bf1.bayes_factor(0, 1, 0, 1), 1.0)
        return
    
    def test_bayes_factor_returns_spike_over_slab_ratio(self):
        bf1 = BayesFactor(20, 4)
        slab  = bf1.evidence_slab()
        spike = bf1.evidence_spike()
        actual = slab / spike #fail on purpose
        expected = bf1.bayes_factor()
        self.assertEqual(expected, actual)
        return
    
    def test_bayes_factor_positive(self):
        actual = self.bf.bayes_factor()
        self.assertGreater(actual, 0)

    def test_likelihood_returns_float(self):
        actual = self.bf.likelihood(0.5)
        self.assertIsInstance(actual, float)

    def test_evidence_slab_returns_float(self):
        actual  = self.bf.evidence_slab()
        self.assertIsInstance(actual, float)

    def test_evidence_spike_returns_float(self):
        actual = self.bf.evidence_spike()
        self.assertIsInstance(actual, float)

    def test_bayes_factor_returns_float(self):
        actual  = self.bf.bayes_factor()
        self.assertIsInstance(actual, float)

    def test_methods_are_callable(self):
        self.assertTrue(callable(self.bf.likelihood))
        self.assertTrue(callable(self.bf.evidence_slab))
        self.assertTrue(callable(self.bf.evidence_spike))
        self.assertTrue(callable(self.bf.bayes_factor))