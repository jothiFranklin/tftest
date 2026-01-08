import os
from fastapi import FastAPI

app = FastAPI()

SECRET = os.getenv("MY_SECRET", "SECRET_NOT_FOUND")
VOLUME_PATH = "/mnt/data"
FILE_PATH = f"{VOLUME_PATH}/data.txt"

@app.get("/")
def hello():
    return {"message": "Hello World"}

def print_secret():
    print("Secret value:", SECRET)

def write_volume():
    os.makedirs(VOLUME_PATH, exist_ok=True)
    with open(FILE_PATH, "w") as f:
        f.write("Hello from volume")
    print("Written file to volume")

def read_volume():
    try:
        with open(FILE_PATH, "r") as f:
            print("File content:", f.read())
    except Exception as e:
        print("Error reading file:", e)

if __name__ == "__main__":
    MODE = os.getenv("MODE", "api")

    if MODE == "print-secret":
        print_secret()

    elif MODE == "write-volume":
        write_volume()

    elif MODE == "read-volume":
        read_volume()

    else:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
