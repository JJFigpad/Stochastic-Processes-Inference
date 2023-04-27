#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:04:26 2023

@author: juanjose
"""

import random
import numpy as np
from matplotlib import pyplot as plt

class F_MarkovChain:
    """
    Class that represents a finite Markov Chain.
    """
    
    def __init__(self, n):
        self.n = n
        self.M = None
        self.initial_dist = None

    def __checkTM__(self, M):
        """
        

        Parameters
        ----------
        M : numpy.ndarray
            Transition matrix candidate.

        Returns
        -------
        bool
            True if it is a valid transition matrix. False otherwise.

        """
        for row in M:
            if sum(row) == 1 or (1-sum(row)) < 1e-12:
                return True
            else:
                return False

    def transitionMatrix(self, L):
        """
        
    
        Parameters
        ----------
        L : str
            String with all values of the nxn size matrix.
    
        Returns
        -------
        matrix : numpy array
            Transition Matrix in form of an array. The size and values of the matrix
            are the parameters.
    
        """
        
        values = L.split(" ")
        if len(values) != self.n**2:
            return("Error in values length")
        matrix = []
        for i in range(self.n):
            matrix.append([])
        counter = 0
        for i in range(self.n):
            for j in range(self.n):
                matrix[i].append(eval(values[counter]))
                counter += 1
        flag = self.__checkTM__(matrix)
        if not flag:
            return "The matrix given is not valid"
        self.M = np.array(matrix)
        return self.M

    
    def __checkID__(self, v):
        """
        

        Parameters
        ----------
        v : numpy.ndarray
            Initial distribution candidate.

        Returns
        -------
        bool
            True if it is a valid initial distribution. False in other case.

        """
        if sum(v) != 1:
            return False
        return True
    
    def init_dist(self, L):
        """
        
    
        Parameters
        ----------
        L : str
            String with all values of the nxn size matrix.
    
        Returns
        -------
        arr : numpy array
            Initial distribution of a MC in form of an array. The size and values
            of the matrix are the parameters.
    
        """
        
        values = L.split(" ")
        if len(values) != self.n:
            return("Error in values length")
        arr = []
        for i in range(self.n):
            arr.append(float(values[i]))
        flag = self.__checkID__(arr)
        if not flag:
            return "Invalid ID"
        self.initial_dist = np.array(arr)
        return self.initial_dist

    def stationary_dist(self):
        """
        

        Returns
        -------
        numpy array
            Stationary distribution of the Markov chain
            using Gaussian Elimination.

        """
        
        P = self.M.T - np.identity(self.n)
        P = np.vstack(([1]*self.n, P))
        P = np.delete(P, self.n, 0)
        vec = np.array([0]*self.n)
        vec[0] = 1
        return np.linalg.solve(P, vec)
    
    def state_classification(self):
        r = []
        for k in range(1, self.n):
            tempM = np.linalg.matrix_power(self.M, k)
            acc = []
            for i in range(self.n):
                temp_classes = []
                for j in range(self.n):
                    if tempM[i, j] > 0 and tempM[j, i] > 0:
                        if i not in temp_classes:
                            temp_classes.append(i)
                        if j not in temp_classes:
                            temp_classes.append(j)
                if temp_classes != []:
                    acc.append(sorted(temp_classes))
            if acc not in r:
                r.append(acc)
        c = 0
        r1 = []
        while c < len(r):
            tempC = []
            acc = []
            for i in r:
                tempC.append(i[c])
            for i in tempC:
                acc += i
            acc = sorted(list(set(acc)))
            c += 1
            if acc not in r1:
                r1.append(acc)
        return r1
    
    def __fund_matrix__(self, Q):
        """
        

        Parameters
        ----------
        Q : numpy.ndarray
            Q matrix of the canonical form of the transition matrix.

        Returns
        -------
        numpy.ndarray
            Fundamental Matrix.

        """
        return np.linalg.inv(-Q + np.identity(len(Q)))
    
    def expected_hitting_time(self, i, j):
        return (1-self.M[i,j])/self.M[i,j]
    
    def runProcess(self, i, j):
        choices = list(range(self.n))
        T = 0
        act_state = i
        while act_state != j:
            temp = random.choices(choices, weights=list(self.M[act_state]), k=1)[0]
            T += 1
            act_state = temp
        return T

mc = F_MarkovChain(3)
mat = mc.transitionMatrix("0.2 0.2 0.6 0.3 0 0.7 0.3 0.3 0.4")
ht = mc.expected_hitting_time(1, 0)
print(mat)
print(mc.stationary_dist())
print(mc.state_classification())
print(ht)

#Simulation
x = list(range(1, 501))
y = []
for i in range(1, 501):
    s = []
    for k in range(i):
        s.append(mc.runProcess(1, 0))
    p = 1/(1+(sum(s)/i))
    y.append((1-p)/p - 1)
plt.scatter(x, y)
plt.plot(x, [ht]*500, color="red")
plt.title("T_{ij} approximation")
plt.legend(["T_02", "q/p"])
plt.xlabel("Number of attempt")
plt.ylabel("Transition probability in n steps")
plt.show()