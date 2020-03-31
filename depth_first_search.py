# learning how to implement depth first search
class Node:
  # python version on constructor
  def __init__(self, name):
    self.children = []
    self.name = name

  # method for adding a name 
  def addChild(self, name):
    self.children.append(Node(name))
    return self

  # depth first search implemented, it calles itself from left to right , each branch at a time 
  def depthFirstSearch(self, array):
    array.append(self.name)
  for child in self.children:
    child.depthFirstSearch(array)
  return array