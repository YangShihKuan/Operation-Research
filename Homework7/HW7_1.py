from gurobipy import *
print 'root'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <= 6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "c2")
m.setParam('OutputFlag', False )
m.optimize()

print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)
status = m.getAttr('Status')
print status
print 'Status  OPTIMAL'
print 'Keep branching:current upper bound x1  <= 3'
print 'Keep branching:current lower bound x1  >= 4'
print
###################################################################
print 'node1'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <= 6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "c2")
m.addConstr(     x1  <= 3, "c3")
m.setParam('OutputFlag', False )
m.optimize()

print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)
status = m.getAttr('Status')
print status
print 'Status  OPTIMAL'
print 'STOP reason : optimal solutions are integer'
print
###################################################################
print 'node2'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <= 6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "c2")
m.addConstr(     x1  >= 4, "c4")
m.setParam('OutputFlag', False )
m.optimize()

print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)

status = m.getAttr('Status')
print status
print 'Status  OPTIMAL'
print 'Keep branching:current upper bound x2  <= 1'
print 'Keep branching:current lower bound x2  >= 2'
print
###################################################################
print 'node21'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <=  6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "c2")
m.addConstr(     x1  >= 4, "c3")
m.addConstr(     x2  <= 1, "c5")
m.setParam('OutputFlag', False )
m.optimize()

print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)

status = m.getAttr('Status')
print status
print 'Status  OPTIMAL'
print 'Keep branching:current upper bound x1  <= 4'
print 'Keep branching:current lower bound x1  >= 5'
print
###################################################################
print 'node22'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <=  6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "c2")
m.addConstr(     x1  >= 4, "c3")
m.addConstr(     x2  >= 2, "c6")

m.setParam('OutputFlag', False )
m.optimize()
  
status = m.getAttr('Status')
print status
print 'STOP reason:Infeasible'    
print
###################################################################
print 'node211'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <=  6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "21")
m.addConstr(     x1  >= 4, "c3")
m.addConstr(     x2  <= 1, "c5")
m.addConstr(     x1  <= 4, "c7")
m.setParam('OutputFlag', False )
m.optimize()

print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)
status = m.getAttr('Status')
print status
print 'Status  OPTIMAL'
print 'STOP reason : optimal solutions are integer'
print
###################################################################
print 'node212'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <=  6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "21")
m.addConstr(     x1  >= 4, "c3")
m.addConstr(     x2  <= 1, "c5")
m.addConstr(     x1  >= 5, "c8")
m.update()

m.setParam('OutputFlag', False )
m.optimize()

print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)
status = m.getAttr('Status')
print status
print 'Status  OPTIMAL'
print 'STOP reason : optimal solutions are integer'
print  
###################################################################
print 'Final State'
m = Model("Homework 7-1")

x1 = m.addVar(vtype="C", name="x1", obj = 8)
x2 = m.addVar(vtype="C", name="x2", obj = 5)
m.setAttr('ModelSense', GRB.MAXIMIZE)
m.update()

m.addConstr(     x1 +      x2 <=  6, "c1")
m.addConstr( 9 * x1 + 5  * x2 <= 45, "21")
m.addConstr(     x1  >= 4, "c3")
m.addConstr(     x2  <= 1, "c5")
m.addConstr(     x1  >= 5, "c8")
m.update()

m.setParam('OutputFlag', False )
m.optimize()

print('Optimal from MIP solver:')
for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f' % m.objVal)


import BBNode as bn
root = bn.BBNode(None, '', '', 0)
node1 = bn.BBNode(root, 'x1', 'ub', 3)
node2 = bn.BBNode(root, 'x1', 'lb', 4)
node21 = bn.BBNode(node2, 'x2', 'ub', 1)
node22 = bn.BBNode(node2, 'x2', 'lb', 2)
node211 = bn.BBNode(node21, 'x1', 'ub', 4)
node212 = bn.BBNode(node21, 'x1', 'lb', 5)

dvNode = node212

print 'Showing bounds from node212 to root'
while dvNode != root:
    print dvNode.dv, dvNode.boundSense, dvNode.bound
    dvNode = dvNode.parent








