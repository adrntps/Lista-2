import cvxpy as cp

x = cp.Variable(2)
objective = cp.Minimize(x[0] + x[1])
constraints = [0 <= 2*x[0] + x[1] -1, 0 <= x[0] + 3*x[1] -1, 0 <= x[0], 0 <= x[1]]
prob = cp.Problem(objective, constraints)
result = prob.solve()
print(x.value)
print(x[0].value+x[1].value)




