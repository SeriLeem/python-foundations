#ex1 making dictionary with various ways
# my_dict={}
# print(type(my_dict))
# print(my_dict)
# my_dict_1={'fishing':'to catch a fish', 'fishing boats':'boats used for fishing'}
# print(my_dict_1)

# my_dict_2={1:'Hydrogen', 2:'Helium', 2:'Lithium', 3:'Lithium'}
# print(my_dict_2)

# my_dict_3={'name':'mr.Kang', 14003:[3,2,0,1]}
# print(my_dict_3)

# my_dict_4=dict([(1,'seoul'), (2,'Busan')])
# print(my_dict_4)
# my_dict_5={'name':'aaa', 'age':25, 'manager':'Samsung', 'job':'researcher'}
# print(my_dict_5)
# price={('noodle', 'rice'):'20 dollars', ('pizza', 'hotdog'):'40dollars'} #using tuples as keys
# print(price)

#ex2 Dictionary Comprehension
# d1={w:1 for w in 'abcdef'}
# print(d1)

# ex3 make a dictionary with two lists
# import sys
# keys=['one', 'two', 'three']
# values=[1,2,3]
# d=dict(zip(keys, values))

# for k in d:
#     print(k)
# print()

# for key, value in d.items():
#     print(key, value)


#ex4 make a dictionary with two sequences (string, set, tuple)
# a1='abcd'
# a2=(1,2,3,4)
# d1={x:y for x, y in zip(a1, a2)}
# print(d1)

# d2={w:k for k, w in [(1, 'one'), (2, 'two'), (3, 'three')]}
# print(d2)

# d3={w:k+1 for k, w in enumerate(['one', 'two', 'three'])}
# print(d3)


#ex5 make a dictionary using nested for loop
# d={(k,v):k for k in range(3) for v in range(2)}
# print(d)

#ex6 make a dictionary (English to korean) and search the word
# english_dict=dict()

# english_dict['one']='hana'
# english_dict['two']='dul'
# english_dict['three']='saet'

# word=input("input a word")
# print(english_dict[word])

#ex7 let's search for the value in the dictionary.
# also edit and add values in the dictionary
# my_phone={"hong":"111-1111", 'kang':'222-2222', 'kim':'333-3333'}
# print(my_phone)
# print(my_phone['hong']) #search for the value using the key
# print(my_phone.get('hong'))
# print()

# my_phone['hong']='xxx' #edit the value
# print(my_phone)
# print()

# my_phone['bts']='444-4444'
# my_phone['exo']='000'
# print(my_phone)


#ex8 delete a value from a dictionary
# my_idol={'occupation':'singer', 'age':18, "name":'suzy', 'date of birth':'1994-10-10'}
# print(my_idol)
# print()

# print(my_idol.pop('date of birth')) #bring the value and delte it simultaneously
# print(my_idol)
# print()

# del my_idol['age'] #delete the value
# print(my_idol)
# print()

# print(my_idol.popitem()) #bring a random value and delete simultaneously
# print(my_idol)
# print()
# my_idol.clear() #empty the dictionary
# print(my_idol)
# del my_idol
# #print(my_idol)


#ex9 learning methods realted to dictionary
# d={'one':1, 'two':2, 'three':3}

# d2=d.copy() #copying the dictionary
# print(d2)

# d['four']=4 #adding a new key-value
# print(d)

# d3={'nine':9, 'ten':10}
# d.update(d3)
# print(d)

# d.popitem()
# print(d)

# d.pop('two')
# print(d)


#ex10 iterate the values in set and dictionary
# print("--------- for in a set ---------")
# for a in {1,2,3}:
#     print("a=", a)

# print("--------- for in a dict ---------")
# D={'one':1, 'two':2, 'three':3}
# for key in D:    #NOT for key in D.keys()
#     print('key=', key)
    
# for value in D.values():   #should be value in D.values()
#     print('value = ', value)

