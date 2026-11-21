"""幂等键约定:校验、作用域与同键不同体的冲突判定(纯标准库)。"""
import hashlib
import uuid

MAX_KEY_LEN = 255


def check_key(route, tenant, key):
    """校验幂等键约定,返回 (ok, http_status, scope)。"""
    if not key:
        return False, 400, None
    if len(key) > MAX_KEY_LEN:
        return False, 400, None
    return True, None, f"{tenant}:{route}"


def decide(store, scope, key, body_bytes):
    """返回 (action, status):execute 执行 / replay 重放 / conflict 冲突。"""
    fingerprint = hashlib.sha256(body_bytes).hexdigest()[:16]
    record = store.get((scope, key))
    if record is None:
        return "execute", 200, fingerprint
    if record["fingerprint"] != fingerprint:
        return "conflict", 409, fingerprint
    return "replay", 200, fingerprint


store = {}
ok, _, scope = check_key("/payments", "tenant-a", str(uuid.uuid4()))
print("键合法:", ok, "作用域:", scope)

fp1 = hashlib.sha256(b'{"amount": 100}').hexdigest()[:16]
store[(scope, "k1")] = {"fingerprint": fp1, "response": {"order": "pay-0001"}}
print("同键同体:", decide(store, scope, "k1", b'{"amount": 100}')[:2])
print("同键不同体:", decide(store, scope, "k1", b'{"amount": 999}')[:2])
print("缺键:", check_key("/payments", "tenant-a", "")[:2])
