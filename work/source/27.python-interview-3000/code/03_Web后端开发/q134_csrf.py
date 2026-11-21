import secrets

# Django 内置方案的双提交校验逻辑示意
SESSIONS: dict[str, str] = {}     # session_id -> csrf_token

def issue_token(session_id: str) -> str:
    token = secrets.token_urlsafe(32)
    SESSIONS[session_id] = token          # ① Cookie/Session 侧存一份
    return token                          # ② 表单 hidden 字段发一份

def verify(session_id: str, form_token: str) -> bool:
    expected = SESSIONS.get(session_id)
    return bool(expected) and secrets.compare_digest(expected, form_token)

# settings.py: MIDDLEWARE 需含 CsrfViewMiddleware
# 模板: <form>{% csrf_token %}</form>
# 前后端分离: 前端从 cookie 取 csrftoken 放入 X-CSRFToken 头

sid = 'sess-0001'
tok = issue_token(sid)
print(verify(sid, tok), verify(sid, 'evil-token'))
