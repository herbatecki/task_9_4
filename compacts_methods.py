import json
from types import DynamicClassAttribute
from operator import itemgetter

class PutShelf:
  def __init__(self):
    try:
      with open('compacts.json', 'r') as collection:
        self.compacts = sorted(json.load(collection), key=itemgetter('mark'), reverse=True) # zapis sortujący 
    except FileNotFoundError:
      self.compacts = []

  def collect(self):
     return self.compacts

  def choose(self, id):
     return self.compacts[id] #wybiera jedną z instancji z pliku .json

  def make(self, data):
    data.pop('csrf_token') # wycina zapis 'csrf_token'
    self.compacts.append(data) # resztę dodaje do instancji

  def save_collection(self):
    with open('compacts.json', 'w') as collection:
        json.dump(self.compacts, collection)  # zapisuje zebrane dane w pliku json
    
  def adding(self, id, data):
      data.pop('csrf_token')
      self.compacts[id] = data
      self.save_collection()
"""
  def sorting_validator(self):
      sorted_compacts = sorted(self.compacts, key=lambda k: k['mark'])
      # return sorted_compacts

  def sort(self):
      self.sorting_validator()
      return self.compacts
"""

compacts = PutShelf()