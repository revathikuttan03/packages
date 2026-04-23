# import csv
# f=open("data1.csv",'w',newline='')
# data=[['name','age','place'],['amal',30,'thrissur'],['kiran',25,'malappuram']]
# w=csv.writer(f)
# w.writerows(data)
# f.close()


import csv
f=open('data1.csv','r')
w=csv.reader(f)
for row in w:
    print(row)

f.close()

