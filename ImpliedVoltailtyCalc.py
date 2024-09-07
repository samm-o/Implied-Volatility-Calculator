from scipy.optimize import fmin
import numpy as np
import scipy.stats as si

def NORMSDIST(x):
    NORMSDIST = si.norm.cdf(x,0.0,1.0)
    return(NORMSDIST)

S = 60 # Stock Price
X = 65 # Strike Price
r = 0.08 # Risk-Free Interest-Rate
T = 0.25 # Time to Maturity (in years)
cm = 4 # Call Option Market Price
pm = 8 # Put Option Market Price

def ImpliedVolatilityCall(s):
    d1 = ( (np.log(S/X)+(r+0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    d2 = ( (np.log(S/X)+(r-0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    of = ( S*NORMSDIST(d1) - X*np.exp(-r*T)*NORMSDIST(d2) ) - cm
    val = of**2
    print("[σ]=",s,", Object Function Value:", val)
    return(val)

def ImpliedVolatilityPut(s):
    d1 = ( (np.log(S/X)+(r+0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    d2 = ( (np.log(S/X)+(r-0.5*s[0]**2)*T) / (s[0]*np.sqrt(T)) )
    of = (  X*np.exp(-r*T)*NORMSDIST(-d2) - S*NORMSDIST(-d1) ) - pm
    val = of**2
    print("[σ]=",s,", Object Function Value:", val)
    return(val)

print("Do you want to see implied volatility for a call or put option?")
if input("Enter 'C' for call and 'P' for put: ") == 'C':
    c = fmin(ImpliedVolatilityCall, [0.3])
else:
    p = fmin(ImpliedVolatilityPut, [0.3])