"""缓存值结构演进: 滚动发布期新旧代码共存要互相容忍"""
import json

def pack_v2(user):
    """新代码写入: 带版本字段与新增 level"""
    return json.dumps({"v": 2, "name": user["name"], "level": user.get("level", 1)})

def pack_v1(user):
    """旧代码写入: 不认识 level"""
    return json.dumps({"name": user["name"]})

def read_tolerant(raw):
    obj = json.loads(raw)
    return {
        "name": obj["name"],
        "level": obj.get("level", 1),
        "unknown_keys": [k for k in obj if k not in ("v", "name", "level")],
        "src_version": obj.get("v", 1),
    }

print("新代码读旧值:", read_tolerant(pack_v1({"name": "a"})))
print("新代码读新值:", read_tolerant(pack_v2({"name": "b", "level": 5})))
print("旧代码读新值: 取认识的 name ->", json.loads(pack_v2({"name": "b", "level": 5}))["name"])
print("纪律: 只增不改 读端给默认 写端带版本 语义变化时改名再失效")
