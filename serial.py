"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start=100):
        self.start = self.next = start

    def generate(self):
        self.next +=1
        return self.next -1
    
    def restart(self):
        self.next = self.start

        


            
                 
       
            
    

 
