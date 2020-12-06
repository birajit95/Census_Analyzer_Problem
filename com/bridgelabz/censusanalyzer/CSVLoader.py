import pandas as pd
from com.bridgelabz.censusanalyzer.CensusAnalyserCSVHeader import StateCensusCSVHeader, StateCodeCSVHeader
from com.bridgelabz.censusanalyzer.CensusAnalyserException import CensusAnalyserException
from com.bridgelabz.censusanalyzer.CensusAnalyserException import ExceptionType
from com.bridgelabz.censusanalyzer.CSVBuilder import CSVBuilder


class CSVLoader(CSVBuilder):

    @staticmethod
    def genericCSVLoader(path, fileName, delimiter="\t", header=None):
        """This generic loader function can load both the data set and raise exceptions if found any error"""

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
