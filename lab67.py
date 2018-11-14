class Emp:
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel

    def startWork(self):
        print "RD with level %d start to work" % self.currentGrade

    def endWork(self):
        print "RD stop to work"


rd1 = RD()
rd1.startWork()
rd1.currentGrade = 7
rd1.startWork()
print rd1.currentGrade, rd1.gradeLevel
