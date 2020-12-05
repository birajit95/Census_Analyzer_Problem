from com.bridgelabz.censusanalyzer.CensusAnalyser import CensusAnalyser
from com.bridgelabz.censusanalyzer.CensusAnalyserException import CensusAnalyserException
import pytest

STATE_CENSUS_ACTUAL_PATH = r"C:\Users\User\PycharmProjects\CensusAnalyserProblem\com\bridgelabz\Resource\stateCensusData.csv"
STATE_CENSUS_INCORRECT_TYPE_PATH = r"C:\Users\User\PycharmProjects\CensusAnalyserProblem\com\bridgelabz\Resource\stateCensusData.xls"
STATE_CODE_ACTUAL_PATH = r"C:\Users\User\PycharmProjects\CensusAnalyserProblem\com\bridgelabz\Resource\stateCodeData.csv"
STATE_CODE_INCORRECT_TYPE_PATH = r"C:\Users\User\PycharmProjects\CensusAnalyserProblem\com\bridgelabz\Resource\stateCodeData.xls"
WRONG_PATH = r"Problem\com\bridgelabz\Resource\stateCensusData.csv"
WRONG_HEADER = ["A", "B", "C", "D"]


@pytest.fixture
def stateCensusInstance():
    return CensusAnalyser()


def test_givenStateCensusCSVFile_WhenCounted_ShouldReturnRecordCount(stateCensusInstance):
    stateCensusInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH)
    assert stateCensusInstance.getStateCensusRecordCount() == 29


def test_givenStateCensusCSVFile_WhenWrongPath_ShouldRaiseCensusAnalyserException(stateCensusInstance):
    with pytest.raises(CensusAnalyserException):
        stateCensusInstance.loadStateCensusData(WRONG_PATH)


def test_givenStateCensusFile_WhenIncorrectFileType_ShouldRaiseCensusAnalyserException(stateCensusInstance):
    with pytest.raises(CensusAnalyserException):
        stateCensusInstance.loadStateCensusData(STATE_CENSUS_INCORRECT_TYPE_PATH)


def test_givenStateCensusCSVFile_WhenWrongDelimiter_ShouldRaiseCensusAnalyserException(stateCensusInstance):
    with pytest.raises(CensusAnalyserException):
        stateCensusInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH, delimiter=",")


def test_givenStateCensusCSVFile_WhenWrongHeaderFound_ShouldRaiseCensusAnalyserException(stateCensusInstance):
    with pytest.raises(CensusAnalyserException):
        stateCensusInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH, header=WRONG_HEADER)


def test_givenStateCodeCSVFile_WhenCounted_ShouldReturnRecordCount(stateCensusInstance):
    stateCensusInstance.loadStateCodeData(STATE_CODE_ACTUAL_PATH)
    assert stateCensusInstance.getStateCodeRecordCount() == 37


def test_givenStateCodeCSVFile_WhenWrongPath_ShouldRaiseCensusAnalyserException(stateCensusInstance):
    with pytest.raises(CensusAnalyserException):
        stateCensusInstance.loadStateCodeData(WRONG_PATH)


def test_givenStateCodeFile_WhenIncorrectFileType_ShouldRaiseCensusAnalyserException(stateCensusInstance):
    with pytest.raises(CensusAnalyserException):
        stateCensusInstance.loadStateCodeData(STATE_CODE_INCORRECT_TYPE_PATH)
