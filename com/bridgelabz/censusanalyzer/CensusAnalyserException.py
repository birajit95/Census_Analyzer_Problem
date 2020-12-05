import enum


class ExceptionType(enum.Enum):
    WRONG_FILE_PATH_EXCEPTION = "Wrong file path has been given!"


class CensusAnalyserException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

