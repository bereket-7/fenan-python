class FenanpayUnauthorizedException(Exception):
    def __init__(self, message, *args):
        self.msg = message
        # Ensure everything is assigned properly
        super().__init__(message, *args)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.msg}"
