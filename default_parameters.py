def replace(str,char,ind=2):
    x=len(str)
    if ind<=x:
        result=str[0:ind]+char+str[ind+1:]
        print(result)
    else:
        print("index out of range")
str1=str(input())
char1=str(input())
ind1=int(input())
replace(str1,char1)
replace(str1,char1,ind1,)
