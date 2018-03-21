import random
import os
from itertools import combinations

#Source: https://stackoverflow.com/questions/40067386/how-to-obtain-the-nth-row-of-the-pascal-triangle
#Returns the nth row of Pascal's triangle
def pascaline(n):
    n = n - 1
    line = [1]
    for k in range(max(n ,0)):
        line.append(int(line[k]*(n-k)/(k+1)))
    return line

def probability(c,p):
    output = 0
    pascal = pascaline(c + 1)
    for i in range(0,c + 1):
        output += pascal[i] * (p ** i * (p-1) ** (c - 1))
    return output

def main():
    n_doctors = 3
    individual_prob = 0.8
    print(probability(n_doctors,individual_prob))

if(__name__ == '__main__'):
    main()