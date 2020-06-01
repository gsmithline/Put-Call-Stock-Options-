
# coding: utf-8

# In[1]:


#non dividend paying 
import numpy as np
import scipy.stats as si
import sympy as sy 
from sympy.stats import Normal, cdf 
from sympy import init_printing
init_printing()


# In[5]:


#non dividend paying 
def european_call(S, X, R, T, sigma):
    #S=stock price 
    #X=excercise price 
    #R=risk-free interest rate 
    #T=time to expiration
    #sigma=standard deviation of log returns -> volatility 
    
    deriv1= (np.log(S / X) + (R + .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    deriv2 = (np.log(S / X) + (R - .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(deriv1, 0, 1) - X * np.exp(-R * T) * si.norm.cdf(deriv2, 0, 1))
    
    return call


# In[6]:


european_call()


# In[7]:


#non dividend paying
def european_put(S, X, R, T, sigma):
    #S=stock price 
    #X=excercise price 
    #R=risk-free interest rate 
    #T=time to expiration
    #sigma=standard deviation of log returns -> volatility 
    
    deriv1= (np.log(S / X) + (R + .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    deriv2 = (np.log(S / X) + (R - .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    
    put = (X * np.exp(-R * T) * si.norm.cdf(-deriv2, 0, 1) - S * si.norm(-deriv2, 0, 1))
    
    return put


# In[8]:


european_put()


# In[12]:


#non dividend paying
def european_fut(S, X, R, T, sigma, option = ""):
     #S=stock price 
    #X=excercise price 
    #R=risk-free interest rate 
    #T=time to expiration
    #sigma=standard deviation of log returns -> volatility 
    #option=call or option 
    number=""
    understand = (number, 0, 1)
    
    deriv1= (np.log(S / X) + (R + .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    deriv2 = (np.log(S / X) + (R - .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    
    if option == "call":
        answer =  (S * si.norm.cdf(deriv1, 0, 1) - X * np.exp(-R * T) * si.norm.cdf(deriv2, 0, 1))
    if option == 'put':
        answer = (X * np.exp(-R * T) * si.norm.cdf(-deriv2, 0, 1) - S * si.norm(-deriv2, 0, 1))
        


# In[16]:





# In[17]:


def black_scholes_divid(S, X, R, T, q, sigma, option = ""):
    #S=stock price 
    #X=excercise price 
    #R=risk-free interest rate 
    #T=time to expiration
    #sigma=standard deviation of log returns -> volatility 
    # q= rate of continous dividend paying asset 
    #option=call or option 
    
    deriv1= (np.log(S / X) + (R + .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    deriv2 = (np.log(S / X) + (R - .5 * sigma ** 2) * T / sigma * np.sqrt(T))
    
    if option == "call":
        answer =  (S * si.norm.cdf(deriv1, 0, 1) - X * np.exp(-R * T) * si.norm.cdf(deriv2, 0, 1))
    if option == 'put':
        answer = (X * np.exp(-R * T) * si.norm.cdf(-deriv2, 0, 1) - S * si.norm(-deriv2, 0, 1))
        
    return answer

    
    
    
    
    
    

