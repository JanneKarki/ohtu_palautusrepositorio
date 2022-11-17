class Player:
    def __init__(self, name, team, goals, assists, nationality, points):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.points = points
    
    def __str__(self):
        string = (f"{self.name:20}" +
                    " " +
                    f"{self.team:5}" +
                    " " +
                    f"{str(self.goals):2}" +
                    " + " +
                    f"{str(self.assists):2}"+
                    " = " +
                    str(self.points)
                    )

        return string
