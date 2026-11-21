"""审计轨迹:仅追加的哈希链,每条含前链哈希;锚点外移固化;检测篡改与截断回滚。"""
import hashlib, json


def _h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


class AuditLog:
    def __init__(self):
        self.entries = []
        self.head = "GENESIS"
        self.anchors = []

    def append(self, event):
        rec = {"seq": len(self.entries), "event": event, "prev": self.head}
        raw = json.dumps(rec, ensure_ascii=False, sort_keys=True)
        self.head = _h(raw)
        rec["hash"] = self.head
        self.entries.append(rec)
        return rec["seq"]

    def anchor(self):
        self.anchors.append((len(self.entries), self.head))
        return self.anchors[-1]

    def verify(self):
        prev = "GENESIS"
        problems = []
        for rec in self.entries:
            body = {k: rec[k] for k in ("seq", "event", "prev")}
            if _h(json.dumps(body, ensure_ascii=False, sort_keys=True)) != rec["hash"]:
                problems.append(("tampered", rec["seq"]))
            if rec["prev"] != prev:
                problems.append(("chain_break", rec["seq"]))
            prev = rec["hash"]
        for n, head in self.anchors:
            if n <= len(self.entries):
                if self.entries[n - 1]["hash"] != head:
                    problems.append(("anchor_mismatch", n))
            else:
                problems.append(("truncated", n))
        return problems


if __name__ == "__main__":
    log = AuditLog()
    for ev in ({"do": "read", "target": "doc1"}, {"do": "write", "target": "doc1"},
               {"do": "approve", "target": "doc1"}):
        log.append(ev)
    log.anchor()
    assert log.verify() == [], "正常链零告警"
    log.entries[1]["event"] = {"do": "delete", "target": "doc1"}
    assert ("tampered", 1) in log.verify(), "改历史被链哈希抓到"
    log2 = AuditLog()
    for ev in ({"do": "a"}, {"do": "b"}, {"do": "c"}):
        log2.append(ev)
    log2.anchor()
    del log2.entries[2]
    assert ("truncated", 3) in log2.verify(), "锚点指向第 3 条而现存只有 2 条 报截断"
    log3 = AuditLog()
    for ev in ({"do": "a"}, {"do": "b"}, {"do": "c"}, {"do": "d"}):
        log3.append(ev)
    log3.anchor()
    del log3.entries[1]
    problems = log3.verify()
    assert ("chain_break", 2) in problems, "中间抽条 后继的前链哈希对不上"
    assert ("truncated", 4) in problems
    print("审计轨迹通过:链式哈希 篡改可检 截断回滚可检 链断可检")
