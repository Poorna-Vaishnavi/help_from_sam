def sum(a):
    count=1
    res=1
    while res<a:
        res*=2
    if res>a:
       b=res//2
       c=a-b
       return count+c
    if res==a:
        return count   

a=int(input())
print(sum(a))   
