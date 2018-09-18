from typing import Union, Iterable
import numpy as np

# payoff_a = np.mat([[2,1,1],[0,0,0],[0,0,0]])
# payoff_b = np.mat([[12,10,12],[12,10,11],[12,10,13]])

payoff_a = np.mat([[1,1,0],[0,0,2]])
payoff_b = np.mat([[0,2,1],[3,1,0]])

print(payoff_a)
print(payoff_b)

i_row_a = np.shape(payoff_a)[0]
j_col_a = np.shape(payoff_a)[1]
i_row_b = np.shape(payoff_b)[0]
j_col_b = np.shape(payoff_b)[1]

count_mat = np.mat(np.zeros((i_row_a,j_col_a)), dtype=int)      # to count focal points
# print(count_mat)

for j in range(j_col_a):                # search by column
    for i in range(i_row_a):
        if payoff_a[i,j] == payoff_a[:,j].max():
            count_mat[i,j] += 1
            print('在第%s列，a的占优策略位于第%s行' %((j+1) , (i+1) ))
            print(count_mat)

for i in range(i_row_b):                # search by row
    for j in range(j_col_b):
        if payoff_b[i,j] == payoff_b[i,:].max():
            count_mat[i,j] += 1
            print('在第%s行，b的占优策略位于第%s列' %((i+1) , (j+1) ))
            print(count_mat)

# print(np.argmax(count_mat))
strict_position_tuple = np.where(count_mat == 2)

if count_mat.max() == 2 & len(strict_position_tuple[0]) == 2:
    print('有混合策略nash equil.')
    print('There are %s Schelling(focal) point(s) exists' %(len(strict_position_tuple[0])))  # tuple value in rows[], cols[]
    for i in range(len(strict_position_tuple[0])):
        print('Schelling point %s in : %s ' %(i+1, strict_position_tuple[i]+1))

else:
    print('有纯策略nash equil.')
    print('There are %s Schelling(focal) point(s) exists' % (len(strict_position_tuple[0])))


# print('Nash Equil. on Row:%s Col:%s' %(strict_position_tuple[0][0]+1,strict_position_tuple[1][1]+1))










# for i in range(np.shape(payoff_a)[0]):