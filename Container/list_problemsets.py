#q1 make an empty list, add these values so that it prints [100, 200, 300]
# myList=[]
# myList.append(100)
# myList.append(200)
# myList.append(300)
# print(myList)

#q2 what could be the outcome of a following code?
# list_odd=[1,3,5,7,9]
# list_even=[2,4,6,8,10]
# print(list_odd[-3]) #5
# print(list_odd[1+3]) #7 --> should be 9 
# print(list_odd + list_even) #1,3,5,7,9,2,4,6,8,10
# print(list_odd*2) #1,3,5,7,9,1,3,5,7,9,

#q3 input four numbers and append to a list. print 4th and 3th numbers
# list=[]
# n=int(input("1st number"))
# list.append(n)
# n=int(input("2nd number"))
# list.append(n)
# n=int(input("3rd number"))
# list.append(n)
# n=int(input("4th number"))
# list.append(n)

# print("number in {}th: {}".format(4, list[3]))
# print("number in {}th: {}".format(3, list[2]))


#q4 you are given a following list: string=['a', 'b', 'c', 'd', 'e', 'f']
#print as following: ['a', 'b', 'c'], ['c', 'd', 'e'], ['b', 'c']
# string=['a', 'b', 'c', 'd', 'e', 'f']
# print(string[0:3])
# print(string[2:5])
# print(string[1:3])

#q5 make an empty list, enter 20 random numbers between 0-99 and print each of them with its index.
# import random
# list=[]
# for i in range(20):
#     r=random.randint(0,99)
#     list.append(r)

# for k in range(20):
#     print("[{}:{}]".format(k, list[k]), end='')
#     if (k%5==4):
#         print()


#q6 you are givn a list spell=['j', 'e', 's', 'u', 's'] and are required to change 's', 'u', 's' to 'l', 'l', 'y'
#use slice to replace them.
# spell=['j', 'e', 's', 'u', 's']
# spell[2:5]=['l', 'l', 'y']
# print(spell)


#q7 you are given a list number=[2,4, 8, 10] insert 6 in number[2]'s position
# number=[2,4,8,10]
# number.insert(2, 6)
# print(number)

#q8 expect the result of the following code
# list1=['a', 'b', ['c', 'd'], 1, [2, 3], 'e']
# len(list1)
# print(['b'] in list1) #t --> should be false!
# print(['d'] in list1) #f 
# print('a' in list1) #t
# print([2,3] in list1) #t

#q9 using the list xs=range(10) and for, make the following lists:
# [0,2,4,6,8,10, 12, 14, 16, 18]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [0, 2, 4, 6, 8]

# xs=range(10)
# list1=[]
# list2=[]
# list3=[]

# for i in range(10):
#     list1.append(i*2)
# print(list1)

# for i in range(1,11):
#     list2.append(i*i)
# print(list2)

# for i in range(5):
#     list3.append(list1[i])
# print(list3)

#q10 merge int_num_a and int_num_b lists into int_num_c list. print its components backward.
# int_num_a=[0,1,2,3]
# int_num_b=[4,5,6]

# int_num_c=int_num_a + int_num_b
# print(int_num_c)
# for num in reversed(int_num_c):
#     print(num, end='')


#q11 Tom applied to a math exam five times and received 90, 75, 30, 100, 83, respectively. 
# store these scores in a list named score and calculate the total and average scores.
# score=[90, 75, 30, 100, 83]
# tot=0
# for i in score:
#     tot+=i
# print(tot)
# print("%.2f"%(tot/5))

#q12 myList=[100, 200, 300] 
# add [400, 300, 200] to this list
# sort this list in an ascending order
# myList=[100, 200, 300]
# print(myList)
# myList2=[400, 300, 200]
# list=myList+myList2
# print(list)
# print(sorted(list))

#q13 insert a value of 3 in 2nd position of the list. 
# myList=[1,5,10]
# myList.insert(2,3)
# print(myList)
# print(myList.index(1))
# print(myList.index(5))
# print(myList.index(3))
# print(myList.index(10))

#q14 let the user input 5 numbers and store them in a list. print the average.
# list=[]
# tot=0
# for i in range(5):
#     a=int(input("input an integer"))
#     list.append(a)
#     tot+=a
# print("average=%.2f"%(tot/5))

#q15 let's rol a dice 50 times (using random) and print the frequency of each numbers on the dice. 
#which number appeared most frequently?
# import random
# list=[]
# for i in range(50):
#     r=random.randint(1, 6)
#     list.append(r)

# freq=[0, 0, 0, 0, 0, 0]
# for i in range(50):
#     k=list[i]
#     freq[k-1]+=1

# for i in range(6):
#     print("{} appeared {} times".format(i, freq[i]))

# a=max(freq)
# for i in range(len(freq)):
#     if a==freq[i]:
#         ind=i
    
# print("the most frequently appeared number and its frequency were {}/{}: ".format(i,a) )

#16 remove a value from a list and print out the final list: [1,3,5,7,9]
# myList=[1,2,3,4,5,6,7,8,9,10]

# for i in range(2, 11, 2):
#     myList.remove(i)

# print(myList)


#q17 flip the order of favorite_list and print it
# favorite_list=['hotel california', 7, 'tiger', 'true']
# print(reversed(favorite_list))


