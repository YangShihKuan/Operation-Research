**作業研究-授課教授陳柏華**  
Learn to systematically analyze the problem of concern, formulate the problem into mathematical models, and find the optimal solution using available techniques and software packages. 


## Homework2

1. Write up a short report about Python (HW2-1)
2. the graphical method (HW2-2)
3. the derivation of the Shadow Price (HW2-3) and discuss what you have learned.


## Homework3

### Homework 3-1
Script Files for:
1. printing of integers from 1 to 50 divisible by 11 using a for loop.
2. printing of integers from 1 to 30 divisible by 5 or 7 using a for loop.
3. printing of integers from 1 to 30 divisible by 2 and 7 using a for loop.
4. printing of integers from 1 to 20 not divisible by 2 nor 7 using a while loop.
5. printing of odd integers from 1 to 20 using a while loop.

### Homework 3-2
Please write a Python script called factori.py such that the Factorial is calculated based on a loop structure, where N is given by the user.

### Homework 3-3
For the following problem, please solve it by using the simplex method by hand. Please also indicate geometric properties you have observed when working on this problem.  
max z = 2*x1 + x2  
s.t.  
x1 + x2 ≤ 10  
−x1 + x2 ≥ 2  
x1, x2 ≥ 0  

## Homework4

### Homework 4-1
Please write a Python script called Fibo2.py which includes a function called fibo2(n) such that the Fibonacci sequence is returned to the nth number, where n is the input.

### Homework 4-2
1. Please solve the problem on page 110 by hand and check the answer by using the pivot function.  
2. Is it appropriate to use the (Primal) Simplex Method? Can you use the 2-Phase Method? Would the Dual Simplex Method work? What if you convert the problem into its dual problem?  
3. Please organize your Python calculation steps into one Script File called hw42.py, so that you can just execute the Script File and see the results.  

### Homework4 - Bouns
Given a problem (A and BV in the right format), implement the simplex method to automatically pivot the problem to the optimal state.
Please also write a short report on your thoughts, challenges and findings

## Homework5
### Homework5-1:
Use gurobi to solve LP below:  
max z = 5x1 + 4x2  
s. t.  
6x1 + 4x2 <= 24  
x1 + 2x2 <= 6  
-x1 + x2 <= 1  
x2 <= 2  
x1, x2 >= 0  

Solution:  
x1 = 3  
x2 = 1.5  
z = 21  

### Homework5-2:
Please try to formulate the problem into a (Mixed) Integer Programming problem, and write the model in a document and save as pdf. Once the problem is formed, please use Gurobi to solve the problem.

## Homework6
### Homework6-1 (40%)  
Please solve for a TSP.
### Homework6-2 (60%)
Please form this problem and solve it with Python using Gurobi, and describe your model in pdf and also provide the .py file


## Homework7
For the problem at page 61, solve the problem using branch-and-bound.  
Through the process, you can use Python and Gurobi to help you solve the Linear Programming sub-problems (not directly solving the Integer Program).  
Please organize all your calculation (code) in a .py file, and output the answers for each sub-problem  

## Homework8
### Homework8-1 (30%)
*10 % for each constraint
### Homework8-2 (30%)
*10 % for each constraint
### Homework8-3(Report) (40%)
*Which one do you think is better?(20%)
*The findings(20%)

## Homework9
### Homework9-1 30%
Please print out the solution, zd ,z* and the gap of each iteration.
### Homework9-2 25%
Fill in necessary material in ORkmedoidsLR.py
### Homework9-3 25%
Fill in necessary material in ORkmedoidsLR.py

Report 20%
Talking about your finding.

## Homework10
Please implement the Dynamic Programming of the Knapsack Problem in Python. The solution algorithm is to be implemented through a Python function you will define called knapsackDP, in a file you will create called knapsackDP.py, and use testKnapsackDP.py for testing.

## Homework11
In this homework, you are to implement the column generation with the following example.
Pieces of steel in three lengths:  
·97 pieces of length 45 cm.,  
·610 pieces of length 36 cm.,  
·395 pieces of length 31 cm., and  
·211 pieces of length 14 cm.  
We have steel rods of length 100 cm. of unit price.  
Please submit the compressed .zip file which includes your .py, and .pdf report on you findings of column generation.  


## Homework12

### Homework12-1
Form the model and use Gurobi to solve for the answer.  
Answer:  
x12 = x23 = x31 = 1.  
What if we do not use binary decision variables, but continuous variables with upper bounds?
### Homework12-2
Solve the Transportation Problem using Gurobi and confirm that the solution from the Transportation Algorithm introduced in this lecture is correct. Does it make a difference whether the decision variables
are integer or continuos?





























