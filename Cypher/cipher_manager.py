from cipher_types import CipherType
from additive_cipher import AdditiveCipher

class CypherManager:
    def __init__(self, cipher_type : CipherType):
        match cipher_type:
            case CipherType.ADDITIVE_CIPHER:
                self.cipher_object = AdditiveCipher()
            
    def cipher(self, input: str, key = None):
        return self.cipher_object.cipher(input, key)