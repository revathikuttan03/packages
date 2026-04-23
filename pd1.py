import pandas as pd

# data={'name':['kiran','ammu','appu'],'age':[15,18,12]}

# a=pd.DataFrame(data)
# print(a)
# data={'name':[],'place':[]}
# x = True
# while x:
#     choice =input("Enter your choice:(add,display,exit): ")
#     match choice:
#         case "add":
#             a=input("Enter your name: ")
#             b=input("Enter your place: ")
#             data['name'].append(a)
#             data['place'].append(b)
#         case "display":
#             z=pd.DataFrame(data)
#             print(z)
#         case 'exit':
#             x=False
        

import pandas
import json
f=open("store.json",'r')
data= json.load(f)
f.close()
x=True
while x:
    Choice=input("Enter your choice:")
    match Choice:
        case "add":
            a=input("Enter your name: ")
            b=int(input("Enter your maths: "))
            c=int(input("Enter your english: "))
            d=int(input("Enter your science: "))
            data['name'].append(a)
            data['maths'].append(b)
            data['english'].append(c)
            data['science'].append(d)
            av=(b+c+d)/3
            data['avg'].append(av)
            f=open('store.json','w')
            json.dump(data,f,indent=4)
            f.close()
        case "display":
            r=open('data.txt','w')
            v=pd.DataFrame(data)
            print(v)
            r.write(str(v))
            r.close()
        case "exit":
            x=False
    




    

