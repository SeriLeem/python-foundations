#ex1 generating various lists
# aa=[]
# bb=[10,20,30,40,50]
# cc=["python", "java", "C language"]
# dd=["hong", "170, 60.4"]

# print(aa)
# print(bb)
# print(cc)
# print(dd)

#ex2 add values to the list
# aa=[]
# bb=[]
# value=0

# for i in range(0,100):
#     aa.append(value)
#     value+=2
# for n in aa:
#     print(n, end='')
# print()

# for i in range(0,100):
#     bb.append(aa[99-i])
# for n in bb:
#     print(n, end='')

#ex3 printing list in various ways
# L=[]
# L1=[1, 2, "Great"]
# print(L1)
# print(L1[0], L1[-1])
# print(L1[1:3], L1[:])
# print(L1*2)
# L2=list(range(10))
# print(L2)
# print(L2[::2])
# print(L1+L2)

# print('length =', len(L1))
# print(4 in L2)

#ex4 creating list with iteration
# A=[x for x in range(10)]
# print("A=", A)
# B=[x for x in 'abcd']
# print("B=", B)
# print("A=", A)
# print(B[1])

#ex5 creating list with list()
# A=list()
# print(A)
# B=list('abc')
# print(B)
# C=list(range(5))
# print(C)

#ex6 printing data in list using for loop
# t_list=["apple", "banana", "orange", "melon"]
# for i in t_list:
#     print(i)
    
    
#ex7 changing data in list using index + 3 ways of using format
# l=[2,1,3,5,4]
# for i in range(len(l)):
#     l[i]*=10
# print("l=%s"%l)
# print("l={}".format(l))
# print("%5d %5.2f %10s"%(10, 3.14, "python"))
# print("{0:>5} {1:>5.2f} {2:>10}".format(10, 3.14, "python"))
# print(f"{10:>5} {3.14:>5.2f} {'python':>10}")

#ex8 compare two lists
# A=[1,2,3]
# B=[1,2,3]
# print(A==B) #are they same in value?
# print(A is B)  #are they same in memory address?
# print(id(A), id(B))  #print their memory address
# B=A
# print(A is B)
# print(id(A), id(B))

#ex9 concatenate two lists, iterate through a list
# print(10 in [10, 20, 30])
# print (10 not in [10, 20, 30])
# print([1,2,3]+[4,5,6])
# print([0,1,2]*3)
# print(3*[0,1,2])

#ex10 printing the length, min, max, index, count from a list
# A=[10, 20, 30, 40, 40, 40, 50,]
# print(len(A), min(A), max(A))
# print(A.index(30))
# print(A.count(40))
# print()
# A[0]=100
# print(A)
# A=[0,1,2,3,4,5]
# A[1:4]=[10,20,30]
# print(A)
# A=[0,1,2,3,4,5]
# A[1:4]=[]
# print(A)
# A=[1,2,3,4,5]
# A.append(6)
# print(A)
# A.append([100,200,300])
# print(A)
# A.clear()
# print(A)
 

#ex11 shallow and deep copies of a list
# A=[10,20,30]
# B=A #shallow copy
# print(id(A), id(B))

# A[0]=100
# print(A)
# print(B)
# A=[0,[1,2]]

# B=A.copy() #deep copy
# print(id(A), id(B))
# A[0]=100
# print(A)
# print(B)
# print() 

#ex12 various methods of a list
# A=[1,2,3]
# A.extend([4,5,6])
# print(A)
# A.insert(1, 100)
# print(A)
# A.pop()
# print(A)
# A.pop(1)
# print(A)
# A.remove(2)
# print(A)
# A.reverse()
# print(A)


#ex13 tuples or lists within a list
# lt=[('one', 1), ('two', 2), ('three', 3)]
# for t in lt:
#     print('name={:7} num={}'.format(t[0], t[1]))
# print()
# for name, num in lt:
#     print('name={:7} num={}'.format(name, num))
# print()
# for name, num in lt:
#     print(name, num)


#ex14 alignment of data with list sort() method
# A=[2,3,5,1,0]
# A.sort()
# print(A)
# A.sort(reverse=True) #reverse order
# print(A)

# colors=['blue', 'green', 'orange', 'red', 'yellow', 'purple']
# colors.sort()
# print(colors)
# colors.sort(reverse=True)   
# print(colors)

# L='Python is a Programming Language'.split()
# L.sort()
# print(L)
# L.sort(key=str.lower) #sort without case sensitivity
# print(L)

# L=['123', '34', '56', '2345']
# L.sort()
# print(L)

# L=['123', '34', '56', '2345']
# L.sort(key=int)
# print(L) 

#ex15 computing the lists
# ct_list=['apple', 'banana', 'grape', 'orange']
# print(ct_list)

# ct_list[2]='kiwi'
# print(ct_list[0], end=' ')
# print(ct_list[1], end=' ')
# print(ct_list[2], end=' ')
# print(ct_list[3])

