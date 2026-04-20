from uuid import uuid8

class DataStore:
  def __init__(self):
    self.data = dict()

  def create(self, item):
    key = str(uuid8())
    self.data.update({key: item})
    return key

  def get(self, key):
    return self.data.get(key)

  def read(self):
    counter = 0
    str = " Idx|                uuid                | Data\n"
    for item in self.data:
      counter += 1
      str += f"  {counter}. {item}:{self.data.get(item)}\n"
    return str

  def update(self, key, item):
    old = self.get(key)
    if(old):
      self.data.update({key: item})
    return old

  def delete(self, key):
    return self.data.pop(key, None)

