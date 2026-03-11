class CepNotFoundException(Exception):
    def __init__(self):
        super().__init__("CEP not found")