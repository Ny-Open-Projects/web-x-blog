"""Q2996 审计日志的不可变追加:哈希链+防篡改校验。

合规要求审计日志「写了就不能改」:每条记录包含前一条的哈希,形成
链式结构,任何一条被篡改都会导致其后所有条目的哈希校验断裂。配合
只提供的 append/verify 接口(不暴露改写入口),就能用最朴素的结构
做出防抵赖的审计痕迹。校验时返回第一条断裂位置,便于定位事发点。
"""

import copy
import hashlib
import json

GENESIS = "0" * 64


class AuditLog:
    def __init__(self):
        self._entries = []

    @staticmethod
    def _hash(entry):
        payload = json.dumps(entry, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def append(self, actor, action, target, detail=None):
        prev = self._entries[-1]["hash"] if self._entries else GENESIS
        entry = {"seq": len(self._entries), "actor": actor,
                 "action": action, "target": target, "detail": detail or {},
                 "prev": prev}
        entry["hash"] = self._hash(
            {k: v for k, v in entry.items() if k != "hash"})
        self._entries.append(entry)
        return entry["seq"]

    def verify(self):
        """逐条校验链;返回 (ok, 首个断裂 seq 或 None)。"""
        prev = GENESIS
        for e in self._entries:
            body = {k: v for k, v in e.items() if k != "hash"}
            if e["prev"] != prev or self._hash(body) != e["hash"]:
                return False, e["seq"]
            prev = e["hash"]
        return True, None

    def tail(self, n=3):
        return self._entries[-n:]

    def __len__(self):
        return len(self._entries)


def main():
    log = AuditLog()
    log.append("agent", "tool.call", "pay.refund", {"order": "o_9"})
    log.append("human", "approve", "wf_1", {"level": 1})
    log.append("agent", "tool.call", "mail.send", {"to": "user@x"})
    assert len(log) == 3
    ok, broken = log.verify()
    assert ok and broken is None, (ok, broken)

    # 篡改中间一条:该条及其后全部判为断裂,且能定位到事发点
    tampered = copy.deepcopy(log)
    tampered._entries[1]["actor"] = "ghost"          # 内鬼改历史
    tampered._entries[1]["action"] = "approve"       # 伪装成已批准
    ok2, broken2 = tampered.verify()
    assert not ok2 and broken2 == 1, (ok2, broken2)

    # 篡改者连哈希一起重算:链会断在下一跳,除非重算其后所有条目
    tampered2 = copy.deepcopy(log)
    e = tampered2._entries[1]
    e["detail"] = {"level": 9}
    body = {k: v for k, v in e.items() if k != "hash"}
    e["hash"] = AuditLog._hash(body)                 # 只重算本条
    ok3, broken3 = tampered2.verify()
    assert not ok3 and broken3 == 2, (ok3, broken3)

    # 追加语义:原日志继续 append 不受影响,校验依旧通过
    log.append("human", "reject", "wf_2", {"reason": "材料不全"})
    ok4, _ = log.verify()
    assert ok4 and len(log) == 4
    last = log.tail(1)[0]
    assert last["action"] == "reject" and last["seq"] == 3
    print("校验通过:", ok4, "| 链长:", len(log))
    print("篡改定位: 中间改写断在 seq=%s, 尾部改写断在 seq=%s"
          % (broken2, broken3))


if __name__ == "__main__":
    main()
