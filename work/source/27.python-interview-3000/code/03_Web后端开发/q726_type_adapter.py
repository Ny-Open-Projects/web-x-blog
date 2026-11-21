try:
    from pydantic import RootModel, TypeAdapter, ValidationError
except ImportError:
    print("pip install pydantic v2 后再运行")
    raise SystemExit(0)

adapter = TypeAdapter(dict[str, int])
print(adapter.validate_python({"a": "1"}))
print(adapter.dump_python({"b": 2}))

class Tags(RootModel[list[str]]):
    pass

print(Tags.model_validate(["x", "y"]).root)
try:
    TypeAdapter(list[int]).validate_python(["1", "a"])
except ValidationError as e:
    print("错误条数:", e.error_count())
