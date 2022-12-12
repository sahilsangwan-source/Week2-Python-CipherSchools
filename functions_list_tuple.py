def tutorial():
    num1=int(input("enter your first number "))
    num2=int(input("enter your second number "))
    x=int(input("num1"+"+"+ "num2 " ))
    y=num1+num2
    if x ==y:
        print("true")
    else :
        print("false")


def prime() :
    x=int(input("enter the value of x"))
    if x<2 :
        print("the number is not prime")
    else :
        for i in range(2,x):
            if x%i==0 :
                print("the number is not prime")
                break
        else :
            print("the number is prime")

def even() :
    x=int(input("enter the value of x"))
    if x%2==0 :
       print("even")
    else :
       print("odd")

prime()

#x="sahil \n is a good boy "
#print(x.replace("sahil","akhil"))

y=[1,2,3,4,5,6,7,8,9]
for a in y:
    if a==7 :
        continue
    elif a==9 :
        continue
    print(a)

x=["sahil","yash","priya","khushi","akhil",]
y=[]
for a in x :
    if "k" in a :
        y.append(a)
print(y)

x=["sahil","yash","priya","khushi","ruchika",]
def loop(x):
    print(x*3)
def function(crazy,x):
    for items in x :
        crazy(items)
function(loop,x)

a=2
while a<=256:
    print(a)
    a*=2

list=["car","bike","scooter","bus","train"]
list.insert(0,"sahil")
list.append("khushi")
list.remove("bus")
print(list)

list =["sahil","naina","khushi","priya","vikey","mohit"]
x=[]
for a in list:
    if "a" in a :
        x.append(a)
print(x)

X=("sahil","khushi","isha","naina","shiv","kajal")
z=list(X)
z.insert(4,"akhil")
y=tuple(z)
print(y)

list=["sahil","yunesh","khushi"]
x=[]
for a in list :
    if "i" in a :
        x.append(a)
print(x)


x=lambda b : b**2
print(x(4))
y=lambda c,d : c*d
print(y(45,2))


def f1(n):
    return lambda a :a+n
doub=f1(40)#in it we define the value of arguement of f1 function
print(doub(30))#in it we define value of a for lambda


def prime(x):
    for a in range(2,x):
        if x%a==0:
            return False
        else :
            return True

x=filter(prime,range(50))
print(list(x))

def square(x):
    return x*x
numb=[1,2,3,4,5,6,7]
numb=map(square,numb)
print(list(numb))




i=10
while i<=300:
    print(i,end="")
    i+=10

#tuple dat structure 
#tuple can store any data
#tuples are immutable
#tuple methods
# count,index,len<slicing
a=(1,2,3,4,5)  
fruits='orange','mango','apple'  #tuple without  paranthesis


#list insiede tuple
v=(1,2,3,4,[2,6,8,9,0])
v[1].pop()            # we can change data of list inside tuple
v[1].append(0)   


#min and max as used in list
print(min(a))
print(max(a))
#sum
print(sum(a))

        