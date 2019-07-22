class Employee:
    def __init__(self, name, emp_id, email_id):
        self.__name=name
        self.__emp_id=emp_id
        self.__email_id=email_id

    def get_name(self):
        return self.__name

    def get_emp_id(self):
        return self.__emp_id

    def get_email_id(self):
        return self.__email_id

class InfosysDirectory:
    def __init__(self,emp_list):
        self.__emp_list=emp_list

    def lookup(self,key_name):
        result_list=[]
        for emp in self.__emp_list:
            if(key_name in emp.get_name()):
                result_list.append(emp)
        self.display(result_list)
        return result_list

    def display(self,result_list):
        print("Search results:")
        for emp in result_list:
            print(emp.get_name()," ", emp.get_emp_id()," ",emp.get_email_id())



emp1=Employee("Kevin",24089, "Kevin_xyz@infosys.com")
emp2=Employee("Jack",56789,"Jack_xyz@infosys.com")
emp3=Employee("Jackson",67895,"Jackson_xyz@infosys.com")
emp4=Employee("Henry Jack",23456,"Jacky_xyz@infosys.com")
emp_list=[emp1,emp2,emp3,emp4]

infy_dir=InfosysDirectory(emp_list)
#Search for an employee
infy_dir.lookup("Jack")