from gurobipy import *
m = Model("mip1")

x1A = m.addVar(vtype='C', name='x1A')
x2A = m.addVar(vtype='C', name='X2A')
xA1 = m.addVar(vtype='C', name='xA1')
xA2 = m.addVar(vtype='C', name='xA2')
x1B = m.addVar(vtype='C', name='x1B')
x2B = m.addVar(vtype='C', name='x2B')
xB1 = m.addVar(vtype='C', name='xB1')
xB2 = m.addVar(vtype='C', name='xB2')
x1C = m.addVar(vtype='C', name='x1C')
x2C = m.addVar(vtype='C', name='x2C')
xC1 = m.addVar(vtype='C', name='xC1')
xC2 = m.addVar(vtype='C', name='xC2')
x11 = m.addVar(vtype='C', name='x11')
x12 = m.addVar(vtype='C', name='x12')
x21 = m.addVar(vtype='C', name='x21')
x22 = m.addVar(vtype='C', name='x22')
A = m.addVar(vtype='B', name="A")
B = m.addVar(vtype='B', name="B")
C = m.addVar(vtype='B', name="C")
m.update()

m.setObjective(
         (1*x1A + 6*x2A + 4*xA1 + 6*xA2 + 50)*A
        +(2*x1B + 3*x2B + 3*xB1 + 4*xB2 + 60)*B
        +(8*x1C +   x2C + 5*xC1 + 3*xC2 + 68)*C
        + 4*x11 + 8*x12 + 7*x21 + 6*x22,GRB.MINIMIZE)

m.addConstr(x1B + x2B  <= 60, "c1")
m.addConstr(x1C + x2C  <= 70, "c2")
m.addConstr(A + B + C == 1, "c3")
m.addConstr(x1A + x1B + x1C + x11 + x12 == 50, "c4")
m.addConstr(x2A + x2B + x2C + x21 + x22 == 75, "c5")
m.addConstr(xA1 + xB1 + xC1 + x11 + x21 == 75, "c6")
m.addConstr(xA2 + xB2 + xC2 + x12 + x22 == 50, "c7")
m.addConstr(x1A + x2A == xA1 + xA2, "c8")
m.addConstr(x1B + x2B == xB1 + xB2, "c9")
m.addConstr(x1C + x2C == xC1 + xC2, "c10")

m.addConstr(1*x1A + 6*x2A + 4*xA1 + 6*xA2 <= 100000000*A, "c11")
m.addConstr(2*x1B + 3*x2B + 3*xB1 + 4*xB2 <= 100000000*B, "c12")
m.addConstr(8*x1C +   x2C + 5*xC1 + 3*xC2 <= 100000000*C, "c13")
m.optimize()



for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
print('Obj: %f '% m.objVal)
