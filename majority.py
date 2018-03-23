import random
import os
import matplotlib.pyplot as plt

#Source: https://stackoverflow.com/questions/40067386/how-to-obtain-the-nth-row-of-the-pascal-triangle
#Returns the nth row of Pascal's triangle
def pascaline(n):
    n = n - 1
    line = [1]
    for k in range(max(n ,0)):
        line.append(int(line[k]*(n-k)/(k+1)))
    return line

#Returns the probability that the majority of the experts are correct
def probability(c,p):
    output = 0
    pascal = pascaline(c - 1)
    if (c % 2 == 0):
        limit = int(c/2 + 1)
    else:
        limit = int(c/2 + 0.5)
    for i in range(0,limit):
        output += pascal[i] * (p ** (c-i) * (1-p) ** i)
    return output

def main():
    n_doctors = 15
    individual_prob = 0.6
    #1c.
    print(probability(n_doctors,individual_prob))

    #1d. Create plots for how the group size and individual competency
    #Graph 1, varying competency with group size 10
    competencies = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    plt.plot(competencies,[probability(10,p) for p in competencies])
    plt.xlabel("Competency of individual experts")
    plt.ylabel("Probability")
    plt.title("Probability of correct majority by individual competency with group size 10")
    plt.savefig('plot1.png');plt.clf()

    #Graph 2, varying group size with competency of 0.7
    group_sizes = [x * 10 for x in range(1,11)]
    plt.plot(group_sizes,[probability(s,0.7) for s in group_sizes])
    plt.xlabel("Probability of correct majority by group size")
    plt.ylabel("Probability")
    plt.title("Probability of correct majority by group size with individual probability 0.7")
    plt.savefig('plot2.png');plt.clf()

    #1e.
    plt.plot(range(0,40),[probability(c,0.6) for c in range(0,40)])
    plt.show()

if(__name__ == '__main__'):
    main()