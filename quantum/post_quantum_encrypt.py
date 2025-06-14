from pqcrypto.sign.dilithium2 import generate_keypair, sign, verify

class QuantumVault:
    def __init__(self):
        self.public_key, self.private_key = generate_keypair()

    def encrypt_data(self, data: bytes) -> bytes:
        signature = sign(self.private_key, data)
        return signature + data

    def verify_data(self, payload: bytes) -> bool:
        sig, data = payload[:64], payload[64:]
        return verify(self.public_key, data, sig)
