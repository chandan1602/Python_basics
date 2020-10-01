# cook your dish here
try:
    n = int(input())
    w = list(map(int, input().split()))
    limit = list(map(int, input().split()))
    sol = 0
    w.sort()
    for i in range(0, n, 1):
        j=i+1
        if(w[i]<=limit[1]):
            if(w[i]>=limit[0]):
                sol+=1
            while(w[i]+w[j]<=limit[1]):
                if(w[i]+w[j]>=limit[0]):
                    sol+=1
                j+=1
            j=i+3
            if(i<n-2):
                x = w[i]+w[i+1]
                while(x+w[j]<=limit[1]):
                    if(x+w[j]>=limit[0]):
                        sol+=1
                    x=x+w[j]
                    j+=1
        else:
            break
    print(sol)
except:
    pass
