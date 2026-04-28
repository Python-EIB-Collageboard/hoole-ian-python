from uuid import uuid8
import json
from logging import info, error
from pathlib import Path

class DataStore:

  def __init__(self):
    filePath = Path.cwd() / "data.json"
    jsonData = []
    try:
      info("opening file at", filePath)
      with open(filePath, 'r') as file:
        jsonData = json.load(file)
    except:
      info('failed to find file, creating')
      try:
        with open('data.json', 'w') as file:
          file.write("{}")
          
      except Exception as e:
        error("Failed to create file", e)
    self.data = dict(jsonData)

  def create(self, item):
    key = str(uuid8())
    self.data.update({key: item})
    self.updateFile()
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
      self.updateFile()
    return old

  def delete(self, key):
    item = self.data.pop(key, None)
    self.updateFile()
    return item

  def updateFile(self):
    try:
      with open('data.json', 'w') as file:
        file.write(json.dumps(self.data, indent=2))
    except:
      error("Failed to write to file")
