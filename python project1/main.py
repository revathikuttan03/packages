import pandas as pd
import json

try:
    f=open("store.json",'r')
    data= json.load(f)
    f.close()
except:
    data={"name":[],"maths":[],'english':[],'science':[],'avg':[]}
x=True
while x:
    Choice=input("Enter your choice:")
    match Choice:
        case "add":
            try:
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
            except ValueError:
                print("marks only allowed in numbers")
        case "display":
            r=open('data.txt','w')
            v=pd.DataFrame(data)
            print(v)
            r.write(str(v))
            r.close()
        case "exit":
            x=False
        case _:
            print("available choices (add,display,exit)")
    




