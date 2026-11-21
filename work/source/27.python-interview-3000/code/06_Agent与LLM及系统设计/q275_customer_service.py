"""端到端智能客服骨架:意图路由 + RAG + 工具调用 + 转人工 + 防护,全 stub。"""


def fake_embed(t):
    return [ord(c) % 7 for c in t[:6].ljust(6, "x")]


KNOWLEDGE = ["我们的退货政策是 7 天无理由", "会员每月送 10GB 流量"]
ORDERS = {"1001": {"status": "已发货", "carrier": "顺丰"}}


def classify(text: str) -> str:
    if any(k in text for k in ["投诉", "人工"]):
        return "human"
    if any(k in text for k in ["退款", "订单", "物流", "发货"]):
        return "action"   # 退款是写操作,归入 action 后走人工确认,而不是直接转人工
    return "knowledge"


class KnowledgeRAG:
    def answer(self, q: str) -> str:
        hits = max(KNOWLEDGE, key=lambda d: sum(a == b for a, b in zip(fake_embed(d), fake_embed(q))))
        return f"根据知识库[{hits[:12]}...]回答您的问题"


def query_order(order_id: str) -> str:
    return str(ORDERS.get(order_id, "订单不存在"))


def serve(user_text: str) -> str:
    intent = classify(user_text)
    if intent == "human":
        return "已为您转接人工客服"
    if intent == "action":
        if "退款" in user_text:   # 写操作:强制确认
            return "退款操作需人工确认后执行(高危)"
        import re
        m = re.search(r"\d{3,}", user_text)
        return f"订单信息:{query_order(m.group())}" if m else "请提供订单号"
    return KnowledgeRAG().answer(user_text)


if __name__ == "__main__":
    for q in ["退货政策是什么?", "订单 1001 到哪了?", "我要退款!", "你好"]:
        print(f"Q: {q}\nA: {serve(q)}\n")
