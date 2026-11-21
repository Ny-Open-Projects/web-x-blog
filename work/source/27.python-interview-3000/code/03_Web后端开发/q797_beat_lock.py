import time

lock_store: dict = {}

def try_lock(name: str, ttl: float) -> bool:
    now = time.time()
    holder = lock_store.get(name)
    if holder and holder > now:
        return False
    lock_store[name] = now + ttl
    return True

def nightly_job() -> str:
    if not try_lock("nightly-report", ttl=3600):
        return "已被其他节点执行"
    return "执行报表生成"

print(nightly_job())
print(nightly_job())
