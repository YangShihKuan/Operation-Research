import math 
import numpy

class KnapsackDPResult(object): # save this in the KnapsackDP.py file
    def __init__(self, f, result):
        # instance variables
        self.f = f # optimal objective value
        self.result = result # optimal combination of goods in knapsack


def knapsackDP(C,W,V):
    # C is the capacity, which is a constant
    # W is the weight vector
    # V is the value vector

    # fill in the logic for Dynamic Programming here:
    # ...    
    stage_list =range(0,len(W)) #[0, 1, 2]
    stage_order = list(reversed(stage_list)) #[2, 1, 0]
    opt_value = [[]]*len(W) #[[], [], []]
    opt_m = [[]]*len(W)


    for stage in stage_order:
    
        temp_value = []
        temp_m = []  
        for x in range(int(C+1)):
            ####
            solution = []
            for m in range(int(C/W[stage])+1):
                #print 'sol',solution
                if stage == stage_order[0]:
                    if x-W[stage]*m < 0:
                        solution.append(0)
                    else:
                        solution.append(round(V[stage]*m,2))
                elif x-W[stage]*m < 0:
                    solution.append(0)
                    
                else:
                    solution.append(round(V[stage]*m + opt_value[stage+1][x-W[stage]*m],2))
        
            max_opt = max(solution)
            max_m = solution.index(max_opt)
    
            temp_value.append(max_opt)
            temp_m.append(max_m)
                      
            opt_value[stage] = temp_value
            opt_m[stage] = temp_m
   
    result = []
    remaining_value = 0
    for h in stage_list:
        if h == 0:
            optf = max(opt_value[h])
            current_x = opt_value[h].index(optf)
        
            remaining_value = max(opt_value[h]) - V[h]*opt_m[h][current_x]
            result.append(opt_m[h][current_x])
        else:
            current_m = opt_value[h].index(remaining_value)
            result.append(opt_m[h][current_m])
            remaining_value = round(remaining_value - V[h]*opt_m[h][current_m],2)
            
    opt_value = numpy.array(opt_value)
    opt_m = numpy.array(opt_m)
    #print
    #print '''Optimal Value:\n''',opt_value
    #print
    #print '''Optimal M:\n''',opt_m
    return KnapsackDPResult(optf, result)    
             