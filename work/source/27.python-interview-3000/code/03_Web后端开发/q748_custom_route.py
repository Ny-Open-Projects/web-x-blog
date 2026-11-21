try:
    from fastapi import APIRouter, FastAPI, Request, Response
    from fastapi.routing import APIRoute
    from fastapi.testclient import TestClient
except ImportError:
    print("pip install fastapi httpx 后再运行")
    raise SystemExit(0)

class SignedRoute(APIRoute):
    def get_route_handler(self):
        original = super().get_route_handler()

        async def custom_handler(request: Request) -> Response:
            if request.headers.get("x-signature") != "secret":
                return Response("bad signature", status_code=401)
            return await original(request)

        return custom_handler

app = FastAPI()
router = APIRouter(route_class=SignedRoute)

@router.get("/data")
def data():
    return {"ok": True}

app.include_router(router)

client = TestClient(app)
print(client.get("/data").status_code)
print(client.get("/data", headers={"x-signature": "secret"}).json())
