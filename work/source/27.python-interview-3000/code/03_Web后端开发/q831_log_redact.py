import re

SENSITIVE = re.compile(r"(password|token|authorization|card_no)[=:]\s*([^\s,&]+)", re.I)

def redact(msg: str) -> str:
    return SENSITIVE.sub(lambda m: f"{m.group(1)}=***", msg)

SENSITIVE_KEYS = {"password", "token", "authorization"}

def redact_dict(d: dict) -> dict:
    return {k: ("***" if k.lower() in SENSITIVE_KEYS else v) for k, v in d.items()}

print(redact("POST /login password=hunter2 token=abc123 ip=1.2.3.4"))
print(redact_dict({"password": "x", "note": "ok"}))
