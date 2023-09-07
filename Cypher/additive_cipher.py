import random

class AdditiveCipher:
    def __init__(self) -> None:
        pass
    
    def cipher(self, input: str, key = random.randint(0, 25)):
        output = ""
        for c in input:
            output += chr(ord(c) + key)
        return output