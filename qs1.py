import matplotlib.pyplot as plt
import pandas as pd
data={'year':[],'profit':[]}
x=True
while x:
    choice=input("Enter your choice:")
    match choice:
        case'add':
            a=int(input("Enter the year:"))
            b=int(input("Enter the profit:"))
            data['year'].append(a)
            data['profit'].append(b)
        case 'display':
            b=pd.DataFrame(data)
            print(b)
            print(data['year'])
        case 'graph':
            fig,ax=plt.subplots()
            ax.plot(data['year'],data['profit'])
            plt.show() 
        case 'exit':
            x=False



