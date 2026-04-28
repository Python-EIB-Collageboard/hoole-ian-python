from dataStore import DataStore

class AppController:

  def __init__(self):
    self.db = DataStore()

  def run(self):
    while True:
      input = self.prompt()
      if(input == "exit"):
        break
      elif(input == "create"):
        response = self.create()
        print(" Input at key:", response)
      elif(input == "get"):
        response = self.get()
        print(" Data at key is:", response)
      elif(input == "read"):
        response = self.read()
        print(response)
      elif(input == "update"):
        response = self.update()
        if(response):
          print(" Replaced:", response)
        else:
          print("No data at key, create instead");
      elif(input == "delete"):
        response = self.delete()
        print(" Deleted:", response)
      else:
        print("Invalid Input")

  def prompt(self):
    print("Valid Operations [Create, Get, Read, Update, Delete, Exit]")
    userInput = input("Input Operation:")
    return userInput.strip().lower()
  
  def create(self):
    userInput = input("Input Item:")
    return self.db.create(userInput)

  def read(self):
    return self.db.read()
  
  def get(self):
    userInput = input("Input Key:")
    return self.db.get(userInput)

  def update(self):
    userKey = input("Input Key:")
    userData = input("Input Data:")
    return self.db.update(userKey, userData)
  
  def delete(self):
    userInput = input("Input Key:")
    return self.db.delete(userInput)

if __name__ == "__main__":
  app = AppController()
  app.run()