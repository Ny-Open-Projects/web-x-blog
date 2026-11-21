"""演示用模板渲染 system prompt,注入动态变量并校验必备区块。"""

SYSTEM_TEMPLATE = """你是 {product} 的客服助手,服务于 {user_name}。
[硬性规则]
1. 只回答与 {product} 相关的问题
2. 输出必须是 JSON: {{"answer": "...", "confidence": 0到1}}
3. 不知道就承认,不要编造
[示例]
用户:怎么开发票? -> {{"answer": "在订单详情页点击申请发票", "confidence": 0.95}}"""


def render_system(product: str, user_name: str) -> str:
    return SYSTEM_TEMPLATE.format(product=product, user_name=user_name)


def validate_system(prompt: str) -> list[str]:
    checks = {"规则区块": "[硬性规则]" in prompt, "输出格式": "JSON" in prompt,
              "兜底话术": "不要编造" in prompt}
    return [name for name, ok in checks.items() if not ok] or ["校验通过"]


class FakeLLM:
    def chat(self, messages):
        return '{"answer": "请在设置页修改密码", "confidence": 0.9}'


if __name__ == "__main__":
    prompt = render_system("云盘Pro", "王工")
    print("缺失项:", validate_system(prompt))
    reply = FakeLLM().chat([{"role": "system", "content": prompt},
                            {"role": "user", "content": "怎么改密码?"}])
    print("模型输出:", reply)
