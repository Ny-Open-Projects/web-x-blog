"""Q3000 端到端客服 Agent 综合骨架:意图-检索-工具-人审-审计。

把前面所有零件装成一台整机:入口先做意图路由(知识问答走检索、
业务操作走工具、闲聊走兜底);工具执行前过策略闸(金额阈值决定
自动处理还是转人工);全过程写哈希链审计日志;会话跨轮保持状态。
骨架的价值在接缝:每个接缝都有明确的拒绝与升级路径,而不是各自
为政的完美组件。
"""

import hashlib
import json
import math

DIM = 32


def embed(text):
    vec = [0.0] * DIM
    for token in text.split():
        h = int(hashlib.md5(token.encode("utf-8")).hexdigest(), 16)
        vec[h % DIM] += 1.0
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


class AuditLog:
    """哈希链审计:append-only,verify 定位首条断裂。"""

    def __init__(self):
        self.entries = []

    def append(self, actor, action, detail):
        prev = self.entries[-1]["hash"] if self.entries else "0" * 64
        body = {"actor": actor, "action": action, "detail": detail,
                "prev": prev}
        body["hash"] = hashlib.sha256(
            json.dumps(body, sort_keys=True, ensure_ascii=False)
            .encode("utf-8")).hexdigest()
        self.entries.append(body)
        return len(self.entries) - 1

    def verify(self):
        prev = "0" * 64
        for i, e in enumerate(self.entries):
            body = {k: v for k, v in e.items() if k != "hash"}
            if e["prev"] != prev or hashlib.sha256(
                    json.dumps(body, sort_keys=True,
                               ensure_ascii=False)
                    .encode("utf-8")).hexdigest() != e["hash"]:
                return False, i
            prev = e["hash"]
        return True, None


KNOWLEDGE = [
    ("退款 到账 政策 三个工作日内 原路 退回 超时 转人工", "policy"),
    ("发货 物流 时效 四十八小时内 发出 偏远地区 顺延", "shipping"),
]
ORDERS = {"o_1": {"user": "u_1", "amount": 200, "days_since": 3},
          "o_2": {"user": "u_1", "amount": 3000, "days_since": 2},
          "o_3": {"user": "u_1", "amount": 200, "days_since": 12}}
REFUND_LIMIT = 500          # 超过即需人工确认


class SupportAgent:
    def __init__(self, user_id, audit):
        self.user = user_id
        self.audit = audit
        self.session = []
        self.pending = None        # 待人审的工单

    def _retrieve(self, question):
        qv = embed(question)
        best, score = None, -1.0
        for text, doc in KNOWLEDGE:
            s = cosine(qv, embed(text))
            if s > score:
                best, score = (text, doc), s
        return best, round(score, 4)

    def _classify(self, msg):
        # 带合法订单号才走业务工具,否则退款类咨询一律是知识问答
        if any(w in ORDERS for w in msg.split()):
            return "refund"
        if any(w in msg for w in ("退款", "退货", "订单", "发货",
                                  "物流", "到账")):
            return "faq"
        return "chitchat"

    def handle(self, msg):
        self.session.append(("user", msg))
        intent = self._classify(msg)
        self.audit.append("agent", "intent", {"msg": msg, "intent": intent})
        if intent == "refund":
            return self._refund(msg)
        if intent == "faq":
            return self._faq(msg)
        reply = "您好,我是客服助手,可以帮您查询退款与物流问题。"
        self.session.append(("assistant", reply))
        return {"reply": reply, "handoff": False}

    def _faq(self, msg):
        (text, doc), score = self._retrieve(msg)
        if score < 0.3:
            reply = "这个问题我需要人工帮您确认。"
            self.session.append(("assistant", reply))
            self.audit.append("agent", "handoff", {"reason": "low_score"})
            return {"reply": reply, "handoff": True}
        reply = "根据%s政策:%s" % (doc, text.split()[0])
        self.session.append(("assistant", reply))
        self.audit.append("agent", "faq_answer", {"doc": doc})
        return {"reply": reply, "handoff": False, "cite": doc}

    def _refund(self, msg):
        order_id = next((w for w in msg.split() if w in ORDERS), None)
        if order_id is None:
            reply = "请提供订单号,例如:退款 o_1。"
            self.session.append(("assistant", reply))
            return {"reply": reply, "handoff": False}
        order = ORDERS[order_id]
        self.audit.append("agent", "policy_check",
                          {"order": order_id, **order})
        if order["days_since"] > 7:
            reply = "订单 %s 已超过七天,需人工审核。" % order_id
            self.session.append(("assistant", reply))
            self.audit.append("agent", "handoff", {"order": order_id,
                                                   "reason": "over_7d"})
            return {"reply": reply, "handoff": True}
        if order["amount"] > REFUND_LIMIT:
            self.pending = {"order": order_id, "amount": order["amount"]}
            reply = "订单 %s 金额较大,已转人工确认,请稍候。" % order_id
            self.session.append(("assistant", reply))
            self.audit.append("agent", "handoff",
                              {"order": order_id, "reason": "amount"})
            return {"reply": reply, "handoff": True, "pending": True}
        self.audit.append("tool", "pay.refund", {"order": order_id,
                                                 "amount": order["amount"]})
        reply = "订单 %s 退款 %d 元已受理,3 个工作日内原路退回。" \
            % (order_id, order["amount"])
        self.session.append(("assistant", reply))
        return {"reply": reply, "handoff": False}


def main():
    audit = AuditLog()
    agent = SupportAgent("u_1", audit)

    # 知识问答:命中检索并带引用
    out1 = agent.handle("退款 到账 时间")
    assert out1["handoff"] is False and "cite" in out1, out1
    assert out1["reply"].startswith("根据"), out1

    # 小额+在期内:自动受理
    out2 = agent.handle("退款 o_1")
    assert "已受理" in out2["reply"] and not out2["handoff"], out2

    # 大额:转人工,挂起工单
    out3 = agent.handle("退款 o_2")
    assert out3["handoff"] and out3.get("pending"), out3
    assert agent.pending == {"order": "o_2", "amount": 3000}

    # 超七天:转人工
    out4 = agent.handle("退款 o_3")
    assert out4["handoff"] and "超过七天" in out4["reply"], out4

    # 闲聊:兜底话术
    out5 = agent.handle("在吗")
    assert "客服助手" in out5["reply"] and not out5["handoff"]

    # 会话状态与审计链
    assert len(agent.session) == 10            # 5 轮 x 2 条
    assert agent.session[0][0] == "user"
    ok, broken = audit.verify()
    assert ok and broken is None, (ok, broken)
    actions = [e["action"] for e in audit.entries]
    assert actions.count("handoff") == 2, actions     # 两次升级都有留痕
    assert "policy_check" in actions and "pay.refund" in actions
    print("FAQ:", out1["reply"], "| 引用:", out1["cite"])
    print("小额退款:", out2["reply"])
    print("审计链长度:", len(audit.entries), "| 校验:", ok)
    print("动作序列:", actions)


if __name__ == "__main__":
    main()
