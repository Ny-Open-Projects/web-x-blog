import hashlib
import json
import time


class AuditLog:
    """哈希链审计日志: 每条包含前一条哈希, 篡改任意一条即断链。"""

    def __init__(self) -> None:
        self.records: list = []
        self.prev_hash = "GENESIS"

    def append(self, actor: str, action: str, target: str,
               result: str, source: str) -> dict:
        rec = {
            "seq": len(self.records),
            "ts": time.time(),
            "actor": actor,
            "action": action,
            "target": target,
            "result": result,
            "source": source,
            "prev_hash": self.prev_hash,
        }
        rec["hash"] = hashlib.sha256(
            json.dumps(rec, sort_keys=True).encode()).hexdigest()
        self.records.append(rec)
        self.prev_hash = rec["hash"]
        return rec

    def verify(self) -> tuple:
        prev = "GENESIS"
        for i, rec in enumerate(self.records):
            expect = hashlib.sha256(
                json.dumps({k: v for k, v in rec.items() if k != "hash"},
                           sort_keys=True).encode()).hexdigest()
            if rec["prev_hash"] != prev:
                return False, f"第 {i} 条链断裂 (prev_hash 不匹配)"
            if rec["hash"] != expect:
                return False, f"第 {i} 条内容被篡改"
            prev = rec["hash"]
        return True, f"{len(self.records)} 条记录链完整"


if __name__ == "__main__":
    audit = AuditLog()
    audit.append("op-wang", "ssh.login", "prod-db-1", "ok", "10.2.3.4")
    audit.append("op-wang", "db.query", "prod-db-1/users", "ok", "10.2.3.4")
    audit.append("svc-billing", "api.call", "payment/refund", "denied", "10.5.1.9")
    audit.append("op-li", "config.update", "gateway/rate_limit", "ok", "10.2.3.7")

    for rec in audit.records:
        print(f"  #{rec['seq']} {rec['actor']:<10} {rec['action']:<14} "
              f"{rec['target']:<22} {rec['result']:<6} {rec['hash'][:12]}...")

    ok, msg = audit.verify()
    print("\n完整性校验:", ok, "-", msg)

    # 篡改演练: 改一条历史记录
    audit.records[1]["result"] = "ok-tampered"
    ok, msg = audit.verify()
    print("篡改后校验:", ok, "-", msg)
    assert not ok
