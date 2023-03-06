#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:04:26 2023

@author: juanjose
"""

import numpy as np
import matplotlib as mpl

class MarkovChain:
    """
    Class that represents a Markov Chain.
    """
    
    def __init__(self, n):
        self.n = n

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
                matrix[i].append(int(values[counter]))
                counter += 1
        return np.array(matrix)
    
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
            arr.append(int(values[i]))
        return np.array(arr)

mc = MarkovChain(2)
#print(transitionMatrix(2, "2 4 6 8"))
print(mc.init_dist("1 2"))