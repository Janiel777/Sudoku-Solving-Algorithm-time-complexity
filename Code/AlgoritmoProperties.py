

class AlgoritmoProperties:
  def __init__(self):
    self.times = list()
    self.averageTimes = list()
    self.itWorks = True
    self.name = ""
    self.maxTime = list()
    
  def resetValues(self):
    self.times.clear()
    self.averageTimes.clear()
    self.itWorks = True
    self.name = ""