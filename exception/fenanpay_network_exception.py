class FenanpayNetworkException(ConnectionError):
    def __init__(self, *args):
        # Ensure everything is assigned properly
        super().__init__("NetworkException", *args)

    def __str__(self):
        return f"{self.__class__.__name__}: NetworkException"
