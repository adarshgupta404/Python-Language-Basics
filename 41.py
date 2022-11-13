dic = {}
name =["adarsh", "rohan", "sumit"]
salary = [25000, 30000, 35000]
for key in name:
    for val in salary:
        dic[key] = val;
        salary.remove(val);
        break;
print (dic)