import pandas as pd


class CensusAnalyser:
    def __init__(self):
        self.stateCensusData = None

    def loadStateCensusData(self, path, delimiter="\t"):
        """Loading State census data set"""
        self.stateCensusData = pd.read_csv(path, sep=delimiter, skiprows=[0])


if __name__ == '__main__':
    STATE_CENSUS_PATH = r"..\Resource\stateCensusData.csv"
    analyser = CensusAnalyser()
    analyser.loadStateCensusData(STATE_CENSUS_PATH)
