# Enter your code here. Read input from STDIN. Print output to STDOUT
str=""
history=[]
q=int(input())

for _ in range(q):
    query=input().split()
    op_type=int(query[0])
    
    if op_type==1:
        history.append(str)
        str += query[1]
    elif op_type==2:
        history.append(str)
        k=int(query[1])
        str=str[:-k]
    elif op_type==3:
        k=int(query[1])
        print(str[k-1])
    elif op_type==4:
        if history:
            str=history.pop()