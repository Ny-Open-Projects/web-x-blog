import hashlib

def drift(deps: dict, lock: dict) -> list:
    keys = set(deps) | set(lock)
    return [k for k in sorted(keys) if deps.get(k) != lock.get(k)]

deps = {"fastapi": "0.115.0", "httpx": "0.27.0"}
lock = {"fastapi": "0.115.0", "httpx": "0.27.2"}
print("版本漂移:", drift(deps, lock))
print("构建产物哈希:", hashlib.sha256(b"wheel-bytes").hexdigest()[:16])
