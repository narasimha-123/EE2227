def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x
def gcd(list):
	num1=list[0] 
	num2=list[1] 
	gcd=find_gcd(num1,num2) 
	  
	for i in range(2,len(list)): 
		gcd=find_gcd(gcd,list[i]) 
		  
	return gcd
import numpy as np
import matplotlib.pyplot as plt
#------------------------Ruth Herwitz------------------------#

A1 = []
A2 = []

inp = [1,2,2,4,11,10] #Input coefficients starting from s^n to s^0 

len_inp = len(inp)
for i in range(0,len_inp,2): #Creating first array of matrix
	A1.append(inp[i])
	if(i+1==len_inp): # Creating Second array of matrix
		break
	A2.append(inp[i+1])
if(len(A1)!=len(A2)):
	A2.append(0)	
A1=np.asarray(A1)
A2=np.asarray(A2)
A1 = A1#/gcd(A1)
A2 = A2#/gcd(A2)
print(A1,A2)	
rows = len(inp)

if(rows%2==0):
	cols = int(rows/2)
else:
	cols = int(rows/2)+1
sum = 0	
dim  = (rows,cols)
mat = np.zeros(dim)
temp = [0]*cols
mat[0] = A1
mat[1] = A2
for k in range(0,cols):
		sum += mat[1][k]
for j in range(0,cols-1): #Making sure second array has no zeros
		if(sum==0):
			mat[1][j] = mat[0][j]*((rows-1)*((2*j)+1))

sum = 0 					

for i in range(2,rows):
	for j in range(0,cols-1):
		temp [j] = ((mat[i-1][0]*mat[i-2][j+1])-(mat[i-2][0]*mat[i-1][j+1]))/(mat[i-1][0])
		temp[cols-1]=0  #Making Sure zeros don't occur in an array
	for k in range(0,cols):
		sum += temp[k]
	
	for j in range(0,cols-1):
		if(sum==0):
			mat[i][j] = mat[i-1][j]*((rows-i)*((2*j)+1))  #if zeros occur
			
		else:  #If no zeros occur 
			if(mat[i-1][0] == 0): mat[i-1][0]=1e-3	 
			mat[i][j] =  ((mat[i-1][0]*mat[i-2][j+1])-(mat[i-2][0]*mat[i-1][j+1]))/(mat[i-1][0])
			mat[i][cols-1] = 0
	
print(mat)   # Output Ruth-Herwitz Matrix

#----------------------------------------------------------
# Veryfing results by printing rootss of function 

col1 = mat[:,0]
count =0
a = col1[0]
for i in range(0,rows):
	col1[i] = col1[i]/abs(col1[i])
	count += col1[i]

roots = (rows-count)

if	(col1[0]+col1[1]==0 and col[1]+col[2]!=0): roots = roots-1
if	(col1[rows-1]+col1[rows-2]==0 and col1[rows-3]+col1[rows-2]!=0): roots = roots-1
print(col1,roots) #No: of roots
print(np.roots(inp))	#Roots
	 

		
