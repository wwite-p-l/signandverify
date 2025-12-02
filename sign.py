import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

if len(sys.argv)<3:
    print(" pass 2 arguments privatekey.pem message")
    sys.exit()


privatefile = sys.argv[1]
msg = sys.argv[2]
message = msg.encode() # Message must be bytes
print(message)
with open(privatefile, "rb") as f:
    private_key_pem = f.read()
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None,  # No password if the key is unencrypted
        backend=default_backend()
    )
# Sign the message
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Signature")
print(signature.hex())