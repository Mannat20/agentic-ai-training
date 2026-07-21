class Bank:
    def __init__(self,name,id,branch):
        self.name=name
        self.id=id
        self.branch=branch

class employee:
    def __init__(self,name,id,address,phone_number,email,salary,designation):
        self.name=name
        self.id=id
        self.address=address
        self.phone_number=phone_number
        self.email=email
        self.salary=salary
        self.designation=designation



class branch:
    def __init__(self,name,address,employees,id,phone_number,timings):
        self.name=name
        self.address=address
        self.employees=employees
        self.id=id
        self.phone_number=phone_number
        self.timings=timings

    


# bank=Bank()
# branch1=branch()
employee1=employee(
    'Rahul',101,'#34,ABC',7628635429,'rahul@gmail.com',67000,'HR'
)
employee2=employee(
    'Anjali',102,'#78,ABC',9111176543,'Anjali@gmail.com',89000,'Manager'
)
employee3=employee(
    'Sam',103,'#90,SectarA',8999945555,'sam@gmail.com',90000,'Helper'
)
employee_dict=[employee1,employee2,employee3]
branch1=branch(name='EAST',address='#34,model town',employees=employee_dict,id='89A',phone_number='+91 7876545668',timings='2-4PM')
bank=Bank(name='HDFC',branch=branch1,id='1A')
print('Bank: ',bank,vars(bank),'\n')
print('Branch: ',branch1,vars(branch1),'\n')
print('Employee1: ',employee1,vars(employee1),'\n')
print('Employee2: ',employee2,vars(employee2),'\n')
print('Employee3: ',employee3,vars(employee3))