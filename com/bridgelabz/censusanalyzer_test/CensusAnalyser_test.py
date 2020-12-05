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
def censusAnalyserInstance():
    return CensusAnalyser()


def test_givenStateCensusCSVFile_WhenCounted_ShouldReturnRecordCount(censusAnalyserInstance):
    censusAnalyserInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH)
    assert censusAnalyserInstance.getStateCensusRecordCount() == 29


@pytest.mark.parametrize("filePath,delimiter,header, expected", [
    (WRONG_PATH, "\t", None, CensusAnalyserException),
    (STATE_CENSUS_INCORRECT_TYPE_PATH, "\t", None, CensusAnalyserException),
    (STATE_CENSUS_ACTUAL_PATH, ",", None, CensusAnalyserException),
    (STATE_CENSUS_ACTUAL_PATH, "\t", WRONG_HEADER, CensusAnalyserException),

])
def test_StateCensusCSVFile_WhenGiven_CSVLoader_ShouldMeetExpectation(censusAnalyserInstance, filePath, delimiter,
                                                                      header, expected):
    with pytest.raises(expected):
        censusAnalyserInstance.loadStateCensusData(path=filePath, delimiter=delimiter, header=header)


def test_givenStateCodeCSVFile_WhenCounted_ShouldReturnRecordCount(censusAnalyserInstance):
    censusAnalyserInstance.loadStateCodeData(STATE_CODE_ACTUAL_PATH)
    assert censusAnalyserInstance.getStateCodeRecordCount() == 37


@pytest.mark.parametrize("filePath,delimiter,header, expected", [
    (WRONG_PATH, "\t", None, CensusAnalyserException),
    (STATE_CODE_INCORRECT_TYPE_PATH, "\t", None, CensusAnalyserException),
    (STATE_CODE_ACTUAL_PATH, ",", None, CensusAnalyserException),
    (STATE_CODE_ACTUAL_PATH, "\t", WRONG_HEADER, CensusAnalyserException),

])
def test_StateCodeCSVFile_WhenGiven_CSVLoader_ShouldMeetExpectation(censusAnalyserInstance, filePath, delimiter, header,
                                                                    expected):
    with pytest.raises(expected):
        censusAnalyserInstance.loadStateCensusData(path=filePath, delimiter=delimiter, header=header)
