# ITEM            WEIGHT     PROFIT
# SLEEPING BAG    15         15
# ROPE            3          7
# POCKET KNIFE    2          10
# TORCH           5          5
# BOTTLE          9          8
# GLUCOSE         20         17

import random

wt = [15,3,2,5,9,20]
pt = [15,7,10,5,8,17]
par = ["100110","001110","010100","011001"]
score = [0,0,0,0]
weight= [0,0,0,0]
print("Parents:")
print(par)

def fitScore(chrom):
    x = 0
    y = 0
    for i in range(0,6):
        if chrom[i] is "1":
            x+= wt[i]
            y+= pt[i]
    return x, y
"""
while 1:
    x = input(">>")
    print("weight,point")
    print(fitScore(str(x)))
"""



def minAndBetter(scr):
    d = score[0]
    temp = 0
    flag = 0
    for i in range(0,4):
        print(score[i])
        if score[i]<d and score[i]<scr:
            d = score[i]
            temp = i
            flag = 1
    if flag==1:
        print("replaced a",temp,d)
        return temp
    else:
        t = random.randint(0,3)
        print("replaced b", t)
        return t


i=1
while (i<4):
    print("Generation#",i)
    # fitness score all
    for j in range(0,4):
        weight[j],score[j] = fitScore(par[j])
        print(par[j],weight[j],score[j])

    # Selection
    t1 = random.randint(0,3) # these are candidates
    t2 = random.randint(0,3)
    while(t1==t2):
        t1 = random.randint(1, 3)

    p1 = par[t1]
    p2= par[t2]
    print("Candidate parents",p1,p2)

    #Crossover
    c1 = p1[0:3]+p2[3:]
    print("After Crossover:",c1)
    #Mutation
    child = [0,0,0,0,0,0]
    t2 = random.randint(0, 5)
    for j in range(0,6):
        child[j] = c1[j]

    if child[t2] == '1':
        child[t2] = '0'
    else:
        child[t2] = '1'

    c1 = ''.join(child)
    print("After Mutation:", c1)
    #Validation
    chWt1, chPt1 = fitScore(c1)
    if chWt1 <= 30:
        x = minAndBetter(chPt1)
        par[x] = c1

    print(">>>>>",c1,"Weight",chWt1,"Point",chPt1)

    i+=1

"""
Parents:
['100110', '001110', '010100', '011001']
Generation# 1
100110 29 28
001110 16 23
010100 8 12
011001 25 34
Candidate parents 010100 100110
After Crossover: 010110
After Mutation: 011110
28
23
12
34
replaced  010100
>>>>> 011110 Weight 19 Profit 30
after replacing: 
['100110', '001110', '011110', '011001']
Generation# 2
100110 29 28
001110 16 23
011110 19 30
011001 25 34
Candidate parents 011110 100110
After Crossover: 011110
After Mutation: 111110
not updated because weight is  34
Generation# 3
100110 29 28
001110 16 23
011110 19 30
011001 25 34
Candidate parents 001110 011110
After Crossover: 001110
After Mutation: 011110
28
23
30
34
replaced  001110
>>>>> 011110 Weight 19 Profit 30
after replacing: 
['100110', '011110', '011110', '011001']
optimal sol:  ['100110', '011110', '011110', '011001']

"""
