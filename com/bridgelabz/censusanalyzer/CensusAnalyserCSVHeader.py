class StateCensusCSVHeader:
    def __init__(self):
        self.state = "State"
        self.population = "Population"
        self.area = "Area"
        self.density = "Density"

    def __repr__(self):
        return f"{self.state},{self.population},{self.area},{self.density}"


class StateCodeCSVHeader:
    def __init__(self):
        self.serialNo = "SerialNo"
        self.state = "State"
        self.tin = "TIN"
        self.stateCode = "StateCode"

    def __repr__(self):
        return f"{self.serialNo},{self.state},{self.tin},{self.stateCode}"
