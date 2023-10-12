import math
import numpy as np
import matplotlib.pyplot as plt

n1=1.325462301
n2=1.326154871
n3=1.334365534
n4=1.33657421
n5=1.3376125669
n6=1.340853238
n7=1.347315414

l1=671.67*10**(-9)
l2=648.09*10**(-9)
l3=571.40*10**(-9)
l4=488.68*10**(-9)
l5=464.52*10**(-9)
l6=456.13*10**(-9)
l7=445.40*10**(-9)

plt.figure()
plt.plot(l1,n1,"ro")
plt.plot(l2,n2,"ro")
plt.plot(l3,n3,"ro")
plt.plot(l4,n4,"ro")
plt.plot(l5,n5,"ro")
plt.plot(l6,n6,"ro")
plt.plot(l7,n7,"ro")
plt.title("lambda-n")
plt.xlabel("lambda")
plt.ylabel("n")
plt.legend(['mjerenja'])
plt.grid()

plt.show()