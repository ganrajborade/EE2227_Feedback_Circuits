import numpy as np
import math

#if using termux
import subprocess
import shlex
#end if

cur_x = 310000 # The algorithm starts at x=310000
gamma = 25 # step size multiplier
precision = 0.00001
previous_step_size = 1
max_iters = 20000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda x: -math.atan(x/1e5)-math.atan(x/(3.16*1e5))-math.atan(x/1e6) + (135*np.pi/180)

while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x += gamma * df(prev_x) #knowing that the value is greater than that of the 310000.
    previous_step_size = abs(cur_x - prev_x)
    iters+=1

print("The value of fc is", cur_x,"Hz")


df1 = lambda fc : (10**5)/((1+(fc/(10**5))**2)**0.5)
df2 = lambda fc : 1/((1+(fc/((3.16*(10**6)))**2))**0.5) 
df3 = lambda fc : 1/((1+(fc/(10**6))**2)**0.5)

G = df1(cur_x)*df2(cur_x)*df3(cur_x)
H = 1/G
print("The value of H is ",H)
print("The corresponding value of G where the graph stabilise is",G)
Af = (10**5)/(1+(H*(10**5)))
print("The closed loop gain is ",Af)