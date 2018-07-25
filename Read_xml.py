import xml.etree.cElementTree as ET
import os.path
import math
"""
This program is used for read an annotation part and store in class Annotation
border = [0,0,0,0] #A 4 - index list [leftmost, rightmost, upmost, downmost]
"""
class Annotation():
  def __init__(self, **kwargs):
     #store the ann information in xml tree
    for key in kwargs:
        self.__dict__[key] = kwargs.get(key)
    self.coordinateX = []
    self.coordinateY = []
    self.border = [0,0,0,0]
  def compute_border(self):
    self.border[0] = min(self.coordinateX)
    self.border[1] = max(self.coordinateX)
    self.border[2] = min(self.coordinateY)
    self.border[3] = max(self.coordinateY)

#file_name = "patient_004_node_4.xml"
def read_xml(file_name):
  annlist = []
  tree = ET.ElementTree(file = file_name)
  for index, elem in enumerate(tree.iter("Annotation")):
     if(elem.get("Type") != "None"):
       ann = Annotation(**{"name" : elem.get("Name"), "type" : elem.get("Type"), "index" : index, "part" : elem.get("PartOfGroup")})
       for coor_elem in elem.iter("Coordinate"):
         X = coor_elem.get("X")
         Y = coor_elem.get("Y")
         ann.coordinateX.append(int(float(X)))
         ann.coordinateY.append(int(float(Y)))
       annlist.append(ann)
       print (ann.coordinateX)

  print(len(annlist))
  #compute the annotation block
  for ann in annlist:
    print (ann.coordinateX)
    ann.compute_border()
  for item in annlist:
      print (item.name)
      print (item.index)
      print (item.border)
  return annlist

#read_xml("patient_004_node_4.xml")