# for item in D.items():  #type(item)=tuple --> prints out both key and value
#     print("item=", item)
    
# for key, value in D.items():
#     print('key={0}:value={1}'.format(key, value))
    

#ex11 make a dictionary from these two lists
# keys=['one', 'two', 'three', 'four']
# values=[1,2,3,4]
# d=dict(zip(keys, values))
# print(d)
   
#ex12 allocated an equal value using fromkeys() method
# d1={}.fromkeys('abcde', 1)
# print(d1)
# d2={}.fromkeys('abcde', [])
# d2['b'].append(5) #problem occurrs (every keys in one dictionary share a common address) --> go to ex13
# print(d2) 

# #ex13 use an individual value object 
# #problem from ex12 solved
# d=dict((c,[]) for c in 'abcde')
# print(d)
# d['a'].append(10)
# print(d)

#ex14 you are given a string s='We propose to start by making it possible to teachign programming in Python, an existing scripting language, and to focus on creating creating a new development environment and teaching materials for it.'
#convert all uppercase letters to lowercases. delete ',' and '.'
#print repetitive words only once and print their frequencies.

# s='We propose to start by making it possible to teachign programming in Python, an existing scripting language, and to focus on creating creating a new development environment and teaching materials for it.'
# import re
# s2=re.sub('[,.]','',s.lower())
# print(s2)
# ws=s2.split()

# import collections
# print(collections.Counter(ws))

# print(sorted(list(collections.Counter(ws).items())))

#ex15 use dictionary to print various combinations of foods
# foods={'pizza':'pickles', 'ramen':'kimchi', 'beer':'peanuts'}

# while(True):
#     myfood=input("which do you like:"+ str(list(foods.keys())))
#     if myfood in foods:
#         print("<%s> pairs well with <%s>"%(myfood, foods.get(myfood)))
#     elif myfood=='end':
#         break
#     else:
#         print("we do not have such food. please double check")


#ex16 merging two dictionaries
# from itertools import chain
# from collections import defaultdict

# dict1={'bookA':1, 'bookB':2, 'bookC':3}
# dict2={'bookC':2, 'bookD':4, 'bookE':5}
# dict3=defaultdict(list)
# #print(dict3)
# for k, v in chain (dict1.items(), dict2.items()):
#     dict3[k].append(v)
    
# for k, v in dict3.items():
#     print(k,v)


#ex17 error when accessing a non-initialized value --> solved in ex18 
# animals=['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
# dic={}

# for animal in animals:
#     dic[animal]+=1
# print(dic)

#ex18 two ways of solving a problem from ex17
#1
# animals=['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
# dic={}

# for animal in animals:
#     #if key is there, we add 1
#     if animal in dic.keys():
#         dic[animal]+=1
#     #if key is not there, initiate as 1
#     else:
#         dic[animal]=1

# print(dic)

#2
# from collections import defaultdict

# animals=['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
# dic=defaultdict(int)

# for animal in animals:
#     dic[animal]+=1

# print(dic)
# print(dic['door'])
# print(dic)

#19 using defaultdict when giving default value as set
# from collections import defaultdict
# animals=[('dog', 'Ricky'), ('cat', 'Momo'), ('rabbit', 'Jimmy'), ('cat', 'Chars'), ('cat', "Pipy"), ('dog', 'Ricky'), ('dog', 'Ricky')]
# dic=defaultdict(set)

# for animal, name in animals:
#     dic[animal].add(name)
    
# print(dic)

#20 using defaultdict when diving default value as list
# from collections import defaultdict

# animals=[('dog', 'Ricky'), ('cat', 'Momo'), ('rabbit', 'Jimmy'), ('cat', 'Chars'), ('cat', "Pipy"), ('dog', 'Ricky'), ('dog', 'Ricky')]
# dic=defaultdict(list)

# for animal, name in animals:
#     dic[animal].append(name)

# print(dic)