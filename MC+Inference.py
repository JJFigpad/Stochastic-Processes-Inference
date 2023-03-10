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

    def __checkTM__(self, M):
        """
        

        Parameters
        ----------
        M : TYPE
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        for row in M:
            if sum(row) != 1:
                return False
        return True

    def transitionMatrix(self, L):
        """
        
    
        Parameters
        ----------
        n : int
            size of square matrix.
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
                matrix[i].append(float(values[counter]))
                counter += 1
        flag = self.__checkTM__(matrix)
        if not flag:
            return "The matrix given is not valid"
        return np.array(matrix)
    
    def __checkID__(self, v):
        """
        

        Parameters
        ----------
        v : TYPE
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        if sum(v) != 1:
            return False
        return True
    
    def init_dist(self, L):
        """
        
    
        Parameters
        ----------
        n : int
            size of square matrix.
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
        return np.array(arr)

    def stationary_dist(self, P):
        """
        

        Parameters
        ----------
        P : numpy matrix
            Transition matrix of the Markov chain.

        Returns
        -------
        numpy array
            Stationary distribution of the Markov chain
            using Gaussian Elimination.

        """
        
        n = P.shape[0]
        P_new = np.column_stack((P, np.identity(n)))
        for i in range(n):
        # Find the row with the largest absolute value in the i-th column
            max_row = i
            for j in range(i+1, n):
                if abs(P_new[j, i]) > abs(P_new[max_row, i]):
                    max_row = j
            # Swap the i-th and max_row-th rows
            P_new[[i, max_row], :] = P_new[[max_row, i], :]
            # Eliminate the i-th column below the i-th row
            for j in range(i+1, n):
                P_new[j, :] -= P_new[j, i]/P_new[i, i] * P_new[i, :]
            # Divide the i-th row by the i-th diagonal element
            P_new[i, :] /= P_new[i, i]    
        return P_new[:,n:]
    
    def expected_hitting_time(self, P, s1, s2):
        
        return 0

mc = F_MarkovChain(2)
mat = mc.transitionMatrix("0.2 0.8 .6 .4")
vec = mc.init_dist(".1 .9")
#print(vec)
#print(np.matmul(vec, mat))
print(mc.stationary_dist(mat))