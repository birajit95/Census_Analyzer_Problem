from com.bridgelabz.censusanalyzer.CensusAnalyser import CensusAnalyser
import pytest

STATE_CENSUS_ACTUAL_PATH = r"C:\Users\User\PycharmProjects\CensusAnalyserProblem\com\bridgelabz\Resource\stateCensusData.csv"


@pytest.fixture
def stateCensusInstance():
    return CensusAnalyser()


def test_givenStateCensusCSVFile_WhenCounted_ShouldReturnRecordCount(stateCensusInstance):
    stateCensusInstance.loadStateCensusData(STATE_CENSUS_ACTUAL_PATH)
    assert stateCensusInstance.getStateCensusRecordCount() == 29
