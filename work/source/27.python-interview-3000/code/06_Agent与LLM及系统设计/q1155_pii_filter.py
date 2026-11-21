"""PII 过滤管线:检测->分类->占位脱敏->审计,支持同请求一致占位。"""
import hashlib, re

PATTERNS = {
    "PHONE": (re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"), lambda s: s[:3] + "****" + s[-4:]),
    "ID_CARD": (re.compile(r"(?<!\d)\d{17}[\dXx](?!\d)"), lambda s: s[:4] + "**********" + s[-3:]),
    "API_KEY": (re.compile(r"\b(sk-[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16})\b"), lambda s: s[:5] + "***REDACTED***"),
}


class PIIFilter:
    def __init__(self):
        self.audit = []

    def sanitize(self, text, source="input"):
        found, mapping = [], {}
        for kind, (pat, mask) in PATTERNS.items():
            for m in pat.finditer(text):
                raw = m.group()
                if raw not in mapping:
                    token = f"{kind}_{len(mapping) + 1}"
                    mapping[raw] = token
                    found.append({"kind": kind, "token": token,
                                  "fp": hashlib.sha1(raw.encode()).hexdigest()[:8]})
                text = text.replace(raw, mapping[raw])
        self.audit.append({"source": source, "hits": found})
        return text, found


if __name__ == "__main__":
    f = PIIFilter()
    raw = "用户手机 13812345678,身份证 11010119900307867X,我的 key 是 sk-abcdef1234567890abcdef"
    clean, hits = f.sanitize(raw)
    print("脱敏后:", clean)
    for h in hits:
        print("  命中:", h["kind"], "指纹", h["fp"], "->", h["token"])
    assert "13812345678" not in clean and "sk-abcdef" not in clean
    # 同一值第二次出现应得到一致占位
    clean2, _ = f.sanitize("再发一次 13812345678")
    assert "PHONE_1" in clean2, "相同原值占位一致便于模型引用"
    print(f"审计记录 {len(f.audit)} 条,原始值未入库")
