import os
import time
from fastapi import FastAPI

app = FastAPI()

# Read environment variables
MODE = os.getenv("MODE", "helloworld")
MY_SECRET = os.getenv("MY_SECRET", "SECRET_NOT_FOUND")
VOLUME_PATH = "/mnt/data"
FILE_NAME = "test.txt"
FILE_PATH = os.path.join(VOLUME_PATH, FILE_NAME)

# Service 1 — Print Secret
if MODE == "print-secret":
    print("Secret value:", MY_SECRET)
    time.sleep(3600)

# Service 2 — Write File to Volume
elif MODE == "write-volume":
    os.makedirs(VOLUME_PATH, exist_ok=True)
    with open(FILE_PATH, "w") as f:
        f.write("Hello from persistent volume!")
    print("File created in volume:", FILE_PATH)
    with open(FILE_PATH) as f:
        print(f.read())
    time.sleep(3600)

# Service 3 — Read File from Volume
elif MODE == "read-volume":
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH) as f:
            print("File contents:", f.read())
    else:
        print("File not found in volume!")
    time.sleep(3600)

# Service 4 — HTTP Endpoint
elif MODE == "helloworld":
    print("Secret value on startup:", MY_SECRET)

    @app.get("/")
    def hello():
        return {"message": "Hello World"}

    @app.get("/secret")
    def get_secret():
        return {"secret": MY_SECRET}

else:
    print(f"Unknown MODE: {MODE}")
