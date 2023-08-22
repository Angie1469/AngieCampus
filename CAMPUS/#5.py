pp= [1, 1, 2, -1, 1, -2]

for i in range(len(pp)):
    print(pp[i])
    if i%2==0:
        sn=pp[i]+1
    else:
        sn=pp[i]-1

    print(sn)