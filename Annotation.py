"""
Define the basic data structure of the annotation
"""
class Annotation(object):
  def __init__(self):
    self.name = " "
    self.type = " "
    self.index = 0
    self.partOfGroup = " "
    self.coordinateX = []
    self.coordinateY = []
    self.xMin = 0
    self.xMax = 0
    self.yMin = 0
    self.yMax = 0

    # Use for record which patch is in the annotation
    self.patchInAnn = {}
    # patch size
    self.patchSize = 50
