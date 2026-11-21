"""登录-会话-登出的完整闭环: 校验、签发、请求识别、登出销毁(纯标准库)。"""
import hashlib
import hmac
import http.cookies
import secrets
import time

SESSION_TTL = 3600
PBKDF2_ROUNDS = 20000  # 演示降低轮次; 生产按 OWASP 当前建议取值

_users = {}
SESSIONS = {}


def _register(username, password):
    salt = secrets.token_hex(8)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), PBKDF2_ROUNDS)
    _users[username] = {"salt": salt, "digest": digest}


def verify_password(username, password):
    """恒定时间比较, 缺用户也要走一遍哈希, 避免时序差暴露账号存在性。"""
    user = _users.get(username)
    salt = user["salt"] if user else "decoy-salt"
    candidate = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), PBKDF2_ROUNDS)
    return user is not None and hmac.compare_digest(candidate, user["digest"])


def login(username, password, now=None):
    """成功必须签发全新 sid 防会话固定; 失败给统一文案不区分账号与口令错。"""
    if not verify_password(username, password):
        raise AuthError(401, "用户名或密码不正确")
    sid = secrets.token_urlsafe(32)
    now = time.time() if now is None else now
    SESSIONS[sid] = {"user": username, "created": now, "expires": now + SESSION_TTL}
    cookie = "sid=%s; Path=/; HttpOnly; SameSite=Lax; Max-Age=%d" % (sid, SESSION_TTL)
    return sid, cookie  # HTTPS 部署时追加 Secure


def current_user(cookie_header, now=None):
    """从 Cookie 头解析 sid 查会话; 过期即惰性删除, 不等到批量清扫。"""
    if not cookie_header:
        return None
    jar = http.cookies.SimpleCookie()
    try:
        jar.load(cookie_header)
    except http.cookies.CookieError:
        return None
    morsel = jar.get("sid")
    if morsel is None:
        return None
    session = SESSIONS.get(morsel.value)
    if session is None:
        return None
    now = time.time() if now is None else now
    if session["expires"] <= now:
        del SESSIONS[morsel.value]
        return None
    return session["user"]


def logout(sid):
    """登出即销毁服务端会话; Cookie 本体只能靠 Max-Age 辅助清场。"""
    return SESSIONS.pop(sid, None) is not None


class AuthError(Exception):
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason


_register("alice", "correct-horse")

# 1. 错误口令 -> 401, 文案不区分账号与口令错
try:
    login("alice", "wrong-password")
except AuthError as e:
    print("错误口令 -> %s %s" % (e.status, e.reason))
try:
    login("ghost", "whatever")
except AuthError as e:
    print("不存在账号 -> %s %s (同一文案)" % (e.status, e.reason))

# 2. 正确口令 -> 签发会话并下发 Cookie
sid, cookie = login("alice", "correct-horse")
print("Set-Cookie:", cookie[:40], "...")
assert "HttpOnly" in cookie and "SameSite=Lax" in cookie

# 3. 带 Cookie 的请求 -> 识别出用户
assert current_user("sid=" + sid) == "alice"
assert current_user("other=x") is None
assert current_user("") is None
assert current_user("sid=" + "forged" + "x" * 30) is None, "伪造 sid 查无会话"

# 4. 会话固定: 即使客户端预带 sid, 登录也只发全新 sid
fixed = "A" * 43
_, cookie2 = login("alice", "correct-horse")
assert fixed not in cookie2, "登录永不复用客户端带来的会话标识"

# 5. 登出闭环: 销毁后同一 Cookie 立即失效
assert logout(sid) is True
assert current_user("sid=" + sid) is None
assert logout(sid) is False, "重复登出返回未登录语义"

# 6. 过期惰性删除
sid3, _ = login("alice", "correct-horse", now=1000.0)
SESSIONS[sid3]["expires"] = 1001.0
assert current_user("sid=" + sid3, now=2000.0) is None
assert sid3 not in SESSIONS, "过期会话被顺手回收"
print("登录-会话-登出闭环演示通过")
