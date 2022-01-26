class Category:
  def __init__(self, name):
      self.name = name
      self.ledger = []
    
  def deposit(self, amount, description = ""):
      self.ledger += [{"amount":amount, "description":description}]
  
  def withdraw(self, amount, description = ""):
      if self.check_funds(amount):
          self.ledger += [{"amount":-amount, "description":description}]
          return True
      else:
        return False
          

  def check_funds(self, money):
      balance = sum([lista["amount"] for lista in self.ledger])
    
      if money>balance:
          return False
      elif money<=balance:
          return True
  
  def get_balance(self):
      return sum([lista["amount"] for lista in self.ledger])

  def __str__(self):
        
      output = "*"*((30-len(self.name))//2) + self.name + "*"*((30-len(self.name))//2 + len(self.name)%2) + "\n"
    
      amour = [lista["description"][:23]+(" "*(30 - (len(lista["description"][:23].strip()) +len(str("{:.2f}".format(lista["amount"])))) ) )+ str("{:.2f}".format(lista["amount"]))+"\n" for lista in self.ledger]
      for mm in amour:
          output += mm
      output += "Total: " + str("{:.2f}".format(sum([lista['amount'] for lista in self.ledger])))
      return output
    
  def transfer(self,amount, category):
      if self.check_funds(amount):
          self.ledger += [{"amount":-amount, "description": f'Transfer to {category.name}'}]
          category.deposit(amount,f"Transfer from {self.name}")
          return True
      else:
        return False
def create_spend_chart(lista):
  nombres = []
  perc_spent = []
  m=0
  for category in lista:
      perc_spent += [0]
      for inner in category.ledger:
          if inner["amount"] <0:
              perc_spent[m] += -inner["amount"]
      m += 1
      nombres += [category.name]
      
  total = sum(perc_spent)
  for x in range(0,len(perc_spent)):
      perc_spent[x] = int((perc_spent[x]/total)*10)*10

  output = "Percentage spent by category"
  for y in range(100,-10,-10):
      output += "\n"+ " "*(100>y) +" "*(y==0) +f"{y}|"
      for perc in perc_spent:
          if perc >= y:
              output += " o "
          else:
              output += "   "
      output += " "
  output += "\n    "+ "-"*(3*len(lista) + 1)
    
  total = max([len(m) for m in nombres])
  for number in range(total):
      output += "\n    "
      for letter in nombres:
          if len(letter) > number:
              output += " "+letter[number]+" "
          else:
              output += "   "
      output += " "
        
  return output
