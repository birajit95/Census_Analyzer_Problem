from com.bridgelabz.censusanalyzer.CSVLoader import CSVLoader
import json

class CensusAnalyser:
    def __init__(self):
        self.stateCensusData = None
        self.stateCodeData = None

    def loadStateCensusData(self, path, delimiter="\t", header=None):
        """This function loads state census data and raise exceptions if found any error"""
        self.stateCensusData = CSVLoader.genericCSVLoader(path, "StateCensusCSV", delimiter=delimiter, header=header)

    def getStateCensusRecordCount(self):
        """returns length of the data set"""
        return len(self.stateCensusData)

    def loadStateCodeData(self, path, delimiter="\t", header=None):
        """This function loads State code data set and can raise exception if any error found"""
        self.stateCodeData = CSVLoader.genericCSVLoader(path, "StateCodeCSV", delimiter=delimiter, header=header)

    def getStateCodeRecordCount(self):
        """returns length of the data set"""
        return len(self.stateCodeData)

    def sortCensusDataByStateName(self):
        sortedData = self.stateCensusData.sort_values(by="State")
        dataDict = {}
        for i in range(0, len(sortedData)):
            data = dict(sortedData.iloc(0)[i])
            dataDict[(sortedData.iloc(0)[i])["State"]] = {"Population": int(data["Population"]),
                                                          "Density": int(data["Density"]), "Area": int(data["Area"])}
        return json.dumps(dataDict)

    def sortCensusDataByStateCode(self):
        sortedData = self.stateCodeData.sort_values(by="StateCode")
        dataDict = {}
        for i in range(0, len(sortedData)):
            data = dict(sortedData.iloc(0)[i])
            dataDict[(sortedData.iloc(0)[i])["State"]] = {"State Code": data["StateCode"], "TIN": int(data["TIN"])}
        return json.dumps(dataDict)


if __name__ == '__main__':
    STATE_CENSUS_PATH = r"..\Resource\stateCensusData.csv"
    STATE_CODE_PATH = r"..\Resource\stateCodeData.csv"
    analyser = CensusAnalyser()
    analyser.loadStateCensusData(STATE_CENSUS_PATH)
    analyser.loadStateCodeData(STATE_CODE_PATH)
    print(analyser.getStateCensusRecordCount())
    print(analyser.getStateCodeRecordCount())
    print(analyser.sortCensusDataByStateCode())
