import cvxpy as cp
import numpy as np

x = cp.Variable(shape=(2,1))
A = np.array([[2,1],[1,3],[1,0],[0,1]])
a = np.array([1,1])
b = np.array([[1],[1],[0],[0]])

objective = cp.Minimize(np.matmul(a,x))
constraints = [b <= np.matmul(A,x)]

prob = cp.Problem(objective, constraints)
result = prob.solve()
print(x.value)
print(result)