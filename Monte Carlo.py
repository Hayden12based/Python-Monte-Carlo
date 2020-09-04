

#generate future stock prices on given votalliy of price Monte carlos simunltaion of future outcomes
# Simple Monte Carlos python generate more outcomes



#caculte daliy returns


#excract last price



#hopin in simulation 
#number of trails



#how many days now





    #list append of prices of the dates 1 initcal start value
                    #first price = last price of the stock times 1 plus np.random.normal
     # norm nth function daily volatilitygenerate random prices
                                                     #append price to the list


      # next for loop y for num days count = 200 days we break 
   



                         
                                         
                                               

    






#create count 
#create df for trails of 1000, number of days break for loop once we reach 200 days
#extract daily stdev


import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2017, 10, 4)
end = dt.datetime(2017, 11, 20)

prices = web.DataReader('MSFT', 'yahoo', start, end)['Close']
returns = prices.pct_change()

last_price = prices[-1]

#Number of Simulations
num_simulations = 1000
num_days = 252

simulation_df = pd.DataFrame()

for x in range(num_simulations):
    count = 0
    daily_vol = returns.std()
    
    price_series = []
    
    price = last_price * (1 + np.random.normal(0, daily_vol))
    price_series.append(price)
    
    for y in range(num_days):
        if count == 251:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)
        count += 1
    
    simulation_df[x] = price_series
    
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: MSFT')
plt.plot(simulation_df)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()









