import pandas as pd
from com.bridgelabz.censusanalyzer.CensusAnalyserCSVHeader import CensusAnalyserCSVHeader


class CensusAnalyser:
    def __init__(self):
        self.stateCensusData = None

    def loadStateCensusData(self, path, delimiter="\t"):
        """Loading State census data set"""
        header = repr(CensusAnalyserCSVHeader()).split(',')
        self.stateCensusData = pd.read_csv(path, sep=delimiter, skiprows=[0], names=header)

    def getStateCensusRecordCount(self):
        return len(self.stateCensusData)


if __name__ == '__main__':
    STATE_CENSUS_PATH = r"..\Resource\stateCensusData.csv"
    analyser = CensusAnalyser()
    analyser.loadStateCensusData(STATE_CENSUS_PATH)
    analyser.getStateCensusRecordCount()
