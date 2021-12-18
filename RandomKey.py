class RandomKey:
    def __init__(self):
        pass

    def keygen(self):
        import hashlib
        from random import SystemRandom
        key = SystemRandom()
        return hashlib.sha3_224(str(key.random()).encode()).hexdigest().upper()
