class CensusAnalyserCSVHeader:
    def __init__(self):
        self.state = "State"
        self.population = "Population"
        self.area = "Area"
        self.density = "Density"

    def __repr__(self):
        return f"{self.state},{self.population},{self.area},{self.density}"
