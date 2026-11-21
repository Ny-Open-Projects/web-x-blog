"""敏感操作的二次确认: 最近强认证窗口(纯标准库)。"""
import time


class StepUpGate:
    """高危操作要求 N 分钟内做过强认证(如二次密码/OTP), 否则要求先补认证。

    低危操作不受影响; 认证通过即刷新窗口时间戳。
    """

    def __init__(self, window_seconds=300):
        self.window = window_seconds
        self.strong_auth_at = {}      # session_id -> last strong auth ts

    def authenticate(self, session_id, now, method="otp"):
        if method != "otp":
            return False, "弱认证不进入窗口"
        self.strong_auth_at[session_id] = now
        return True, "强认证完成"

    def allow(self, session_id, risk, now):
        """返回 (allowed, status, www_authenticate)。"""
        if risk == "low":
            return True, 200, None
        last = self.strong_auth_at.get(session_id, 0)
        if now - last <= self.window:
            return True, 200, None
        return False, 401, "Reauth realm=high-risk, prompt=login"


gate = StepUpGate(window_seconds=300)
t0 = 1762050000.0
gate.authenticate("sess-1", t0)
print("刚认证完执行转账:", gate.allow("sess-1", "high", t0 + 60)[0:2])
assert gate.allow("sess-1", "high", t0 + 60)[0]

ok, status, www = gate.allow("sess-1", "high", t0 + 301)
print("10 分钟后执行转账 ->", status, "要求头:", www)
assert not ok and status == 401 and "Reauth" in www

ok, msg = gate.authenticate("sess-1", t0 + 310)
ok2, status2, _ = gate.allow("sess-1", "high", t0 + 320)
print("补认证后重试 ->", status2)
assert ok2
ok3, _, _ = gate.allow("sess-1", "low", t0 + 400)
print("低危浏览类操作始终放行:", ok3)
assert ok3
print("要点: 窗口型二次确认把安全与体验解耦, 高危动作点名单独要求, 响应带 WWW-Authenticate 引导客户端")
