class ParseError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)




class OwlRuntimeError(Exception):
    def __init__(self, token, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.token = token


if __name__ == "__main__":
    error = ParseError("abcd")
    print(error)