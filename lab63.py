class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.member * self.day

    @staticmethod
    def calculate(x, y):
        return x * y

    @classmethod
    def get_member(cls):
        return cls.member


myTeam1 = Team()
print "all working hour", myTeam1.all_working_hour()
print "working hour?", myTeam1.working_hour()
print myTeam1.calculate(5, 7), Team.calculate(6, 8)
print Team.get_member(), myTeam1.get_member()
