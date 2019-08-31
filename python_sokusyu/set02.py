# set01.py

data1 = { "yellow", "red" , "blue" , "black" , "white" }
data2 = { "red","yellow","pink" ,"green" }

for data in data1 | data2:
    print(data)
    
print()
 
for data in data1 & data2:
    print(data)

