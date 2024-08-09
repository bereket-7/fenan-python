class FenanpayAPIResponse:
    def __init__(self, status, message, content):
        self.status = status
        self.message = message
        self.content = content

    @staticmethod
    def from_json(json_data):
        return FenanpayAPIResponse(
            status=json_data["status"],
            message=json_data["message"],
            content=json_data["content"]
        )
