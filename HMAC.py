class HmacGen:
    def __init__(self):
        pass

    def hmac(self, key, move):
        import hashlib
        str_key = str(key) + str(move)
        return hashlib.sha3_224(str_key.encode()).hexdigest().upper()
