
from gurobipy import *

supply = ['S1', 'S2', 'S3', 'S4'] 
demand = ['J1', 'J2', 'J3', 'J4']


cost = {
('S1', 'J1'): 3,
('S1', 'J2'): 9,
('S1', 'J3'): 3,
('S1', 'J4'): 2,
('S2', 'J1'): 9,
('S2', 'J2'): 4,
('S2', 'J3'): 10,
('S2', 'J4'): 3,
('S3', 'J1'): 8,
('S3', 'J2'): 6,
('S3', 'J3'): 4,
('S3', 'J4'): 5,
('S4', 'J1'): 0,
('S4', 'J2'): 0,
('S4', 'J3'): 0,
('S4', 'J4'): 0,
}

arcs, cost = multidict(cost)
# Create optimization model
m = Model('MAX')

x = {}

for i,j in arcs:
    x[i,j] = m.addVar(ub = 1, vtype = 'C',
         name='x_%s%s' % (i, j))
    
m.update()

# the demand constraints in M1,M2,M3
for j in demand:
    m.addConstr(quicksum(x[i,j]
        for i in supply) == 1,'dem_%s' % (j))
# the supply constraints in S1,S2
for i in supply:
    m.addConstr(quicksum(x[i,j]
        for j in demand) == 1,'sup_%s' % (i))
    
m.setObjective(quicksum((cost[i,j]*x[i,j]) for i in supply for j in demand), GRB.MAXIMIZE)
m.optimize()

# Print solution
if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))



from gurobipy import *

supply = ['S1', 'S2', 'S3', 'S4'] 
demand = ['J1', 'J2', 'J3', 'J4']


cost = {
('S1', 'J1'): 3,
('S1', 'J2'): 9,
('S1', 'J3'): 3,
('S1', 'J4'): 2,
('S2', 'J1'): 9,
('S2', 'J2'): 4,
('S2', 'J3'): 10,
('S2', 'J4'): 3,
('S3', 'J1'): 8,
('S3', 'J2'): 6,
('S3', 'J3'): 4,
('S3', 'J4'): 5,
('S4', 'J1'): 0,
('S4', 'J2'): 0,
('S4', 'J3'): 0,
('S4', 'J4'): 0,
}
print '-----------------------------------------------------------'
arcs, cost = multidict(cost)
# Create optimization model
S = Model('MAX')

x = {}

for i,j in arcs:
    x[i,j] = S.addVar(vtype = 'B', name='x_%s%s' % (i, j))
    
S.update()

# the demand constraints in M1,M2,M3
for j in demand:
    S.addConstr(quicksum(x[i,j]
        for i in supply) == 1,'dem_%s' % (j))
# the supply constraints in S1,S2
for i in supply:
    S.addConstr(quicksum(x[i,j]
        for j in demand) == 1,'sup_%s' % (i))
    
S.setObjective(quicksum((cost[i,j]*x[i,j]) for i in supply for j in demand), GRB.MAXIMIZE)
S.optimize()

# Print solution
if S.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % S.ObjVal
    solution = S.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))