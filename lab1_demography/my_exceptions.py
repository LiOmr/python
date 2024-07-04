import os


class CustomCSVException(Exception):
    pass


class InvalidHeaderError(CustomCSVException):
    def __init__(self, message):
        super().__init__(message)


class EmptyFileError(CustomCSVException):
    def __init__(self, message):
        super().__init__(message)


class WrongRegion(CustomCSVException):
    def __init__(self, message):
        super().__init__(message)


class InvalidFileExtensionError(CustomCSVException):
    def __init__(self, message):
        super().__init__(message)


class InvalidDataError(CustomCSVException):
    def __init__(self, message):
        super().__init__(message)


class FileNotFound(CustomCSVException):
    def __init__(self, message):
        super().__init__(message)
