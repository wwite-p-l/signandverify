
import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
 
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend

if len(sys.argv)<4:
    print(" pass 3 arguments publickeyfile.pem message signature")
    sys.exit()
publickey = sys.argv[1]
msg = sys.argv[2]
message = msg.encode() # 
sign = sys.argv[3]
signature = bytes.fromhex(sign)
with open(publickey, "rb") as f:
    p_k_pem = f.read()
    public_key = load_pem_public_key(
        p_k_pem,
        backend=default_backend()
    )
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid. Message is authentic.")
except Exception as e:
    print(f"Signature is invalid: {e}. Message is not authentic.")