import pandas as pd

# data={'name':['kiran','ammu','appu'],'age':[15,18,12]}

# a=pd.DataFrame(data)
# print(a)
data={'name':[],'place':[]}
x = True
while x:
    choice =input("Enter your choice:(add,display,exit)")
    match choice:
        case "add":
            a=input("Enter your name")
            b=input("Enter your place")
            data['name'].append(a)
            data['place'].append(b)
        case "display":
            z=pd.DataFrame(data)
            print(z)
        case 'exit':
            x=False
        
            
