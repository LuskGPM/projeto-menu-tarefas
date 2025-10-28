from fastapi import FastAPI
import uvicorn

server = FastAPI()

if __name__ == '__main__':
    uvicorn.run(server)