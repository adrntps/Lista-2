import cvxpy as cp
import numpy as np

A = np.array([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
B = np.array([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])
X = cp.Variable(shape=(4,4), symmetric = True)

objective = cp.Maximize(cp.trace(cp.matmul(A,X)))
constraints = [X >> 0, cp.trace(X) == 1, cp.trace(cp.matmul(B,X)) == 1]

prob = cp.Problem(objective, constraints)
result = prob.solve()
print(X.value)
print(result)

