
# coding: utf-8

# In[ ]:

from QuantLib import *


# In[ ]:

todaysDate = Date.todaysDate()
Settings.instance().evaluationDate = todaysDate
settlementDate = todaysDate + Period(2, Days)
riskFreeRate = FlatForward(settlementDate, 0.00, Actual365Fixed())

# option parameters
exercise = EuropeanExercise(settlementDate)
payoff = PlainVanillaPayoff(Option.Call, 355.0)


# In[ ]:

settlementDate
payoff(367.0)


# In[ ]:

timestamp = Date.universalDateTime()
newtime = timestamp + Period(3, Years)
newtime.year()
dcc = ContinuousTime(Years)


# In[ ]:

import numpy as np
import matplotlib.pyplot as plt

def option(strike, vol, t, putcall):
    now = Date.universalDateTime()
    Settings.instance().evaluationDate = now
    settlementDate = todaysDate + Period(3, Weeks)
    riskFreeRate = FlatForward(settlementDate, 0.00, ContinuousTime.perDay())

    # option parameters
    exercise = EuropeanExercise(settlementDate)
    payoff = PlainVanillaPayoff(Option.Call, strike)

    volatility = BlackConstantVol(todaysDate, TARGET(), vol, ContinuousTime.perDay())
    dividendYield = FlatForward(settlementDate, 0.00, ContinuousTime.perDay())
    underlying = SimpleQuote(0.0)
    process = BlackScholesMertonProcess(QuoteHandle(underlying),
                                    YieldTermStructureHandle(dividendYield),
                                    YieldTermStructureHandle(riskFreeRate),
                                    BlackVolTermStructureHandle(volatility))
    option = VanillaOption(payoff, exercise)
    # method: analytic
    option.setPricingEngine(AnalyticEuropeanEngine(process))
    return (option, underlying)

def plotme(option, underlying, strike):
    x = np.arange(strike*0.8, strike*1.2, 0.01);
    def myfunc(x):
        underlying .setValue(x)
        return option.NPV()
    def mydelta(x):
        underlying.setValue(x)
        return option.delta()
    def mytheta(x):
        underlying.setValue(x)
        return option.theta()
    plt.figure(1, figsize=(10,8))
    plt.subplot(221)
    y = list(map(payoff, x))
    plt.plot(x, y)
    plt.plot(x, list(map(myfunc,x)))
    plt.subplot(222)
    plt.plot(x, list(map(mydelta,x)))
    plt.subplot(223)
    plt.plot(x, list(map(mytheta,x)))


# In[ ]:

get_ipython().magic('matplotlib inline')
(o, u) = option(350, 0.02, 90, 1)
plotme(o, u, 350)


# In[ ]:

np.arange(0.8, 1.2,0.1)


# In[ ]:



