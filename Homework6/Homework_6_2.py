from gurobipy import *

supply = ['P1', 'P2'] 
demand = ['M1', 'M2', 'M3']

total_supply = {('P1') : 15,
                ('P2') : 20}
total_demand = {('M1') : 17,
                ('M2') : 8,
                ('M3') : 10}
cost = {
('P1', 'M1'): 3,
('P1', 'M2'): 4,
('P1', 'M3'): 6,
('P2', 'M1'): 5,
('P2', 'M2'): 7,
('P2', 'M3'): 5,
}

arcs, cost = multidict(cost)
# Create optimization model
m = Model('MIN')

x = {}

for i,j in arcs:
    x[i,j] = m.addVar(obj=cost[i,j], vtype = 'C',
         name='x_%s%s' % (i, j))
    
m.update()

# the demand constraints in M1,M2,M3
for j in demand:
    m.addConstr(quicksum(x[i,j]
        for i in supply) == total_demand[j],'dem_%s' % (j))
# the supply constraints in S1,S2
for i in supply:
    m.addConstr(quicksum(x[i,j]
        for j in demand) == total_supply[i],'sup_%s' % (i))

m.optimize()

# Print solution
if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))






