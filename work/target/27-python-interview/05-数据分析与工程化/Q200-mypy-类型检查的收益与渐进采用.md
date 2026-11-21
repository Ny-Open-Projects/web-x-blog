---
title: [Q200] mypy 类型检查的收益与渐进采用
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q200 · mypy 类型检查的收益与渐进采用

> 难度:★★★ | 标签:mypy, typing

**问**:Python 是动态语言,加 mypy 图什么?老项目怎么渐进引入?

**答**:mypy 在**运行前**捕获类型错误:None 传播(`Optional` 没判空)、参数顺序错、返回类型错——这些恰恰是单测最容易漏的分支。收益还有:类型即文档、IDE 补全和重构变可靠、接口契约显式化。渐进策略:先开 `--ignore-missing-imports` 处理无类型注解的第三方库,配置 `per-module-options` 对核心模块 strict、对遗留模块宽松,新增代码从 day 1 强制注解;再用 stub(`types-*` 包或自写 .pyi)补关键依赖。运行期不做类型检查是重要认知:mypy 是静态分析,与运行时行为无关。

```python
# file: code/05_数据分析与工程化/q200_mypy_demo.py
from typing import Optional


def find_user(user_id: int, cache: dict[int, str]) -> Optional[str]:
    # 返回值可能为 None,调用方必须处理
    return cache.get(user_id)


def send_welcome(name: str) -> str:
    # mypy 会报错:Argument 1 has incompatible type Optional[str]
    # return send_welcome(find_user(1, {}))
    user = find_user(1, {})
    if user is None:
        return "guest"
    return f"welcome {user}"


def test_none_handling():
    assert find_user(1, {}) is None
    assert send_welcome("ada") == "welcome ada"
```

**追问**:
- pyright 和 mypy 选哪个?——两者都成熟;pyright 更快且和 VSCode(Pylance)集成好,mypy 生态和插件多,团队统一一个即可。
- mypy 对第三方库报 missing stubs 怎么办?——装 types-* 包或 `ignore_missing_imports` 局部豁免;给核心依赖自写 .pyi 桥接。
- strict 模式包含什么?——disallow_untyped_defs、warn_return_any 等开关集合;核心模块先 strict,存量模块渐进。
- 类型注解会拖慢运行吗?——不会,注解不求值(除非显式);运行时校验是 pydantic 这类库显式做的事,与 mypy 分工不同。
