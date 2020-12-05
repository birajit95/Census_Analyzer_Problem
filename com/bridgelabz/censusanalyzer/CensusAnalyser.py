import pandas as pd
from com.bridgelabz.censusanalyzer.CensusAnalyserCSVHeader import StateCensusCSVHeader, StateCodeCSVHeader
from com.bridgelabz.censusanalyzer.CensusAnalyserException import CensusAnalyserException
from com.bridgelabz.censusanalyzer.CensusAnalyserException import ExceptionType


class CensusAnalyser:
    def __init__(self):
        self.stateCensusData = None
        self.stateCodeData = None

    def genericCSVLoader(self, path, fileName, delimiter="\t", header=None):
        """This generic loader function loads both the data set and raise exceptions if found any error"""
        
        if fileName == "StateCodeCSV":
            if header is None:
                header = repr(StateCodeCSVHeader()).split(',')
            elif header != repr(StateCodeCSVHeader()).split(','):
                raise CensusAnalyserException(ExceptionType.INCORRECT_HEADER_EXCEPTION.value)
        else:
            if header is None:
                header = repr(StateCensusCSVHeader()).split(',')
            elif header != repr(StateCensusCSVHeader()).split(','):
                raise CensusAnalyserException(ExceptionType.INCORRECT_HEADER_EXCEPTION.value)

        if not path.find(".csv"):
            raise CensusAnalyserException(ExceptionType.INCORRECT_FILE_TYPE_EXCEPTION.value)

        if delimiter != "\t":
            raise CensusAnalyserException(ExceptionType.INCORRECT_DELIMITER_EXCEPTION.value)

        try:
            return pd.read_csv(path, sep=delimiter, skiprows=[0], names=header)
        except FileNotFoundError:
            raise CensusAnalyserException(ExceptionType.WRONG_FILE_PATH_EXCEPTION.value)

    def loadStateCensusData(self, path, delimiter="\t", header=None):
        """This function loads state census data and raise exceptions if found any error"""
        self.stateCensusData = self.genericCSVLoader(path, "StateCensusCSV", delimiter=delimiter, header=header)

    def getStateCensusRecordCount(self):
        """returns length of the data set"""
        return len(self.stateCensusData)

    def loadStateCodeData(self, path, delimiter="\t", header=None):
        """This function loads State code data set and can raise exception if any error found"""
        self.stateCodeData = self.genericCSVLoader(path, "StateCodeCSV", delimiter=delimiter, header=header)

    def getStateCodeRecordCount(self):
        """returns length of the data set"""
        return len(self.stateCodeData)


if __name__ == '__main__':
    STATE_CENSUS_PATH = r"..\Resource\stateCensusData.csv"
    STATE_CODE_PATH = r"..\Resource\stateCodeData.csv"
    analyser = CensusAnalyser()
    analyser.loadStateCensusData(STATE_CENSUS_PATH)
    analyser.loadStateCodeData(STATE_CODE_PATH)
    print(analyser.getStateCensusRecordCount())
    print(analyser.getStateCodeRecordCount())
