"""会话固定防护:登录时废弃旧 SID 重新生成(纯标准库)。"""
import secrets

sessions = {}   # sid -> {"user": 用户名或 None}


def new_session():
    sid = secrets.token_urlsafe(32)
    sessions[sid] = {"user": None}
    return sid


def login_vulnerable(sid, user):
    sessions[sid]["user"] = user          # 错误示范:沿用攻击者预置的 SID
    return sid


def login_safe(sid, user):
    sessions.pop(sid, None)               # 正确:作废旧 SID,防止固定
    new_sid = new_session()
    sessions[new_sid]["user"] = user
    return new_sid


attacker_sid = new_session()
print("攻击者预置 SID:", attacker_sid[:16], "...")

victim_sid_vuln = login_vulnerable(attacker_sid, "alice")
print("未防护:受害者登录后 SID 未变 ->", victim_sid_vuln == attacker_sid)
print("攻击者用同一 SID 访问 ->", sessions[attacker_sid])

victim_sid_safe = login_safe(new_session(), "alice")
print("已防护:新 SID 与旧 SID 必然不同 ->", victim_sid_safe != attacker_sid)
print("旧 SID 已失效 ->", attacker_sid not in sessions)
