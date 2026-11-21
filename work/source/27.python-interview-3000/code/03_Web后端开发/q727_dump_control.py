try:
    from pydantic import BaseModel
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Addr(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    password: str
    addr: Addr

u = User(name="a", password="secret", addr={"city": "BJ", "zip_code": "100000"})
print(u.model_dump(exclude={"password"}))
print(u.model_dump(include={"name", "addr"}, exclude={"addr": {"zip_code"}}))
print(u.model_dump_json())
