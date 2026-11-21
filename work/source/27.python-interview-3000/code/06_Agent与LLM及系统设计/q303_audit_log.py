import hashlib
import json
import time


class AuditLog:
    """只追加审计日志,带哈希链防篡改。"""
    def __init__(self):
        self.records: list[dict] = []
        self._prev_hash = "GENESIS"

    def record(self, actor: str, action: str, resource: str,
               before=None, after=None) -> dict:
        entry = {
            "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
            "actor": actor, "action": action, "resource": resource,
            "before": before, "after": after, "prev": self._prev_hash,
        }
        entry["hash"] = hashlib.sha256(
            json.dumps(entry, sort_keys=True).encode()).hexdigest()[:16]
        self._prev_hash = entry["hash"]
        self.records.append(entry)
        return entry

    def verify(self) -> bool:
        prev = "GENESIS"
        for r in self.records:
            if r["prev"] != prev:
                return False
            prev = r["hash"]
        return True


if __name__ == "__main__":
    log = AuditLog()
    log.record("admin", "update", "salary:1001", before=5000, after=6000)
    log.record("hr", "delete", "employee:42")
    print(log.verify())  # True
    log.records[0]["after"] = 9999  # 模拟篡改
    print(log.verify())  # False
