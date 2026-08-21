#q1 using a dictionary with keys and values, store and print the dictionary.
# my_dict={1:'cat', 2:'dog', 3:'horse', 4:'fish'}
# print(my_dict)

#q2 the code below used if.
#write a code that can replace if.
#given code:
# print("fishballs, sausage, dumplings, steak")
# selection=input("select your order")
# if selection=="fishballs":
#     price=1000
# elif selection=="sausage":
#     price=2000
# elif selection=="dumplings":
#     price=3000
# else:
#     price=4000
# print('cost of your', selection, 'is', price)

#new code
# my_menu={'fishballs':1000, 'sausage':2000, 'dumplings':3000, 'steak':4000}
# selection=input('select your order')
# print('cost of your', selection, 'is', my_menu[selection])

#what could be the result of executing the code below?
# L1=[1,2,3]
# L2=[4,5,6]
# d={'low':L1, 'high':L2}
# e=d #shallow copy
# f=d.copy() #deep copy
# d['low']=[10,20,30]
# d['high'][1]=500
# print(e) #low:[10,20,30], high:[4,500,6]
# print(f) #low:[1,2,3], high:[4,5,6]

#4 four menus at the cafe are Americano, Cafe latte, Green tea, Mocha latte
# each menu costs 2000, 2500, 3000, 4500, respectively.
# make a list of these menus using a dictionary and check whether your favorite menu is included
# my_cafe=dict([('Americano', 2000), ('Cafe latte', 2500), ('Green tea', 3000), ('Mocha latte', 4500)])
# selection=input('select an item')
# if selection in my_cafe:
#     print(selection, 'is here!')
# else: 
#     print(selection, 'is not here!')
