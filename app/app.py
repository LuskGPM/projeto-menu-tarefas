import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "backend.api.server:server",
        reload=True,
        host='127.0.0.1',
        port=8000
    )
