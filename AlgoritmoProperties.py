

class AlgoritmoProperties:
  def __init__(self):
    self.times = list()
    self.averageTimes = list()
    self.itWorks = True
    self.name = ""
    
  def resetValues(self):
    self.times.clear()
    self.averageTime = 0
    self.itWorks = True
    self.name = ""