from typing import Union, Iterable

import numpy as np


payoff_a = np.mat([[0,4,5],[4,0,5],[3,3,6]])
payoff_b = np.mat([[4,0,3],[0,4,3],[5,5,6]])

print(payoff_a)
print(payoff_b)

i_row_a = np.shape(payoff_a)[0]
j_col_a = np.shape(payoff_a)[1]
i_row_b = np.shape(payoff_b)[0]
j_col_b = np.shape(payoff_b)[1]

for j in range(j_col_a):                # search by column
    for i in range(i_row_a):
        if payoff_a[i,j] == payoff_a[:,j].max():
            print('在第%s列，a的占优策略位于第%s行' %((j+1) , (i+1) ))


for i in range(i_row_b):                # search by row
    for j in range(j_col_b):
        if payoff_b[i,j] == payoff_b[i,:].max():
            print('在第%s行，b的占优策略位于第%s列' %((i+1) , (j+1) ))












# for i in range(np.shape(payoff_a)[0]):