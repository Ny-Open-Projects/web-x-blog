try:
    from fastapi import FastAPI, Request
    from fastapi.exceptions import RequestValidationError
    from fastapi.responses import JSONResponse
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

app = FastAPI()

@app.get("/items")
def items(price: int):
    return {"code": "OK", "data": {"price": price}}

@app.exception_handler(RequestValidationError)
async def on_validate(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={
        "code": "VALIDATION_ERROR",
        "detail": exc.errors()[:3],
    })

client = TestClient(app)
print(client.get("/items?price=5").json())
print(client.get("/items?price=abc").status_code)
