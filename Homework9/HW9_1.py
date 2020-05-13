# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:46:46 2017

@author: Kuan
Purpose: HW9_2
"""
from gurobipy import *


u1 = 0
u2 = 0
gap = 100
Z = 0 # lower bound
lambada = 1
Time = 1

while gap!=0:
    print ("---'Time'= %d---" %Time)
    print 'u1 :',u1
    print 'u2 :',u2
    var=[]
    m = Model("LR")

    x1 = m.addVar(vtype="I", name="x1")
    x2 = m.addVar(vtype="I", name="x2")
    x3 = m.addVar(vtype="I", name="x3")
    x4 = m.addVar(vtype="I", name="x4")

    m.update()
    
    m.setObjective(16*x1 + 10*x2 + 0*x3 + 4*x4 + u1*(1-x1-x2)+u2*(1-x3-x4), GRB.MAXIMIZE)
    
    m.addConstr(8*x1 + 2*x2 + x3 + 4*x4 <= 10)
    m.addConstr( 0 <= x1 <= 1)
    m.addConstr( 0 <= x2 <= 1)
    m.addConstr( 0 <= x3 <= 1)
    m.addConstr( 0 <= x4 <= 1)
    m.setParam('OutputFlag', False )
    m.optimize()
    print
    for v in m.getVars():
        print('%s : %f' % (v.varName, v.x))
        var.append(v.x)
    print
    print('Zd : %f' % m.objVal)

    r = Model("relax")
    x1 = r.addVar(vtype="I", name="x1")
    x2 = r.addVar(vtype="I", name="x2")
    x3 = r.addVar(vtype="I", name="x3")
    x4 = r.addVar(vtype="I", name="x4")
    r.update()   
    r.setObjective(16*x1 + 10*x2 + 0*x3 + 4*x4, GRB.MAXIMIZE)
    r.addConstr(8*x1 + 2*x2 + x3 + 4*x4 <= 10)
    r.addConstr(x1 + x2 <= 1)
    r.addConstr(x3 + x4 <= 1)
    r.addConstr( x1 == var[0])
    r.addConstr( x2 == var[1])
    r.addConstr( x3 == var[2])
    r.addConstr( x4 == var[3])
    r.setParam('OutputFlag', False )
    r.optimize()


    
    if r.getAttr('Status') > 2:
        tk = lambada*(m.objVal - Z)/((1-var[0]-var[1])**2+(1-var[2]-var[3])**2)
        u1 = max(0,u1-tk*(1-var[0]-var[1]))
        u2 = max(0,u2-tk*(1-var[2]-var[3]))
        if Z!=0:
            gap = (m.objVal - Z)/Z
        
    else:
        if r.objVal > Z:
            Z = r.objVal
        
        tk = lambada*(m.objVal - Z)/((1-var[0]-var[1])**2+(1-var[2]-var[3])**2)
        u1 = max(0,u1-tk*(1-var[0]-var[1]))
        u2 = max(0,u2-tk*(1-var[2]-var[3]))
        gap = (m.objVal - Z)/Z
    print "Z* :",Z
    print
    print 'gap :',gap,'%'
    Time = Time + 1