import xml.etree.cElementTree as ET
import os.path
class Annotation():
  coordinateX = []
  coordinateY = []
  border = [0,0,0,0] #A 4 - index list [leftmost, rightmost, upmost, downmost]
  box = [0,0]# A 2 - index list [width, length]
  def __init__(self, index, name):
    self.index = index
    self.name = name
  def compute_border(self):
    self.border[0] = self.coordinateX.min()
    self.border[1] = self.coordinateX.max()
    self.border[2] = self.coordinateY.min()
    self.border[3] = self.coordinateY.max()
  def compute_box(self):
    self.box[0] = self.border[1] - self.border[0]
    self.box[1] = self.border[3] - self.border[2]


#file_name = "patient_004_node_4.xml"
def read_xml(file_name):
  annlist = []
  tree = ET.ElementTree(file = file_name)
  index = 0

  for elem in tree.iter("Annotation"):
     ann = Annotation(index, elem.get('Name'))
     print (index)
     for coor_elem in elem.iter("Coordinate"):
       X = coor_elem.get('X')
       Y = coor_elem.get('Y')
       ann.coordinateX.append(X)
       ann.coordinateY.append(Y)
     annlist.append(ann)
     index += 1

  #compute the annotation block
  for ann in annlist:
    ann.compute_border()
    ann.compute_box()
  return annlist
