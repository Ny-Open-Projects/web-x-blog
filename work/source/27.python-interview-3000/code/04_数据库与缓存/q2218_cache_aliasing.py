"""本地缓存的可变对象陷阱: 缓存的是引用, 改对象就是改缓存"""
import copy
import json

l1 = {}
l2 = {}   # 模拟远端: 存 JSON 字符串

def set_user(uid, user):
    l2[uid] = json.dumps(user)      # 远端序列化成字节, 天然快照
    l1[uid] = user                  # 本地直接存引用 -> 埋雷

set_user("u1", {"name": "a", "tags": ["vip"]})
got = l1["u1"]
got["tags"].append("black")
print("业务改过返回值后本地缓存:", l1["u1"], " <- 已被污染")
print("远端仍是              :", json.loads(l2["u1"]))
print("下一个读者拿到的      :", l1["u1"])

def get_user_local_safe(uid):
    v = l1.get(uid)
    return copy.deepcopy(v) if v is not None else None

set_user("u1", {"name": "a", "tags": ["vip"]})
got = get_user_local_safe("u1")
got["tags"].append("black")
print("深拷贝命中后缓存完好  :", l1["u1"])
print("纪律: L1 只放不可变结构, 或命中即拷贝, 引用共享必须写进工具的契约")
