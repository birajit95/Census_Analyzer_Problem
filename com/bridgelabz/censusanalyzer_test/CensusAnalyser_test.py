from com.bridgelabz.censusanalyzer.CensusAnalyser import CensusAnalyser
from com.bridgelabz.censusanalyzer.CensusAnalyserException import CensusAnalyserException
import pytest
import json

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


# Test Cases for sorting are following


def test_givenStateCensusCSVFile_WhenSortedByStateName_ShouldReturn_ExactFirstStateName(censusAnalyserInstance):
    censusAnalyserInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH)
    assert list(json.loads(censusAnalyserInstance.sortCensusDataByStateName()))[0] == "Andhra Pradesh"


def test_givenStateCensusCSVFile_WhenSortedByStateName_ShouldReturn_ExactLastStateName(censusAnalyserInstance):
    censusAnalyserInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH)
    assert list(json.loads(censusAnalyserInstance.sortCensusDataByStateName()))[-1] == "West Bengal"


def test_givenStateCensusCSVFile_WhenSortedByStateName_FirstState_ShouldNot_BeAnaOtherThenExpectation(
        censusAnalyserInstance):
    censusAnalyserInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH)
    dataList = list(json.loads(censusAnalyserInstance.sortCensusDataByStateName()))
    for state in dataList:
        if state != "Andhra Pradesh":
            assert dataList[0] != state


def test_givenStateCensusCSVFile_WhenSortedByStateName_LastState_ShouldNot_BeAnaOtherThenExpectation(
        censusAnalyserInstance):
    censusAnalyserInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH)
    dataList = list(json.loads(censusAnalyserInstance.sortCensusDataByStateName()))
    for state in dataList:
        if state != "West Bengal":
            assert dataList[-1] != state


def test_givenStateCensusCSVFile_WhenSortedByStateCode_ShouldReturn_ExactFirstStateCode(censusAnalyserInstance):
    censusAnalyserInstance.loadStateCodeData(STATE_CODE_ACTUAL_PATH)
    assert list(json.loads(censusAnalyserInstance.sortCensusDataByStateCode()).values())[0]["State Code"] == "AD"


def test_givenStateCensusCSVFile_WhenSortedByStateCode_ShouldReturn_ExactLastStateCode(censusAnalyserInstance):
    censusAnalyserInstance.loadStateCodeData(STATE_CODE_ACTUAL_PATH)
    assert list(json.loads(censusAnalyserInstance.sortCensusDataByStateCode()).values())[-1]["State Code"] == "WB"


def test_givenStateCensusCSVFile_WhenSortedByStateCode_FirstStateCode_ShouldNot_BeAnaOtherThenExpectation(
        censusAnalyserInstance):
    censusAnalyserInstance.loadStateCodeData(STATE_CODE_ACTUAL_PATH)
    dataList = list(json.loads(censusAnalyserInstance.sortCensusDataByStateCode()).values())
    for state in dataList:
        if state["State Code"] != "AD":
            assert dataList[0]["State Code"] != state["State Code"]


def test_givenStateCensusCSVFile_WhenSortedByStateCode_LastStateCode_ShouldNot_BeAnaOtherThenExpectation(
        censusAnalyserInstance):
    censusAnalyserInstance.loadStateCodeData(STATE_CODE_ACTUAL_PATH)
    dataList = list(json.loads(censusAnalyserInstance.sortCensusDataByStateCode()).values())
    for state in dataList:
        if state["State Code"] != "WB":
            assert dataList[-1]["State Code"] != state["State Code"]
