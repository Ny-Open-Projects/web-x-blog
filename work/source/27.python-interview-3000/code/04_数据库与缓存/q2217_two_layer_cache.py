"""双层缓存: 本地 L1 与远端 L2 的一致性窗口"""
from collections import OrderedDict

def new_l1(ttl):
    return {"ttl": ttl, "data": OrderedDict()}

def l1_get(l1, key, now):
    item = l1["data"].get(key)
    if item is None:
        return None
    value, expire = item
    if now > expire:
        del l1["data"][key]
        return None
    l1["data"].move_to_end(key)
    return value

def l1_put(l1, key, value, now):
    l1["data"][key] = (value, now + l1["ttl"])

l2 = {}
inbox = []              # 发往实例 B 的失效广播队列
DELAY = 2               # 广播延迟 2 tick
a, b = new_l1(10), new_l1(10)

l2["u1"] = "v1"
l1_put(a, "u1", "v1", 0)
inbox.append(0 + DELAY)
v = l1_get(b, "u1", 1)
if v is None:
    v = l2["u1"]
    l1_put(b, "u1", v, 1)
print("t1  B 回源读到 %s 并写入 L1" % v)

l2["u1"] = "v2"
inbox.append(2 + DELAY)
l1_put(a, "u1", "v2", 2)
print("t2  A 写入 v2, B 的 L1 仍是旧值")
print("t2  B 读到 %s  <- 广播未到, 双层不一致窗口" % l1_get(b, "u1", 2))

while inbox and inbox[0] <= 4:
    inbox.pop(0)
b["data"].pop("u1", None)
print("t4  广播送达, B 失效后读到 %s  <- 重新一致" % l2["u1"])
print("窗口上限 = 广播最坏延迟, L1 的 TTL 必须显著小于它, 作为投递失败时的自愈兜底")
