class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print ("this is your computer configaration:", self.cpu, self.ram)
        
        
        
    
#this is the way to define a obejsts for class    
com1 = computer ("i5", "16GB")

#how to access/print classes
com1.config()