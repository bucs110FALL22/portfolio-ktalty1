import time #import time module

class Animal: #Naming class 
  def__init__(self, name, type):
      self.id = time.strftime
     # self.id = self(id)
     # self.id = uuid()
      self.name = name
      self.type = type
      self.arrived = time.strftime ("%d/%m/%Y")
      self.adopted = None

  def set_adopted(self):
      self.adopted = time.strftime ("%d/%m/%Y")

  def__str__():
      result_str = f"{self.name}{[self.type]}
      resulr_str += f"\narrived: {self.arrived}
      result_str += f"narrived: {self.adopted}
    
def main():
      fido = Animal("fido", "cat")
      fido.set_adopted()

  
main()

