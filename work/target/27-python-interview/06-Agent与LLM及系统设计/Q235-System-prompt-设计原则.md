---
title: [Q235] System prompt 设计原则
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q235 · System prompt 设计原则

> 难度:★★★ | 标签:Agent, Prompt

**问**:写一个好的 system prompt 有哪些要点?常见反模式是什么?

**答**:要点:1) 明确身份与目标(你是谁、为谁服务);2) 硬性约束放前面(禁答范围、输出格式、语言);3) 给 1-3 个 few-shot 示例统一风格;4) 工具使用规则明确(何时调用、参数来源);5) 失败时的兜底话术。反模式:把所有要求堆成一大段无结构文本、规则自相矛盾、依赖"请务必"这类情绪化强调而缺少可验证格式、把动态内容(当天日期、用户名)硬编码进 system 而非模板注入。

```python
# file: code/06_Agent与LLM及系统设计/q235_system_prompt.py
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
```

**追问**:
- 动态内容为什么不能硬编码进 system?——当天日期、用户名属于每次请求变化的模板变量,硬编码会让前缀缓存失效且多轮共享 session 串台;用模板渲染注入。
- few-shot 示例放 system 还是 user?——示例属「全局行为规范」放 system(还能吃前缀缓存);单条输入的示例才放当轮 user。
- 怎么验证 system prompt 有效?——离线评估集回归(改 prompt 跑一遍用例看指标),而不是凭感觉;prompt 要版本化管理,坏版本能回滚。
