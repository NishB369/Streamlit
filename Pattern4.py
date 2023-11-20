l=eval(input('Enter a list:'))
ul=list(set(l))
fl=[]
d={}
for i in ul:
    d[i]=l.count(i)
a=max(d.values())
for i in d:
    if d[i]==a:
        fl.append(i)
print(max(fl))
