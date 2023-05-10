class Response:
    def __init__(self, isSuccess: bool, message: str):
        self.IsSuccess = isSuccess
        self.message = message