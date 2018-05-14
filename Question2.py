# Question 2
# a) Wtite a routine
import sys
def factorial(n): #define the factorial function
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
def binomial(n, k): #define the binomial function
    if (type(n) == float) or (type(n) == complex):
        return 'Arguement requires n is an integer'
    if (type(k) == float) or (type(k) == complex):
        return 'Arguement requires k is an integer'
    if k < 1: #if k < 1 then output 1
        return 1
    if k > n:
        return 'Arguement requires k is less than or equal to n'
    else: #otherwise output binomial function
        return factorial(n)/(factorial(k)*factorial(n-k))

binomial(n,k)

# b) write out firt 20 lines of Pascal's triangle
#print "First", x, "terms of Pascal's Triangle:"

x=1 #first define x, which represents the number of rows, as any integer


#now define a function which will give out the first x values Pascal's Triangle
def Pascal(x): 
    n = 0
    k = 0
    while n < x:
        PascalValues=[]
        while k < n:
            #print binomial(n,k)
            PascalValues.append(binomial(n,k))            
            k +=1
        while k == n:
            #print binomial(n,k)
  				PascalValues.append(binomial(n,k))          
            n +=1
            k =0
        print(PascalValues)
        
Pascal(20)

        
# c) For a biased coin with probabiliy p of coming up heads calculate//
# the probability of obtaining heads at least k times in n flips

# Define a function describing the probability of obtaining heads
# exactly k times out of n
p = 0.5
n = 2
k = 1

def Probk(p, n, k):
    if p > 1:
        return "probability must be less than 1"
    else:    
        return binomial(n,k) * p**k * (1-p)**(n-k)
        
# The probability of obtaining at least k times in n flips is
# 1-Probk(p,n,k)-Probk(p,n,k-1)-...-Probk(p,n,0)

prob = []
def ProbAtLeastk(p,n,k):
    while k <= n:
        prob.append(Probk(p,n,k))
        k+=1        
    print sum(prob)

ProbAtLeastk(0.5,3,0)


# d) Simulate the experiment N times, for large N, for each value of N 
# determine the fraction of successful experiments. Show the result in a plot 

import matplotlib.pyplot as plot
import random
import numpy

#define a list of outcome of flips
def trial(p,N):
    flips = []
    i = 1
    while i <= N:
        if random.random() < p:
            flips.append(1)
        else:
            flips.append(0)
        i+=1
    return flips

print trial(0.5,10)

#Determine the average number of trials which were successful
def Average(p,N):
    return sum(trial(p,N))/(N*1.0)

Average(0.5,10)

#Define a list of the average values of N trials for N increasing by 10 and plot it
def FractionofSuccesses(p,Nmax):
    Averages=[]
    Trials = []
    N = 10
    while N<=Nmax:
        Averages.append(Average(p,N))
        Trials.append(N)
        N+=10
    plot.plot(Trials,Averages)
    plot.ylabel('Fraction of Successes')
    plot.xlabel('Number of Trials')
    plot.title('Fraction of Successful Trials vs trials')
    plot.show()
    print Averages
    
FractionofSuccesses(0.5,1000)