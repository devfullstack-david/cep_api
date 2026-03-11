class MissingKeyEnvException(Exception):
    def __init__(self, key: str):
        self._key = key
        self._message = f"Missing {key} in .env file"
        super().__init__(self._message)