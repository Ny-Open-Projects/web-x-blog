
RULES = [
    ("P0", lambda e: e.get("slo_impact") and e.get("scope") == "all"),
    ("P1", lambda e: e.get("slo_impact") or e.get("scope") == "partial"),
    ("P2", lambda e: e.get("trend_bad")),
    ("P3", lambda e: True),
]
SLA = {
    "P0": ("15 分钟内响应", "电话 + 群通知"),
    "P1": ("30 分钟内响应", "群 + 短信"),
    "P2": ("当日处理", "工单"),
    "P3": ("排期处理", "周报汇总"),
}

def grade(event):
    for level, rule in RULES:
        if rule(event):
            return level
    return "P3"

if __name__ == "__main__":
    for ev in ({"slo_impact": True, "scope": "all"}, {"scope": "partial"}, {"trend_bad": True}, {}):
        level = grade(ev)
        print(ev, "->", level, SLA[level])
