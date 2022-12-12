#break and continue keyword
#break is used to stop the loop when condition is met
#example for break 
for i in range(1,11):
    if i==5:
        break
    print(i,end=' ')   #print 1,2,3,4 and then breaks the loop

#example for continue
for j in range(1,11):
    if j==5:
        continue
    print(j,end=',')    #print all numbers from 1 to 10 except 5

#step arguement in for loop
for num in range(0,11,2):    #prints even numbers upto 11 as it takes 2 steps
    print(num,end=' ')
for k in range(11,1,-1):     #prints from 11 to 1
    print(k)

#using loop in strings only in python as strings are mutable in python
name="suhaib"
for a in name:
    print(a)

num=int(input("Enter the value of row you want"))
for i in range(1,num+1):
    for j in range(i,):
        print(j+1,end=" ")
    print("")

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

for i in range(num,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

for i in range(1,num+1):
    for k in range(num-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("")