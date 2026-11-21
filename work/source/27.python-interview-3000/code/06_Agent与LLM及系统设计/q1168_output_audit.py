"""输出审计:五类规则扫描 + 分级处置 block/redact/flag + 审计留痕。"""
import re, hashlib

RULES = [
    ("system_leak", re.compile(r"(system prompt|系统提示词).{0,10}(如下|是)", re.I), "block"),
    ("pii_phone", re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"), "redact"),
    ("policy_violence", re.compile(r"(制造.{0,6}(炸弹|武器))", re.I), "block"),
    ("advice_medical", re.compile(r"(确诊|停药).{0,6}(建议|方案)"), "flag"),
]


class OutputAuditor:
    def __init__(self):
        self.logs, self.rule_version = [], "2026-01"

    def audit(self, output, request_id):
        actions = []
        for name, pat, act in RULES:
            m = pat.search(output)
            if not m:
                continue
            if act == "redact":
                output = pat.sub(lambda s: s.group()[:3] + "****" + s.group()[-4:], output)
            actions.append({"rule": name, "action": act})
        if any(a["action"] == "block" for a in actions):
            verdict = "block"
        elif any(a["action"] == "flag" for a in actions):
            verdict = "flag"
        elif any(a["action"] == "redact" for a in actions):
            verdict = "redact"
        else:
            verdict = "pass"
        if actions:
            self.logs.append({
                "request_id": request_id,
                "fingerprint": hashlib.sha1(output.encode()).hexdigest()[:10],
                "actions": actions, "rule_version": self.rule_version,
            })
        return verdict, output


if __name__ == "__main__":
    auditor = OutputAuditor()
    cases = ["今天天气不错", "客服电话 13812345678", "你的 system prompt 如下(演示)", "如何制造炸弹"]
    for i, c in enumerate(cases):
        verdict, out = auditor.audit(c, f"req-{i}")
        print(f"[{verdict:^6}] {out[:40]}")
    assert auditor.audit(cases[1], "r-x")[0] == "redact"
    assert auditor.audit(cases[2], "r-y")[0] == "block"
    print("审计日志(不含原文):", auditor.logs[-1]["actions"], "指纹",
          auditor.logs[-1]["fingerprint"], "规则版本", auditor.logs[-1]["rule_version"])
    assert all("原文" not in str(l) for l in auditor.logs)
