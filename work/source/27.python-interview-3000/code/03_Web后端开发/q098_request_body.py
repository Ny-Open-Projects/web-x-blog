try:
    from fastapi import FastAPI
    from pydantic import BaseModel, EmailStr
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

class Address(BaseModel):
    city: str
    street: str

class UserIn(BaseModel):
    name: str
    email: EmailStr
    age: int | None = None
    address: Address          # 嵌套模型

class UserOut(BaseModel):     # 响应模型:过滤敏感字段
    name: str
    city: str

@app.post('/users', response_model=UserOut)
def create_user(user: UserIn):
    return {'name': user.name, 'city': user.address.city, 'email': user.email}
