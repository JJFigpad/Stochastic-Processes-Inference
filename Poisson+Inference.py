#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:13:09 2023

@author: juanjose
"""

import random
import numpy as np
from matplotlib import pyplot as plt

class Poisson_Process:
    """
    Class that represents a Poisson Process.
    """
    
    def __init__(self, lam, t_end):
        self.lam = lam
        self.t_end = t_end
        self.lenght = None
        self.actual = None
    
    def sample(self, length):
        """
        

        Parameters
        ----------
        length : float
            Represents the increment time interval (in minutes).

        Returns
        -------
        poisson_process : list
            Sample of a Poisson Process of parameter lam until time t_end
            with increments length.

        """
        self.lenght = length
        poisson_process = []
        l = 0
        while l < self.t_end:
            poisson_process.append(np.random.poisson(self.lam * length))
            l += length
        self.actual = poisson_process
        return self.actual
    
    def E_T(self, t):
        """
        

        Parameters
        ----------
        t : int
            Number of event.

        Returns
        -------
        float
            Expected value of T_t.

        """
        
        return 1/self.lam
    
    def simulation_T(self, n, length, event):
        """
        

        Parameters
        ----------
        n : int
            Number of simulation repetitions.
        length : float
            Represents the increment time interval (in minutes).
        event : int
            Number if event.

        Returns
        -------
        float
            E_[T_{event}] approximation.

        """
        
        actual = None
        r = 0
        for i in range(n):
            actual = self.sample(length)
            k = 0
            k_1 = 0
            t_temp = 0
            for j in range(len(actual)):
                t_temp += actual[j]
                if t_temp >= event-1:
                    k_1 = j
                    break
            t_temp = 0
            for j in range(len(actual)):
                t_temp += actual[j]
                if t_temp >= event:
                    k = j
                    break
            r += (k-k_1)*length
        return r/n
    
    def E_S(self, t):
        """
        

        Parameters
        ----------
        t : int
            Number of event.

        Returns
        -------
        float
            Expected value of S_t.

        """
        
        return t/self.lam
    
    def simulation_S(self, n, length, event):
        """
        

        Parameters
        ----------
        n : int
            Number of simulation repetitions.
        length : float
            Represents the increment time interval (in minutes).
        event : int
            Number if event.

        Returns
        -------
        float
            E_[S_{event}] approximation.

        """
        actual = None
        r = 0
        for i in range(n):
            actual = self.sample(length)
            k = 0
            t_temp = 0
            for j in range(len(actual)):
                t_temp += actual[j]
                if t_temp >= event:
                    k = j
                    break
            r += k*length
        return r/n

pp = Poisson_Process(0.5, 100)
print("Sample = ", pp.sample(1))
E_T = pp.E_T(10)
E_S = pp.E_S(5)
print("E[T] =", E_T)
print("E[S] =", E_S)

n = 500
x = list(range(1, n+1))
y = []
for i in range(1, n+1):
    y.append(pp.simulation_T(i, 1, 5))
plt.scatter(x, y)
plt.plot(x, [E_T]*n, color="red")
plt.title("E[T_i] approximation")
plt.legend(["T_ij", "1/X_n"])
plt.xlabel("Number of attempt")
plt.ylabel("Expected value realization")
plt.show()

y = []
for i in range(1, n+1):
    y.append(pp.simulation_S(i, 1, 5))
plt.scatter(x, y)
plt.plot(x, [E_S]*n, color="red")
plt.title("E[S_i] approximation")
plt.legend(["S_ij", "n/X_n"])
plt.xlabel("Number of attempt")
plt.ylabel("Expected value realization")
plt.show()