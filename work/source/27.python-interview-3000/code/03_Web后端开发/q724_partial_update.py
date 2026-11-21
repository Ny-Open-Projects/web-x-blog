try:
    from pydantic import BaseModel
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class UserPatch(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None

stored = {"name": "alice", "email": "a@x.com", "age": 30}

def apply_patch(stored: dict, patch: UserPatch) -> dict:
    for k, v in patch.model_dump(exclude_unset=True).items():
        stored[k] = v
    return stored

print(apply_patch(dict(stored), UserPatch(name="bob")))   # 只改 name
print(apply_patch(dict(stored), UserPatch(email=None)))   # 显式 None 才清空
