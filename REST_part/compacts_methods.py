import json
from types import DynamicClassAttribute
from operator import itemgetter

class PutShelf:
  def __init__(self):
    try:
      with open('compacts.json', 'r') as collection:
        self.compacts = json.load(collection)
        # self.compacts = sorted(json.load(collection), key=itemgetter('mark'), reverse=True) # zapis sortujący 
    except FileNotFoundError:
      self.compacts = []

  def collect(self):
     return self.compacts

  def choose(self, id):
    compact = [compact for compact in self.collect() if compact['id']== id]
    if compact:
      return compact[0]
    return []


  def make(self, data):
      self.compacts.append(data)
      self.save_collection()

  def save_collection(self):
    with open('compacts.json', 'w') as collection:
        json.dump(self.compacts, collection)  # zapisuje zebrane dane w pliku json
    
  def adding(self, id, data):
      compact = self.choose(id)
      if compact:
        index = self.compacts.index(compact)
        self.compacts[index] = data
        self.save_collection()
        return True
      return False

  def delete(self, id):
      compact = self.choose(id)
      if compact:
          self.compacts.remove(compact)
          self.save_collection()
          return True
      return False

"""
  def sorting_validator(self):
      sorted_compacts = sorted(self.compacts, key=lambda k: k['mark'])
      # return sorted_compacts

  def sort(self):
      self.sorting_validator()
      return self.compacts
"""

compacts = PutShelf()