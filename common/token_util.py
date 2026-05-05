class TokenUtil:
    _token = None

    @classmethod
    def set_token(cls, token):
        cls._token = token

    @classmethod
    def get_token(cls):
        return cls._token