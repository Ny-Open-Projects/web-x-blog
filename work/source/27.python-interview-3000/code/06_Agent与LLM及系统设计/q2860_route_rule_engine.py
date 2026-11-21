"""Q2860 模型路由的规则引擎:声明式规则、首中即停与兜底。

把「长文走长上下文模型、代码块走代码模型、VIP 走旗舰」这类路由决策
从 if-else 堆里搬出来,变成有序的声明式规则表:按序评估、首中即停,
谁都不中走兜底。规则可增删、可测试、可导出成文档给业务方评审。
"""
FENCE = chr(96) * 3  # 反引号栅栏,运行时拼接避免与文档围栏冲突


def has_code_block(prompt: str) -> bool:
    return FENCE in prompt


RULES = [
    {"name": "vip", "model": "flagship-x",
     "test": lambda r: r.get("tier") == "vip"},
    {"name": "code_block", "model": "coder-x",
     "test": lambda r: has_code_block(r["prompt"])},
    {"name": "long_text", "model": "longctx-x",
     "test": lambda r: len(r["prompt"]) > 4000},
]
DEFAULT_MODEL = "standard-x"


def route(request: dict) -> str:
    for rule in RULES:  # 有序评估,首中即停
        if rule["test"](request):
            return rule["model"]
    return DEFAULT_MODEL


if __name__ == "__main__":
    cases = [
        {"prompt": "帮我写代码 " + FENCE + "print(1)" + FENCE, "tier": "free"},
        {"prompt": "短问题", "tier": "free"},
        {"prompt": "短问题", "tier": "vip"},
        {"prompt": "长" * 4001, "tier": "free"},
    ]
    for c in cases:
        print(route(c), "<-", c["tier"], len(c["prompt"]), "字")
    assert route(cases[0]) == "coder-x"
    assert route(cases[1]) == "standard-x"
    assert route(cases[2]) == "flagship-x"
    assert route(cases[3]) == "longctx-x"
    print("断言全部通过:声明式路由,首中即停,兜底可用")
