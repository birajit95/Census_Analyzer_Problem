import enum


class ExceptionType(enum.Enum):
    WRONG_FILE_PATH_EXCEPTION = "Wrong file path has been given!"
    INCORRECT_FILE_TYPE_EXCEPTION = "Incorrect file type is found!"
    INCORRECT_DELIMITER_EXCEPTION = "Incorrect delimiter is found!"
    INCORRECT_HEADER_EXCEPTION = "Incorrect Header is found!"


class CensusAnalyserException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

