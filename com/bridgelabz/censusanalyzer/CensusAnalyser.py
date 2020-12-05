import pandas as pd
from com.bridgelabz.censusanalyzer.CensusAnalyserCSVHeader import CensusAnalyserCSVHeader
from com.bridgelabz.censusanalyzer.CensusAnalyserException import CensusAnalyserException
from com.bridgelabz.censusanalyzer.CensusAnalyserException import ExceptionType


class CensusAnalyser:
    def __init__(self):
        self.stateCensusData = None

    def loadStateCensusData(self, path, delimiter="\t"):
        """This function loads state census data and raise exceptions if found any error"""

        header = repr(CensusAnalyserCSVHeader()).split(',')

        if not path.find(".csv"):
            raise CensusAnalyserException(ExceptionType.INCORRECT_FILE_TYPE_EXCEPTION.value)
        if delimiter == ',':
            raise CensusAnalyserException(ExceptionType.INCORRECT_DELIMITER_EXCEPTION.value)
        try:
            self.stateCensusData = pd.read_csv(path, sep=delimiter, skiprows=[0], names=header)
        except FileNotFoundError:
            raise CensusAnalyserException(ExceptionType.WRONG_FILE_PATH_EXCEPTION.value)

    def getStateCensusRecordCount(self):
        """returns length of the data set"""
        return len(self.stateCensusData)


if __name__ == '__main__':
    STATE_CENSUS_PATH = r"..\Resource\stateCensusData.csv"
    analyser = CensusAnalyser()
    analyser.loadStateCensusData(STATE_CENSUS_PATH)
    # analyser.getStateCensusRecordCount()
