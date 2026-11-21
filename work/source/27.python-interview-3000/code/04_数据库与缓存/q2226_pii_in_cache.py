"""缓存中的 PII: 键哈希化 值脱敏与按需清除"""
import hashlib

def pii_key(*parts):
    raw = "|".join(parts)
    return "u:" + hashlib.sha256(raw.encode()).hexdigest()[:16]

k1 = pii_key("13800138000")
k2 = pii_key("13800138000")
k3 = pii_key("13900139000")
print("同主体同键:", k1 == k2, " 不同主体不同键:", k1 != k3)
print("键不含明文手机号:", k1)

def mask(value):
    if isinstance(value, str) and len(value) == 11 and value.isdigit():
        return value[:3] + "****" + value[-4:]
    if isinstance(value, dict):
        return {kk: mask(vv) for kk, vv in value.items()}
    return value

profile = {"phone": "13800138000", "name": "王五", "level": 3}
print("入库前脱敏:", mask(profile))

store = {k1: mask(profile)}
def erase(phone):
    k = pii_key(phone)
    if k in store:
        del store[k]
        return True
    return False

print("删除前键数:", len(store), " 按手机号行使删除权:", erase("13800138000"),
      " 删除后键数:", len(store))
print("三件事: 键哈希化 值脱敏 删除可按主体重算键定位")
