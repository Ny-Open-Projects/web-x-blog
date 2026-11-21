try:
    from pydantic import BaseModel, ConfigDict, Field
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_name: str = Field(alias="userName")
    created_at: int = Field(validation_alias="createdAt", serialization_alias="createdAt", ge=0)

raw = {"userName": "alice", "createdAt": 1700000000}
u = User(**raw)                        # 外部命名解析
print(u.user_name)
print(u.model_dump(by_alias=True))     # 对外 camelCase
print(User(user_name="bob", created_at=1).user_name)  # 内部名也能构造
