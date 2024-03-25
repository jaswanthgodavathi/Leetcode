n=int(input())
l=[]
for i in range(n):
    a=input().lower()
    a=a.split()
    stri=''
    for i in a:
        for j in i:
            if j.isalpha():
                stri+=j
        if len(stri)!=0:
            l+=[stri]
        stri=''

b=set(l)
b=sorted(list(b))
l=list(b)
print(len(b),end='\n')
for i in l:
    print(i)