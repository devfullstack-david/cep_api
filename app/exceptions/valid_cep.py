class ValidCepException(Exception):
    def __init__(self):
        super().__init__("CEP isn't valid format")
