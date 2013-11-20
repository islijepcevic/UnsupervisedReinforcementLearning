import math
import pylab as pl
import matplotlib.pyplot as plt

x = pl.linspace(-5,5,100)
y = x**2-x

fig= pl.figure()
pl.plot(x,y)
pl.xlabel('$\omega$')
pl.ylabel('$\dot\omega$')
pl.hold(True)
plt.axhline(y=0, linewidth=1, color='k')
plt.axvline(x=0, linewidth=1, color='k')
plt.title('$\dot \omega $ as a function of $ \omega $ for p=0')
pl.axis([-5.0, 6.0, -5.0, 15.0])  # [tmin, tmax, ymin, ymax]
pl.savefig('p0.png')
pl.show()

