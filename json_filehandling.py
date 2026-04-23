# import json
# data={'name':['kiran','amal'],'age':[30,40]}
# f=open("data2.json",'w')
# json.dump(data,f,indent=4)
# f.close()

import json
f=open("data2.json",'r')
data=json.load(f)
print(data)
f.close()