try:
    from pydantic import BaseModel, ConfigDict
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)
    name: str

class FromAttr(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    uid: int

class Obj:
    uid = 9

s = Strict(name="  alice ")
print(repr(s.name))
try:
    Strict(name="x", extra_field=1)
except Exception as e:
    print("多余字段被拒:", type(e).__name__)
print(FromAttr.model_validate(Obj()).uid)
