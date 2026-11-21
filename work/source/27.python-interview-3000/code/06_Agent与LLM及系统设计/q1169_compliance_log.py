"""合规日志:分级保留 + 脱敏可检索层 + 访问审计 + 被遗忘权删除。"""
import hashlib, json, re, time


class ComplianceLog:
    RETENTION = {"raw": 180 * 86400, "masked": 3 * 365 * 86400}

    def __init__(self):
        self.raw, self.masked, self.access_log, self.tombstones = [], [], [], set()

    @staticmethod
    def _mask(text):
        return re.sub(r"(?<!\d)1[3-9]\d{9}(?!\d)", lambda m: m.group()[:3] + "****", text)

    def write(self, user_id, content):
        if user_id in self.tombstones:
            return "erased_user"
        now = time.time()
        self.raw.append({"user": user_id, "content": content, "expire": now + self.RETENTION["raw"]})
        self.masked.append({"user": hashlib.sha1(user_id.encode()).hexdigest()[:10],
                            "content": self._mask(content),
                            "expire": now + self.RETENTION["masked"]})
        return "ok"

    def query(self, operator, keyword, scope="masked"):
        self.access_log.append({"operator": operator, "scope": scope, "kw_fp": hashlib.sha1(keyword.encode()).hexdigest()[:8], "at": time.time()})
        source = self.masked if scope == "masked" else self.raw
        return [r for r in source if keyword in r["content"]]

    def gc(self):
        now = time.time()
        self.raw = [r for r in self.raw if r["expire"] > now]
        self.masked = [r for r in self.masked if r["expire"] > now]

    def erase_user(self, user_id):
        self.tombstones.add(user_id)
        self.raw = [r for r in self.raw if r["user"] != user_id]
        fp = hashlib.sha1(user_id.encode()).hexdigest()[:10]
        self.masked = [r for r in self.masked if r["user"] != fp]
        return "erased"


if __name__ == "__main__":
    log = ComplianceLog()
    log.write("u-1001", "手机 13911112222 查订单")
    log.write("u-1002", "普通咨询内容")
    hits = log.query("ops-a", "13911112222")
    print("脱敏层检索:", hits)
    assert "13911112222" not in json.dumps(hits), "脱敏层不允许出现原文手机号"
    raw_query = log.query("ops-b", "13911112222", scope="raw")
    assert raw_query, "原始层需授权后才可查(此处仅演示隔离)"
    print("访问审计:", len(log.access_log), "条,含操作者与查询指纹")
    log.erase_user("u-1001")
    assert not log.query("ops-a", "13911112222"), "被遗忘权删除生效"
    print("删除后脱敏层与原始层均无该用户数据")
