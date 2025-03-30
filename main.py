import uvicorn
from src.app import app


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, forwarded_allow_ips="*")
