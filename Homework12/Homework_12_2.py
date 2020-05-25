from gurobipy import *

supply = ['P1', 'P2', 'P3'] 
demand = ['M1', 'M2', 'M3', 'M4']

total_supply = {('P1') : 35,
                ('P2') : 50,
                ('P3') : 40}
total_demand = {('M1') : 45,
                ('M2') : 20,
                ('M3') : 30,
                ('M4') : 30}

cost = {
('P1', 'M1'): 8,
('P1', 'M2'): 6,
('P1', 'M3'): 10,
('P1', 'M4'): 9,
('P2', 'M1'): 9,
('P2', 'M2'): 12,
('P2', 'M3'): 13,
('P2', 'M4'): 7,
('P3', 'M1'): 14,
('P3', 'M2'): 9,
('P3', 'M3'): 16,
('P3', 'M4'): 5,
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
    
m.setObjective(quicksum((cost[i,j]*x[i,j]) for i in supply for j in demand), GRB.MINIMIZE)
m.optimize()

# Print solution
if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i,j in arcs:
        if solution[i,j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i,j]))





'''
supply = [35,50,40]
demand = [45,20,30,30]
cost2 = [[8,6,10,9],[9,12,13,7],[14,9,16,5]]



'''


























            
            
            
            
            
            
            
            
            
            
            
            
            