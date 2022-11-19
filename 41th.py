name = ['John', 'Martin', 'Mike', 'Mary']
salary = [4000, 5500, 6000, 4500]

employees = {name[i]: salary[i] for i in range(len(name))}
print(employees)
