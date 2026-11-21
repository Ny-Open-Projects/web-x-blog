"""双层 Guardrails:规则层拦敏感信息,模型层 stub 判有害,支持脱敏改写。"""
import re

PII_PATTERNS = {
    "手机号": r"1[3-9]\d{9}",
    "身份证": r"\d{17}[\dXx]",
    "密钥": r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{16,})",
}


class Guardrails:
    def __init__(self, toxicity_classifier=None):
        self.cls = toxicity_classifier or (lambda t: False)  # 默认无害

    def inspect_input(self, text: str) -> tuple[str, str]:
        """返回 (处理后的文本, 动作)。动作: pass / redact / block"""
        if self.cls(text):
            return text, "block"
        redacted = text
        for name, pat in PII_PATTERNS.items():
            redacted = re.sub(pat, f"[{name}已脱敏]", redacted)
        return redacted, "redact" if redacted != text else "pass"

    def inspect_output(self, text: str) -> tuple[str, str]:
        for name, pat in PII_PATTERNS.items():
            if re.search(pat, text):
                return re.sub(pat, f"[{name}已脱敏]", text), "redact"
        return text, "pass"


def fake_toxicity_classifier(text: str) -> bool:
    return "怎么制作危险品" in text


if __name__ == "__main__":
    g = Guardrails(fake_toxicity_classifier)
    cases = ["我的手机号是13812345678,帮我注册",
             "key 是 sk-abcdefghijklmnop1234 请保存",
             "怎么制作危险品"]
    for c in cases:
        out, action = g.inspect_input(c)
        print(f"[输入:{action}] {out}")
    out, action = g.inspect_output("回复:用户邮箱 user@x.com,手机 13900001111")
    print(f"[输出:{action}] {out}")
