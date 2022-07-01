''' range datatypes'''

# a = 1,2,3,4,5

# for k in a:
#     print(k,end=' ')                                                    # 1 2 3 4 5



# l = {1:'code',
# 2:True,
# 3:365,
# 4:3.652}

# for m in l:
#     print(m)                                                          # 1 2 3 4 (vertical line)


# for j in range(0,56):
#     print(j)                                                          # 0 1 2 3 ........... 55



# for h in range(0,50,5):
#     print(h)                                                            # 0 5 10 .....45


# for i in range (0,20,2):
#     print(i)                                                                # 0 2 4 6...... 18


    
# for i in range (1,20,2):
#     print(i,end=' ')                                                         # 1 3 5 7 9 ......19



# d = {'apple',15,3.65,True,None}

# for g in d:
#     print(g,end=' ')                                                          # 15 'apple'  None 3.65 True 


# a = range(55)
# print(a)                                                                        # 0 55       




# r = (1, 'bob', 3.65, True, 5236)
# print(r)                                                                         # [1, 'bob', 3.65, True, 5236]

''' If you want to remove the square brackets and coma then place *'''

# r = [1,'bob',3.65, True,5236]
# print(*r)                                                                        # 1 bob 3.65 True 5236



# l = {1:'code',
# 2:True,
# 3:365,
# 4:3.652}

# print(l)                                                                         # {1: 'code', 2: True, 3: 365, 4: 3.652}                      
# for i in l:
#     print(i)                                                                     # 1 2 3 4 
# print(*l,sep='-')                                                                # 1-2-3-4


print(11,'bob',True,23.65,sep='--')                                             # 11--bob--True--23.65


for i in range(10,0,1):
    print(i)                                                                    # Nothing printed

for j in range(7,6):
    print(j)                                                                    # Nothing printed


for m in range(0,10,-1):
    print(m)                                                                     # Nothing printed


for u in range(10,1,-3):
    print(u)                                                                       # 10 7 4


