from google_auth_oauthlib.flow import InstalledAppFlow
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

# Get a unique hardware ID (CPU serial number)
def get_cpu_id():
    result = os.popen("wmic cpu get ProcessorId").read().split("\n")
    return result[1].strip() if len(result) > 1 else "UNKNOWN_CPU"

# Hash token + hardware for security
def secure_token_hash(token):
    h = hashes.Hash(hashes.SHA3_512(), backend=default_backend())
    h.update((token + get_cpu_id()).encode())
    return h.finalize().hex()

# Launch OAuth flow and return secure token
def get_gmail_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        scopes=["https://mail.google.com/"]
    )
    creds = flow.run_local_server(port=0)
    token_hash = secure_token_hash(creds.token)
    print("🔐 Secure Token Hash:", token_hash)
    print("✅ Granted Scopes:", creds.scopes)
    return token_hash, creds

if __name__ == "__main__":
    get_gmail_token()