##############. .................................... reverse/reversed
# l=[3,2,4,6,1]
# print(l)
# l1=list(reversed(l))
# #l#.reverse()
# print(l)
# print(l1)


############## ................................... sort/sorted key lambda
l=[9,4,7,3,2,1]
# print(type(l))
# # l.sort()
# print(l)
# l1=sorted(l)
# print(l, l1)
#########....................................... descending sort 
# print(l)
# l.sort(reverse=True)
# print(l)


########## .................................... using others as key
# l=[[3,10],[1,50],[2,40]]
# # l.sort()
# l.sort(key=lambda x :[x[1]])
# print(l)////////////////////////////////


l=['orange', 'banana', 'grape', 'apple']
l1=sorted(l, key=lambda x:x[-1])
print(l1)
#q18 list names=["lee", "park", "ha"] stores the names of lab members. 
#is member "lee" present in the lab?
# names=["lee", "park", "ha"]
# if ("lee" in names):
#     print("{} is currently working at the lab".format("lee"))
# else:
#     print("{} is currently not working at the lab".format("lee"))
    
#q19 Tom is trying to write a program that checks whether the number of list elements is 5.
# write the code for Tom and conclude whether numlist=[5, 9, 301, 714] satisfies the criteria
# numlist=[5, 9, 301, 714]
# if (len(numlist)==5):
#     print("this list has five elemenets")
# else: 
#     print("this list does not have five elements")


#q20 itereate the int_num_a three times and form a new list int_num_c
# int_num_a=[1,2,3]
# int_num_c=int_num_a*3
# print(int_num_c) 


#q22 collect the surnames from the names in the lists. align them in ascending order.
# mList=["HONG Gildong", "JANG Dong gun", "LEE Jong Suk", "SEO Tae ji"]
# fList=["KANG Soo young", "MIN So jiin", "NAM Suji", "AHN young mi"]

# list=[]
# for ele in mList:
#     list.append(ele.split()[0])

# for ele in fList:
#     list.append(ele.split()[0])

# print(list)
# print(sorted(list))


#q23 you are given a list myList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
# split them into a group of 4 (3 groups with 3 elements and 1 group with 2 elements)
# myList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

# list1=myList[:3]
# list2=myList[3:6]
# list3=myList[6:9]
# list4=myList[9:11]

# print(list1)
# print(list2)
# print(list3)
# print(list4)

#q24 append "zoo" element to the List and align them in alphabetical order
# List=["blind", "apple", "coin"]
# List.append("zoo")
# print(sorted(List))

#q25 from the list number=[2,4,5,6,8,10]
# make a new list2 composed of smallest and largest number only
# number=[2,4,5,6,8,10]
# list2=[]
# list2.append(min(number))
# list2.append(max(number))
# print(list2)

#q26 find the minimum, maximum numbers and their index
# List=[70, 100, 80, 60, 90, 30, 20, 50]
# print("maximum: {} ({})".format(max(List), max(List).index))
# print("maximum: {} ({})".format(max(List), max(List).index))

# q27 make two lists, merge them and align the elements in descending order
# final results should look as follows:
# after merge: [['apple', 100], ['orange', 200], ['kiwi', 300], ['banana', 400], ['banana', , 500]]
# after sorting: [['orange', 200], ['kiwi', 300], ['grape', 500], ['banana', 400], ['apple', 100]]

# fruits=['apple', 'orange', 'kiwi', 'banana', 'grape']
# price=[100, 200, 300, 400, 500]

# list=[]
# newlist=[]
# for i in range(5):
#     list=[]
#     list.append(fruits[i])
#     list.append(price[i])
#     newlist.append(list)
# print(newlist)

# print(sorted(newlist, key=str, reverse=True))

#q28 Teacher Alice has a list of vocabularies for her english vocabulary test. 
#from the following three lists, Alice would like to make a test that
#includes 'maintenance' with at leaast 5 vocabularies.
# write a code that can verify the list eligible for the vocabulary test

# list_ex1=["risk", "issue", "test", "maintenance", "maturity"]
# list_ex2=["security", "plan", "design", "systematic", "safety"]
# list_ex3=["mainttenance", "verifaction", "validation"]

# if "maintenance" in list_ex1 and len(list_ex1)>4:
#     print("list_ex1 is eligible")
# if ("maintenance" in list_ex2 && len(list_ex2)>4):
#     print("list_ex2 is eligible")
# if ("maintenance" in lizst_ex3 && len(list_ex3)>4):
#     print("list_ex3 is eligible")

#q29 makea list of 4x5 and input of 3 starting from 0
# list=[]
# flist=[]
# cnt=0
# for i in range(20):
#     list.append(3*i)
#     cnt+=1
#     if (cnt%5)==0:
#         flist.append(list)
#         list=[]

# for row in flist:
#     for ele in row:
#         #print(f'{ele:<3}', end=' ')
#         # print('{1:<3}{0:<3}'.format(ele,ele*2), end=' ')
#         # print(f'{ele*2:<3}{ele:<3}', end=' ')
#         #print(f'{ele:>3}', end=' ')
#        #print(f'{ele:^3}', end=' ')
#     print()

