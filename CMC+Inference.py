#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 19:09:23 2023

@author: juanjose
"""

import random as rand
import numpy as np
from scipy.linalg import expm

def estimate_infinitesimal_generator(transitions, states):
    num_states = len(states)
    Q = np.zeros((num_states, num_states))

    # Count the number of transitions between states
    transition_counts = np.zeros((num_states, num_states))
    for i in range(len(transitions) - 1):
        current_state = transitions[i]
        next_state = transitions[i + 1]
        transition_counts[current_state, next_state] += 1

    # Estimate the transition rates
    for i in range(num_states):
        row_sum = np.sum(transition_counts[i, :])
        for j in range(num_states):
            if i != j and row_sum > 0:
                Q[i, j] = transition_counts[i, j] / row_sum

    # Adjust the diagonal elements
    for i in range(num_states):
        Q[i, i] = -np.sum(Q[i, :])

    return Q

# Simulation
n = 100
transitions = []
states = [0, 1, 2, 3]
for i in range(n):
    transitions.append(rand.choice(states))

Q_estimated = estimate_infinitesimal_generator(transitions, states)
print("Estimated Infinitesimal Generator Matrix:")
print(Q_estimated)

def infer_transition_matrix(Q, dt):
    P = expm(Q * dt)
    return P

# Example usage
Q = np.array([[-0.5, 0.3, 0.2],
              [0.2, -0.6, 0.4],
              [0.1, 0.2, -0.3]])
dt = 0.1

P_inferred = infer_transition_matrix(Q, dt)
print("Inferred Transition Matrix P:")
print(P_inferred)
