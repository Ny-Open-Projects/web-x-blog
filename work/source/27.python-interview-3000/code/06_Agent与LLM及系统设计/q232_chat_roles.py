"""演示消息角色的组织方式,并统计 token 预算(按简单切分模拟)。"""


class FakeChatModel:
    def chat(self, messages):
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        return f"遵守规则[{system[:6]}],回答你的问题"


def build_messages(system: str, history: list[tuple[str, str]], user: str) -> list[dict]:
    msgs = [{"role": "system", "content": system}]
    for u, a in history:
        msgs += [{"role": "user", "content": u}, {"role": "assistant", "content": a}]
    msgs.append({"role": "user", "content": user})
    return msgs


def approx_tokens(messages) -> int:
    return sum(len(m["content"]) for m in messages) // 2  # 简化估算


if __name__ == "__main__":
    msgs = build_messages(
        "你是客服,只用中文回答",
        history=[("怎么退货?", "在订单页点申请退货")],
        user="退款多久到账?",
    )
    for m in msgs:
        print(m["role"], "->", m["content"])
    print(FakeChatModel().chat(msgs), "| 估算 token:", approx_tokens(msgs))
