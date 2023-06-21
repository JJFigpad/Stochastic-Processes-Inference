#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 17:53:32 2023

@author: juanjose
"""

import numpy as np
import matplotlib.pyplot as plt

class Brownian_Motion_Inference:
    
    def __init__(self, t, n):
        self.t = t
        self.n = n
        self.values = None
    
    def simulation(self):
        r = []
        for j in range(self.n):
            values = [0]  # Starting value is 0
            for i in range(1, self.t+1):
                values.append(values[-1] + np.random.normal(loc=0, scale=np.sqrt(1)))
            r.append(values)
        self.values = r
        return self.values
    
    def B_t_minus_B_s(self, t, s):
        work_values = []
        for attempt in self.values:
            work_values.append(attempt[t] - attempt[s])
        return work_values

# Simulation
n = 1000  # Number of simulations
t = 3  # Time t
s = 2  # Time s
example = Brownian_Motion_Inference(t, n)
example.simulation()
increments = example.B_t_minus_B_s(t, s)
print("var =", np.var(increments))

# Plot histogram of increments
plt.hist(increments, bins=30, density=True, alpha=0.7)
plt.xlabel('Increment Bₜ - Bₛ')
plt.ylabel('Density')
plt.title('Distribution of Increment Bₜ - Bₛ in a Brownian Motion')
plt.axvline(x=0, color='r', linestyle='--', label='Mean')
plt.legend()
plt.show()



