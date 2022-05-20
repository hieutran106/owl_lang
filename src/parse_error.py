class ParseError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)



if __name__ == "__main__":
    error = ParseError("abcd")
    print(error)