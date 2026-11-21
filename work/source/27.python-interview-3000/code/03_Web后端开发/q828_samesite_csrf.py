from __future__ import annotations

from typing import Optional

def cookie_policy(name: str, same_site: str, secure: bool) -> str:
    parts = [f"{name}=v", f"SameSite={same_site}"]
    if secure:
        parts.append("Secure")
    return "; ".join(parts)

def csrf_guard(same_site: str, origin_header: Optional[str], trusted: set) -> str:
    if same_site in ("Lax", "Strict"):
        return "SameSite 已挡住跨站写请求"
    if origin_header:
        host = origin_header.split("/")[2] if "/" in origin_header else origin_header
        if host not in trusted:
            return "Origin 不在白名单 拒绝"
    return "需要 CSRF token 校验"

print(cookie_policy("sid", "Lax", True))
print(csrf_guard("Lax", "https://evil.com", {"api.example.com"}))
print(csrf_guard("None", "https://api.example.com", {"api.example.com"}))
