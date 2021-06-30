#!/usr/bin/python 
# -*- coding: latin-1 -*-

import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,10,20)

print (x)

y = x ** 2.0
print(y)

y2 = x ** 1.5
print(y2)
plt.figure(figsize=(9, 3))

plt.plot(x,y,"bo-",linewidth=2,markersize=12,label="Elevado a 2")
plt.plot(x,y2,"gs-",linewidth=2,markersize=12, label = "Elevado a 1.5")


plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc = "upper left")

#plt.show()

plt.savefig("figura_ejemplo.png")
plt.close()