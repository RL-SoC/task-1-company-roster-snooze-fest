#Global variables
engineer_roster = [] #List of engineer instances/objects
sales_roster = [] #List of saleman instances/objects
branchmap = {  
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}

####################################################################

class Employee:
    #Type annotations to denote expected data types of data members
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] #List of branches employee reports to
    salary : int 

    #Parametric constructor for employee objects
    def __init__(self, name, age, ID, city, branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: 
            self.salary = salary
        else: 
            self.salary = 10000 

    #Change city of an employee, return false if no change
    def change_city(self, new_city:int) -> bool:
        if self.city == new_city:
            return False
        else:
            self.city = new_city
            return True

    #Change branch code of an employee, return false if no change
    #should only work on employees who report to 1 branch
    def migrate_branch(self, new_code:int) -> bool:
        if len(self.branches) != 1:
            return False        
        else:
            if self.branches[0] == new_code:
                return False
            else:
                self.branches[0] = new_code
                return True

    #Increment salary by amount specified.
    def increment(self, increment_amt: int) -> None:
        self.salary += increment_amt


class Engineer(Employee):
    position : str # Position in organization Hierarchy
    hierarchy_engineer = {
        "Junior": 0,
        "Senior" : 1,
        "Team Lead" : 2,
        "Director" : 3,
    }
    
    def __init__(self, name, age, ID, city, branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
        if position in {"Junior", "Senior", "Team Lead", "Director" }:
            self.position = position
    
    def increment(self, amt:int) -> None:
        # All other functions are same for engineer and salespeople
        # However, increment will raise the salary by 10% of amt for engineers
        self.salary += 1.1*amt 
        
    def promote(self, pos:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        if self.hierarchy_engineer[pos] > self.hierarchy_engineer[self.position]:
            self.position = pos
            self.increment(0.3*self.salary)
            return True;
        else:
            return False;



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    hierarchy_sales = {
        'Rep' : 0,
        'Manager' : 1,
        'Head' : 2,
    }
    
    def __init__(self, name, age, ID, city, branchcodes, position= "Rep", superior = None, salary = None):
        #Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)

        if position in {'Rep', 'Manager', 'Head'}:
            self.position = position
            
        if self.position == 'Head':
            self.superior = None
        else:
            self.superior = superior 
        
    
    def increment(self, amt:int) -> None:
         self.salary += 1.05*amt
    
    def promote(self, pos:str) -> bool:
        if self.hierarchy_sales[pos] > self.hierarchy_sales[self.position]:
            self.position = pos
            self.increment(0.3*self.salary)
            return True;
        else:
            return False;
         
    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        for salesman in sales_roster:
            if salesman.ID == self.superior:
                return (salesman.ID, salesman.name)
            return (None, None)

    def add_superior(self, sup_id = None) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        if self.position != 'Head':
            self.superior = sup_id
            return True
        else:
            return False
        
    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        (self.branches).append(new_code)