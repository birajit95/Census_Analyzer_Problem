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

    def sortCensusDataByGivenColumn(self, columnName, ascending=True):
        """This is a generic sorting function which sort the data based on given column and return in json fromat"""
        sortedData = self.stateCensusData.sort_values(by=columnName, ascending=ascending)
        dataDict = {}
        for i in range(0, len(sortedData)):
            data = dict(sortedData.iloc(0)[i])
            dataDict[(sortedData.iloc(0)[i])["State"]] = {"Population": int(data["Population"]),
                                                          "Density": int(data["Density"]), "Area": int(data["Area"])}
        return json.dumps(dataDict)

    def sortCensusDataByStateName(self):
        """Returns census data in json format sorted by State Name"""
        return self.sortCensusDataByGivenColumn(columnName="State")

    def sortCensusDataByPopulation(self):
        """Returns census data in json format sorted by Population in reverse order"""
        return self.sortCensusDataByGivenColumn(columnName="Population", ascending=False)

    def sortCensusDataByStateCode(self):
        """Return State code census data in json format sorted by state code"""
        sortedData = self.stateCodeData.sort_values(by="StateCode")
        dataDict = {}
        for i in range(0, len(sortedData)):
            data = dict(sortedData.iloc(0)[i])
            dataDict[(sortedData.iloc(0)[i])["State"]] = {"State Code": data["StateCode"], "TIN": int(data["TIN"])}
        return json.dumps(dataDict)


# if __name__ == '__main__':
#     STATE_CENSUS_PATH = r"..\Resource\stateCensusData.csv"
#     STATE_CODE_PATH = r"..\Resource\stateCodeData.csv"
#     analyser = CensusAnalyser()
#     analyser.loadStateCensusData(STATE_CENSUS_PATH)
#     analyser.loadStateCodeData(STATE_CODE_PATH)
#     # print(analyser.getStateCensusRecordCount())
#     # print(analyser.getStateCodeRecordCount())
#     print(analyser.sortCensusDataByPopulation())
