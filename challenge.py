#import matplotlib
import matplotlib.pyplot as plt
#import stats
from scipy import stats
#data for graph
x = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
y = [220.00, 330.00, 190.00, 340.00, 410.00, 445.00, 415.00]
#line of best fit
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
plt.xlabel("Temperature")
plt.ylabel("Price in  (R)")
plt.title("Soup sales in relation to temperature")
plt.plot(x, mymodel)
plt.scatter(x, y)
plt.show()


