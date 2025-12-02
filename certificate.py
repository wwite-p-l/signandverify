from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.x509.oid import NameOID
import sys
import datetime

import certificateconfig

def generateSelfSignedCertificateFromKeys(privatefile,certificatefile):
    with open(privatefile, "rb") as f:
        private_key_pem = f.read()
        private_key = serialization.load_pem_private_key(
            private_key_pem,
            password=None,  # No password if the key is unencrypted
            backend=default_backend()
        )

    # Create a self-signed certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, certificateconfig.COUNTRY),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, certificateconfig.STATE),
        x509.NameAttribute(NameOID.LOCALITY_NAME, certificateconfig.CITY),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, certificateconfig.ORGANISATION),
        x509.NameAttribute(NameOID.COMMON_NAME, certificateconfig.DOMAIN),
    ])

    certificate = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.now(datetime.UTC) 
    ).not_valid_after(
        datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=365)#datetime.datetime.utcnow() + datetime.timedelta(days=365) # Valid for 1 year
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(ALTERNATENAME)]),
        critical=False,
    ).sign(private_key, hashes.SHA256(), default_backend())

    # Save the certificate to a file
    with open(certificatefile, "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

    print("Self-signed certificate generated and saved.")

def generatePublicPrivateKey(public,private):
    # Generate a new RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,  # Recommended key size
        backend=default_backend()
    )

  
    public_key = private_key.public_key()

  
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()  # Use NoEncryption for unencrypted key
    )

 
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save keys to files
    with open(private, "wb") as f:
        f.write(pem_private_key)

    with open(public, "wb") as f:
        f.write(pem_public_key)

    print("Private and public keys generated and saved.")


if len(sys.argv) < 4:
    print(" pass 3 arguments publickeyfile.pem privatekeyfile.pem certificatefile.pem")
    sys.exit()

public = sys.argv[1]
private = sys.argv[2]
certificate = sys.argv[3]

generatePublicPrivateKey(public,private)
generateSelfSignedCertificateFromKeys(private,certificate)