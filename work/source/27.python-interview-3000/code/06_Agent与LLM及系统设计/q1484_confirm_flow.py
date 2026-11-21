"""敏感操作二次确认流:风险分级 + 确认码匹配 + 冷却窗口 + 过期作废。"""
import time


class ConfirmGate:
    """高危工具先发挑战再放行:用户必须原样复述确认码,防止模型自答自批。"""

    def __init__(self, cooldown=5.0, ttl=60.0):
        self.cooldown = cooldown            # 两次挑战的最小间隔,防轰炸
        self.ttl = ttl                      # 挑战有效期
        self.pending = {}                   # req_id -> {"code","expires","action"}
        self.last_issue = 0.0
        self.audit = []

    def challenge(self, req_id, action, risk):
        """返回是否已发出挑战;低风险直接放行,高危需要二次确认。"""
        now = time.time()
        if risk == "high" or risk == "critical":
            if now - self.last_issue < self.cooldown:
                return {"ok": False, "why": "挑战过于频繁 请稍后再试"}
            code = "确认执行" + action.replace("_", "")
            self.pending[req_id] = {"code": code, "expires": now + self.ttl, "action": action}
            self.last_issue = now
            self.audit.append(("challenge", req_id, action))
            return {"ok": False, "need_confirm": True, "code_hint": code[:2] + "**", "req_id": req_id}
        self.audit.append(("auto_allow", req_id, action))
        return {"ok": True, "need_confirm": False}

    def confirm(self, req_id, user_reply, now=None):
        """核对确认码:过期作废、错码拒绝、答对后从 pending 移除防重放。"""
        now = now if now is not None else time.time()
        rec = self.pending.get(req_id)
        if not rec:
            return {"ok": False, "why": "无待确认请求"}
        if now > rec["expires"]:
            del self.pending[req_id]
            return {"ok": False, "why": "挑战已过期 需重新发起"}
        if user_reply != rec["code"]:
            return {"ok": False, "why": "确认码不匹配"}
        del self.pending[req_id]
        self.audit.append(("approved", req_id, rec["action"]))
        return {"ok": True, "action": rec["action"]}


class FakeUser:
    """模拟用户输入:正例会复述提示中的完整确认码,负例乱答。"""


if __name__ == "__main__":
    gate = ConfirmGate(cooldown=0.0)
    r1 = gate.challenge("r1", "delete_database", "critical")
    assert r1["need_confirm"] is True
    code = "确认执行delete" + "database"
    bad = gate.confirm("r1", "好的我确认")
    assert bad["ok"] is False and "不匹配" in bad["why"]
    good = gate.confirm("r1", code)
    assert good["ok"] is True
    replay = gate.confirm("r1", code)
    assert replay["ok"] is False and "无待确认" in replay["why"]

    r2 = gate.challenge("r2", "read_file", "low")
    assert r2["need_confirm"] is False and r2["ok"] is True

    expired = ConfirmGate(cooldown=0.0, ttl=-1.0)
    expired.challenge("r3", "drop_table", "high")
    late = expired.confirm("r3", "确认执行drop" + "table")
    assert late["ok"] is False and "过期" in late["why"]
    assert [a[0] for a in gate.audit] == ["challenge", "approved", "auto_allow"]
    print("二次确认流通过:错码拒绝、过期作废、一次性消费、低风险直放")
