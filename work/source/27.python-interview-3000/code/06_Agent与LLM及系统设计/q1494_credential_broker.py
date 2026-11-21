"""凭据注入:工具声明所需凭据,调用时由 Broker 短暂注入,上下文只见掩码。"""
import re


class CredentialBroker:
    """凭据中转:凭据只存在 broker,工具执行帧内短暂可用,日志与上下文一律掩码。"""

    def __init__(self, vault):
        self.vault = vault                 # name -> secret
        self.audit = []

    def required(self, tool_spec):
        """工具声明的凭据需求,例如 ["api_key"]。"""
        return list(tool_spec.get("credentials", []))

    def inject(self, tool_spec, fn, args):
        """执行帧注入:把凭据作为 kwargs 传给工具,用完即弃;缺凭据直接拒绝。"""
        need = self.required(tool_spec)
        ctx = {}
        for name in need:
            if name not in self.vault:
                raise PermissionError("缺少凭据 " + name + " 调用被拒绝")
            ctx[name] = self.vault[name]
        self.audit.append((tool_spec["name"], sorted(need)))
        return fn(args, **ctx)

    @staticmethod
    def mask(secret):
        """掩码规则:留首尾各 1 字符,中间星号;短于 4 的全掩码。"""
        if len(secret) < 4:
            return "*" * len(secret)
        return secret[0] + "*" * (len(secret) - 2) + secret[-1]

    def safe_view(self, text):
        """对任意文本做掩码替换,保证凭据永不落进上下文或日志。"""
        for name, secret in self.vault.items():
            text = text.replace(secret, self.mask(secret))
        return text


def make_tool(fn):
    return fn


if __name__ == "__main__":
    vault = {"api_key": "sk-live-9f8e7d6c", "db_url": "postgres://u:p@h/db"}
    broker = CredentialBroker(vault)
    seen_in_frame = {}

    def call_api(args, api_key=None):
        seen_in_frame["key"] = api_key
        return {"status": 200, "echo": api_key}

    spec = {"name": "call_api", "credentials": ["api_key"]}
    out = broker.inject(spec, call_api, {"q": "x"})
    assert out["status"] == 200 and seen_in_frame["key"] == "sk-live-9f8e7d6c"

    missing_spec = {"name": "call_db", "credentials": ["db_password"]}
    denied = 0
    try:
        broker.inject(missing_spec, lambda a, db_password=None: None, {})
    except PermissionError:
        denied = 1
    assert denied == 1, "缺凭据必须拒绝而不是静默用空值"

    context_text = "调用结果 key=sk-live-9f8e7d6c 已返回"
    safe = broker.safe_view(context_text)
    assert "sk-live-9f8e7d6c" not in safe
    assert "s**************c" in safe
    assert broker.mask("abc") == "***"
    assert [a[0] for a in broker.audit] == ["call_api"]
    print("凭据注入通过:帧内可用缺凭据拒绝 上下文只见掩码 审计留痕")
