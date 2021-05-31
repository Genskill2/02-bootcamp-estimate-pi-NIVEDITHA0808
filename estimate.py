import math
import unittest
import random

# wallis function

def wallis(i):
    
    product = 1
    for n in range(1,i):
        
        product = product*(((2*n)/((2*n)+1)) * ((2*n)/((2*n)-1)))
    return(2*product)
# Unit Testing of wallis function      
class Test_Wallis(unittest.TestCase):
    
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")

# monte_carlo function

def monte_carlo(i):
    
    inside_the_circle = 0
    
    for n in range(1,i):
       x= random.random()
       y= random.random()
       q = (x**2)+(y**2)
       p = math.sqrt(q)
       if p<=1:
          inside_the_circle += 1
    
    pi = (4*(inside_the_circle/i))
    
    return(pi)
# Unit Testing of monte_carlo function 
class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
       
  
if __name__ == "__main__":
    unittest.main()


