class User:
    def __init__(self, name, age):
    
        self.name = name
        self.age = age
       

    def login(self):
        print(f"{self.name} has logged in")
        self.loggedin = True
        