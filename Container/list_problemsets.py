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
import random
list=[]
for i in range(50):
    r=random.randint(1, 6)
    list.append(r)

freq=[0, 0, 0, 0, 0, 0]
for i in range(50):
    k=list[i]
    freq[k-1]+=1

for i in range(6):
    print("{} appeared {} times".format(i, freq[i]))

print("the most frequently appeared number and its frequency were {}/{}: ".format(max(freq), freq.index(max) ) )