# print(ct_list[2:4])

# t_list=[ct_list, ct_list]
# print(t_list)

# list1=[1,2,3,4]
# list2=['apple', 'banana', 'grape', 'kiwi']
# list3=list1 + list2
# print(list3)
# print(list1*2)

#ex16 indexing
# L=[0,1,1,2,3,5,8,13,21]
# print('next value of {0[4]} is {0[5]}'.format(L))
# print('age:{age} height:{height}'.format(age=23, height=175))

# info={'size':32, 'height':173, 'age':43}
# print('age:{age} height:{height}'.format_map(info))

#ex17 alignment of list with sorted() method
# A=[2,3,5,1,0]
# B=(sorted(A))
# print(B)
# print(sorted(A, reverse=True))

# colors=['blue', 'green', 'orange', 'red', 'yellow', 'purple']
# print(sorted(colors))
# print(sorted(colors, key=str.lower))
# print(sorted(colors, key=str.lower, reverse=True))
# print(sorted(colors, key=lambda s:s[-1]))

#ex18 reverse list alignment using reversed() method
# L=['123', '34', '56', '2345']
# for ele in reversed(L):
#     print(ele)

#ex19 storing names of 5 friends in a list and printing them
# friend_list=[]
# friend=input("name of friend?:")
# friend_list.append(friend)
# friend=input("name of friend?:")
# friend_list.append(friend)
# friend=input("name of friend?:")
# friend_list.append(friend)
# friend=input("name of friend?:")
# friend_list.append(friend)
# friend=input("name of friend?:")
# friend_list.append(friend)

# print(friend_list)

#ex20 making a hamburger!
# print("let's make a hamburger!")
# basemat=('bread', 'tomato', 'veggies', 'sauce')
# coremat=('prawn', 'bulgogi', 'beef', 'cheese')

# print('{food} has a base material of {base}, and depending on the core material, its name changes'.format(food='hamburger', base=basemat))
# print()
# for item in coremat:
#     print('with core material of {core}, it is called a {core} burger'.format(core=item))
    

#ex21 store various idioms in a list and randomly print them
# import random
# quotes=[]
# quotes.append("A bird in the hand is worth two in the bush")
# quotes.append("A penny saved is a penny earned")
# quotes.append("A picture is worth a thousand words")
# quotes.append("A watched pot never boils")
# quotes.append("Actions speak louder than words")
# dailyQuote=random.choice(quotes)
# print("#####################################")
# print("#         idiom of the day!         #")
# print("#####################################")
# print("")
# print(dailyQuote)

#ex22 2D list - make a list of 3x4 and print it
# list1=[]
# list2=[]
# value=1
# for i in range(0,3):
#     for k in range(0,4):
#         list1.append(value)
#         value+=1
#     list2.append(list1)
#     list1=[]
    
# for i in range(0,3):
#     for k in range(0,4):
#         print("%3d"%list2[i][k], end='')
#     print("")

#ex23 various ways of forming a list
# A=[num for num in range(1,6)] #comprehension
# print("A=",A)

# B=[num*num for num in range(1,6)]
# print("B=", B)

# C=[num for num in range(1,21) if num%3==0]
# print("C=",C)

# D=[(x, x*2) for x in range(5)]
# print("D=", D)

# E=F=[[i*3+j for j in range(2)] for i in range(3)]
# # i=0,1,2
# # j=0,1
# # 0,0 3,4 6,7
# print(E)
# print(E[0][0])
# print(E[1][0])
# print(E[2][0])
# print(E[2][1])

# print("F=", F)

#ex24 make a list of 5x5
# m=[[0]*5 for i in range(5)]
# n=0
# for i in range(0,5):
#     for j in range(0,5):
#         m[i][j]=n
#         n+=1
        
# for i in range(0,5):
#     for j in range(0,5):
#         print(m[i][j], end="")
#     print()


#ex25 access to multiple lists simultaneously
# foods=["aa", "bb", "cc", "dd", "ee", "ff"]
# sides=["AA", "BB", "CC"]
# for food, side in zip(foods, sides):
#     print(food, '-->', side)
   
#ex26 zip two lists into a tuple or a dictionary
# foods=["aa", "bb", "cc", "dd", "ee"]
# sides=["AA", "BB", "CC"]
# tuplist=list(zip(foods, sides))
# print(tuplist)

# dic=dict(zip(foods, sides))
# print(dic) 


#ex27 make a combination of two sequence data types
# seq1='abc'
# seq2=(1,2,3)
# print([(x,y) for x in seq1 for y in seq2])

#28 overlap a list
# L=[[row+(i*3) for row in [10,11,12,13]] for i in [0,1,2]]
# print(L)
#i=0, 10, 11, 12, 13
#i=1 13, 14, 15, 16
#i=2 16, 17, 18, 19

        