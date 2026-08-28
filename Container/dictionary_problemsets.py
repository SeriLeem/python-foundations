# #q1 using a dictionary with keys and values, store and print the dictionary.
# # my_dict={1:'cat', 2:'dog', 3:'horse', 4:'fish'}
# # print(my_dict)

# #q2 the code below used if.
# #write a code that can replace if.
# #given code:
# # print("fishballs, sausage, dumplings, steak")
# # selection=input("select your order")
# # if selection=="fishballs":
# #     price=1000
# # elif selection=="sausage":
# #     price=2000
# # elif selection=="dumplings":
# #     price=3000
# # else:
# #     price=4000
# # print('cost of your', selection, 'is', price)

# #new code
# # my_menu={'fishballs':1000, 'sausage':2000, 'dumplings':3000, 'steak':4000}
# # selection=input('select your order')
# # print('cost of your', selection, 'is', my_menu[selection])

# #what could be the result of executing the code below?
# # L1=[1,2,3]
# # L2=[4,5,6]
# # d={'low':L1, 'high':L2}
# # e=d #shallow copy
# # f=d.copy() #deep copy
# # d['low']=[10,20,30]
# # d['high'][1]=500
# # print(e) #low:[10,20,30], high:[4,500,6]
# # print(f) #low:[1,2,3], high:[4,5,6]

# #q4 4 four menus at the cafe are Americano, Cafe latte, Green tea, Mocha latte
# # each menu costs 2000, 2500, 3000, 4500, respectively.
# # make a list of these menus using a dictionary and check whether your favorite menu is included
# # my_cafe=dict([('Americano', 2000), ('Cafe latte', 2500), ('Green tea', 3000), ('Mocha latte', 4500)])
# # selection=input('select an item')
# # if selection in my_cafe:
# #     print(selection, 'is here!')
# # else: 
# #     print(selection, 'is not here!')

# #q5 stationary stores have variety of products.
# # pencil - 200, pen - 800, eraser - 500, ruler - 300
# # use a dictionary to store these info and print only the price as a list
# # key=['pencil', 'pen', 'eraser', 'ruler']
# # value=[200, 800, 500, 300]
# # dict_values=zip(key, value)
# # print(value)

# #q6 menus of the restaurant are as follows
# # beef 5000, fish 5500, udon 2500, sushi 9900
# my_menu={'beef':5000, 'fish':5500, 'udon':2500, 'sushi':9900}
# #or key, value in my_menu.items():
#     #print('{}:{}'.format(key, value))
    
# #for key in my_menu:
# #     print('{}'.format(key))
     
# # #for key in my_menu.items():
# #     #print('{}'.format(key))

# # #for value in my_menu.values():
# #     print('{}'.format(value))

# #q7 you are given a dictionary dd={'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
# # print (key, value) in alphabetical order
# # print (key, value) in ascending numbers
# # dd={'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
# # print(sorted(dd))
# # print(sorted(dd, key=dd.values))

# #q8 you are given a string s='pone two one two three four'
# # use a dictionary to print each words without repetition.
# # s='one two one two three four'
# # # import collections
# # # print(list((collections.Counter(s))))

# # import re
# # s1=re.sub()

# #q9
# # you are given an information about fruits kevin has in his house.
# # he would like to purchase fruits so that it maintains five.
# # write a code that can tell him the kind of fruit he has to buy and the total cost.

# # fruits={('banana', 2000):3, ('apple', 1500):5, ('strawberry', 1800):2, ('tomatoes', 2300):5}
# # total=0

# # for (f,p), quant in fruits.items():
# #     if quant<5:
# #         print('shoud buy {}'.format(f))
# #         print('the cost is {}'.format(p*(5-quant)))
# #         total+=p
# #     else:
# #         print('no need to buy {}'.format(f))
        

# # print('the total cost will be {}'.format(total))
    

# #q10 jacob has a number of min, jin, jay, ken and ain in his phonebook.
# # search for jake and jin's number and if there are, print them.

# # tel={'min':'010-1111-1111', 'jin':'010-2222-2222', 'jay':'010-3333-3333', 'ken':'010-4444-4444', 'ain':'010-5555-5555'}

# # name=input('whose number would you like to search for?')

# # if name in tel:
# #     print(tel[name])
# # else:
# #     print('there is no such name!')

# #q11
# #you are given a list of ids and pws. make a login program

# # idlist={'gana':1234, 'dong':1111, 'min':4321, 'sumin':2345}

# # id=input('input your id: ')
# # if id in idlist:
# #     pw=input('input your password: ')
# #     #print(idlist[id])
# #     if pw==idlist[id]:
# #         print("{}, you have successfully logged in".format(id))
# #     else:
# #         print('check your password')
# # else:
# #     print('you have not registered')

#q12 make a dictionary program
# my_dict={}
# while():
#     a=input('1 for new vocab registration, 2 for search vocab, 3 for exit')
#     if a==1:
#         eng=input('english word')
#         kor=input('korean meaning')
#         my_dict[eng]=kor
#     elif a==2:
#         find=input('which word do you wish to search for?')
#         if find in my_dict:
#             print(my_dict[find])
#         else:
#             print('there is no such vocabulary')
#     elif a==3:
#         break


#q13 you have a dictionary containing students name and their scores. 
#use sum() and len() to calculate the average.
# midterm={'prodo':97, 'sally':88, 'neo':70, 'brown':99, 'mini':70}
# for i in range(len(midterm)):

#q14 you are given a string that contains 'a', 'b', 'c' and 'e'
# convert a, b, c, e to w, x, y, z, respectively.
# also, convert w, x, y, z to a, b, c, e, respectively.

# cv={'a':'x', 'b':'y', 'c':'z', 'e':'z'}
# str='cabsz'
# for i in range(len(str)):
#     if str[i] in cv:
#         str.replace(str[i], cv)
        
#q15 you are given a dictionary as follows: n={'kr':'south korea', 'us':'united states', 'jp }

    
