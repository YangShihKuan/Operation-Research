from gurobipy import *

nodes = ['1', '2', '3', '4', '5', '6']
cost = {
('1', '2'): 2429,
('1', '3'): 1967,
('1', '4'): 1497,
('1', '5'): 1650,
('1', '6'): 2392,
('2', '1'): 2429,
('2', '3'): 1105,
('2', '4'): 1674,
('2', '5'): 1320,
('2', '6'): 5566,
('3','1'): 1967,
('3','2'): 1105,
('3','4'): 2023,
('3','5'): 9527,
('3','6'): 560,
('4','1'): 1497,
('4','2'): 1674,
('4','3'): 2023,
('4','5'): 1999,
('4','6'): 1273,
('5','1'): 1650,
('5','2'): 1320,
('5','3'): 9527,
('5','4'): 1999,
('5','6'): 778,
('6','1'): 2392,
('6','2'): 5566,
('6','3'): 560,
('6','4'): 1273,
('6','5'): 778,
}


arcs, cost = multidict(cost)
# Create optimization model
m = Model('TSP')
# Create variables
x = {}
u = {}

for i,j in arcs:
    x[i,j] = m.addVar(obj=cost[i,j], vtype = 'B',
         name='x_%s%s' % (i, j))
    
N = len(nodes)
for i in nodes:
    if i != nodes[N-1]:
        u[i] = m.addVar(obj=0, name='u_%s' % i)
m.update()

# Constraint for sum of incoming links to j
for j in nodes:
    m.addConstr(quicksum(x[i,j]
        for i in nodes if i != j) == 1,'incom_%s' % (j))

# Constraint for sum of outgoing links from i
for i in nodes:
    m.addConstr(quicksum(x[i,j]
        for j in nodes if i != j) == 1,'outgo_%s' % (i))

# Subtour elimination constraints
for i,j in arcs:
    if i != nodes[N-1] and j != nodes[N-1]:
        m.addConstr(u[i] - u[j] + N*x[i,j] <= N-1,'subtour_%s_%s' % (i, j))

# Compute optimal solution
m.optimize()

# Print solution
if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))















