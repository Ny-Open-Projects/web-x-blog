"""Q2573 会话导出与导入的可移植性:带版本号的状态快照。

会话状态只有导出成带 schema_version 的纯数据,才能跨进程跨机器
搬家;导入侧用版本闸拒绝过高的版本,往返导出导入后状态逐字段
等价,凭据类字段绝不进快照。
"""
import json

SCHEMA_VERSION = 2


class Session:
    def __init__(self, tenant, messages=None, anchors=None, counters=None):
        self.tenant = tenant
        self.messages = messages or []
        self.anchors = anchors or []
        self.counters = counters or {"turns": 0}

    def export(self):
        return {"schema_version": SCHEMA_VERSION, "tenant": self.tenant,
                "messages": list(self.messages), "anchors": list(self.anchors),
                "counters": dict(self.counters)}

    @classmethod
    def import_(cls, blob):
        if blob["schema_version"] > SCHEMA_VERSION:
            raise ValueError("会话 schema_version " + str(blob["schema_version"])
                             + " 高于当前支持的 " + str(SCHEMA_VERSION))
        return cls(blob["tenant"], blob.get("messages"),
                   blob.get("anchors"), blob.get("counters"))


def main():
    a = Session("t1", [{"role": "user", "text": "hi"}], ["m0"], {"turns": 3})
    blob = json.loads(json.dumps(a.export(), ensure_ascii=False))
    b = Session.import_(blob)
    assert b.tenant == a.tenant and b.messages == a.messages
    assert b.counters == a.counters and b.anchors == a.anchors
    assert b.export() == a.export()
    blob["schema_version"] = 99
    rejected = False
    try:
        Session.import_(blob)
    except ValueError as exc:
        rejected = True
        print("版本闸:", exc)
    assert rejected, "高版本会话应被拒绝"
    print("导出导入往返一致,状态逐字段等价")


if __name__ == "__main__":
    main()
