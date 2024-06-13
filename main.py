"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            ID = input("ID:")
            city = input("City:")
            age = input("Age: ")
            branchcodes = input("Branch(es):").split(',')
            branchcodes = [int(code.strip()) for code in branchcodes]  # Convert to list of integers
            salary = int(input("Salary:"))
            engineer = Engineer(name, age, ID, city, branchcodes, salary)
            engineer_roster.append(engineer)
        
        elif last_input == 2:
            name = input("Name:")
            ID = int(input("ID:"))
            city = input("City:")
            age = int(input("Age:"))
            branchcodes = input("Branch(es):").split(',')
            branchcodes = [int(code.strip()) for code in branchcodes]  # Convert to list of integers

            salary = int(input("Salary:"))

            superior_id = int(input("Superior ID (None if Head):"))

            salesperson = Salesman(name, age, ID, city, branchcodes, "Rep", superior_id, salary)
            sales_roster.append(salesperson)

        elif last_input == 3:
            ID = int(input("ID: "))
    
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
    
            if not found_employee:
                print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")
    
                branch_names = [branchmap[code]["name"] for code in found_employee.branches]
                print(f"Branches: {','.join(branch_names)}")
    
                print(f"Salary: {found_employee.salary}")
    
        elif last_input == 4:
            ID = int(input("ID: "))
            new_code = int(input("New Branch Code: "))
    
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
    
            if not found_employee:
                raise ValueError("No such employee")
    
            found_employee.migrate_branch(new_code)

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            pos = input("Enter Position to promote to (Rep, Manager, Head): ")
    
            found_employee = None
            for salesman in sales_roster:
                if salesman.ID == ID:
                    found_employee = salesman
                    break
    
            if not found_employee:
                raise ValueError("No such salesman")
    
            found_employee.promote(pos)


        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            increment_amt = int(input("Enter Increment Amount: "))
    
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == ID:
                    found_employee = employee
                    break
    
            if not found_employee:
                raise ValueError("No such employee")
    
            found_employee.increment(increment_amt)
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
    
            found_employee = None
            for salesman in sales_roster:
                if salesman.ID == ID:
                    found_employee = salesman
                    break
    
            if not found_employee:
                raise ValueError("No such salesman")
    
            superior_id, superior_name = found_employee.find_superior()
            if superior_id is None:
                print("No superior found (Head position)")
            else:
                print(f"Superior ID: {superior_id}, Superior Name: {superior_name}")
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            
            found_employee = None
            found_superior = None
            
            for salesman in sales_roster:
                if salesman.ID == ID_E:
                    found_employee = salesman
                elif salesman.ID == ID_S:
                    found_superior = salesman
            
            if not found_employee or not found_superior:
                raise ValueError("One or both employees not found")
            
            found_employee.add_superior(ID_S)