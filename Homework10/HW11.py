from gurobipy import *
import knapsackDP as knapsackDP
'''
rod_length = 100 
lenght = [45, 36, 31, 14]
piece = [97,610,395,211]
'''


c = -1
a = [] 
x = 0 

rod_length = 100

lenght = [45, 36, 31, 14]
piece = [97,610,395,211]
number = len(piece)
while c < 0 :
    if x == 0:
        print '--------------Initial RMP--------------'
    else:
        print '--------------  %xnd  RMP--------------'%(x+1)
            
    m = Model("CuttingStock")
    m.setParam( 'OutputFlag', False )
 
    for i in range(0,number):
        locals()['x%s' % (i+1)] = m.addVar(lb = 0.0, name='x'+str(i+1), obj=1.0)
    m.update()

    for i in range(0,number):
        locals()['c%s' % (i+1)] = m.addConstr(locals()['x%s' % (i+1)] >= piece[i])
    
    constraint = []
    for i in range(0,number):
        constraint.append( locals()['c%s' %(i+1)])
    
    if x > 0: 
        for i in range(0,x):
            col = Column(a[i],constraint) 
            m.addVar(obj=1.0, name='x'+str(i+number+1), column = col)
            m.update()
    
    m.optimize()
    
    shadowprices=[]
    
    for i in range(0,number):
        shadowprices.append(locals()['c%s' % (i+1)].pi)
    round_shadowprices = []
    for i in shadowprices:
        z = round(i,2)
        round_shadowprices.append(z)
    print
    print "pi =",round_shadowprices
    #--------------------
    reload(knapsackDP)
    
    final = knapsackDP.knapsackDP(rod_length,lenght, shadowprices)
    print
    print 'SP Opt:',final.f
    print 'a:',final.result
    a.append(final.result)
    c = 1- final.f
    print 'c:',c
    x = x + 1
    print
    for v in m.getVars():
        print('%s: %f' % (v.varName, v.x))
    
    print
    print 'Obj:',m.objVal
    
    

    
    