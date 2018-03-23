# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:09:49 2018

@author: tpaye
"""

from scipy.special import comb
import math
import matplotlib.pyplot as plt


#Returns the probability that the majority of the experts are correct
def probability(c,p):
    majority = math.ceil(c/2)
    sum = 0
    for r in range(majority, c):
        sum += comb(c, r) * p ** r * (1-p)**(c-r)
    return sum


#1d. Create plots for how the group size and individual competency
#Graph 1, varying competency with group size 10
competencies = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
plt.plot(competencies,[probability(10,p) for p in competencies])
plt.xlabel("Competency of individual experts")
plt.ylabel("Probability")
plt.title("Probability of correct majority by individual competency with group size 10")
#plt.savefig('plot1.png');
plt.clf()

#Graph 2, varying group size with competency of 0.7
group_sizes = [x * 10 for x in range(1,11)]
plt.plot(group_sizes,[probability(s,0.7) for s in group_sizes])
plt.xlabel("Probability of correct majority by group size")
plt.ylabel("Probability")
plt.title("Probability of correct majority by group size with individual probability 0.7")
#plt.savefig('plot2.png');
plt.clf()

#1e.
plt.plot(range(0,40),[probability(c,0.6) for c in range(0,40)])
plt.show()