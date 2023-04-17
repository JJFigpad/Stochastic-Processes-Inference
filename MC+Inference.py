#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:04:26 2023

@author: juanjose
"""

import numpy as np
#import matplotlib as mpl

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
    
    def expected_hitting_time(self, i, j):
        return 0

mc = F_MarkovChain(3)
mat = mc.transitionMatrix("0 1 0 1 0 0 1/2 1/2 0")
eh = mc.expected_hitting_time(2, 3)
print(mat)
print(mc.stationary_dist())
print(eh)