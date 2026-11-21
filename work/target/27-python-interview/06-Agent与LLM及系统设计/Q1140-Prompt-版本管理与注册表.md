---
title: [Q1140] Prompt 版本管理与注册表
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1140 · Prompt 版本管理与注册表

> 难度:★★★☆ | 标签:prompt 管理, 工程化

**问**:prompt 散落在代码各处,线上改一个字都可能翻车,怎么管理版本?

**答**:把 prompt 当代码管理:统一注册表(名称+版本+模板+元数据),渲染只用注册表入口,禁止业务代码内联改写。版本语义建议用"稳定版别名 stable + 语义版本 vN + 灰度别名 canary",线上流量默认 stable,灰度指 canary。每次变更记录:改动原因、评估集分数、生效范围。回滚就是把别名指回旧版本,秒级生效。模板变量必须有 schema 校验,防止漏传变量拼出畸形 prompt。

```python
# file: code/06_Agent与LLM及系统设计/q1140_prompt_registry.py
"""Prompt 注册表:版本管理 + stable/canary 别名 + 变量 schema 校验。"""


class PromptRegistry:
    def __init__(self):
        self.store = {}       # name -> {version: (template, required_vars)}
        self.alias = {}       # name -> {"stable": ver, "canary": ver}

    def register(self, name, version, template, required_vars, set_stable=False):
        self.store.setdefault(name, {})[version] = (template, required_vars)
        if set_stable or version not in self.alias.get(name, {}).values() and not self.alias.get(name):
            self.alias.setdefault(name, {})["stable"] = version

    def set_canary(self, name, version):
        assert version in self.store[name], "canary 必须先注册"
        self.alias[name]["canary"] = version

    def render(self, name, variables, channel="stable", version=None):
        version = version or self.alias[name][channel]
        template, required = self.store[name][version]
        missing = [v for v in required if v not in variables]
        assert not missing, f"变量缺失 {missing},拒绝渲染"
        return template.format(**variables), version


if __name__ == "__main__":
    reg = PromptRegistry()
    reg.register("qa", "v1", "你是客服。问题:{question}", ["question"], set_stable=True)
    reg.register("qa", "v2", "你是资深客服,先复述问题再回答:{question} (语言:{lang})", ["question", "lang"])
    reg.set_canary("qa", "v2")

    for ch in ["stable", "canary"]:
        text, ver = reg.render("qa", {"question": "怎么退款", "lang": "中文"}, channel=ch)
        print(f"[{ch}] v={ver}: {text}")

    try:
        reg.render("qa", {}, channel="canary")
    except AssertionError as e:
        print("变量缺失被拦截:", e)
    # 灰度回滚 = 把别名切回
    reg.alias["qa"]["canary"] = reg.alias["qa"]["stable"]
    _, rolled = reg.render("qa", {"question": "hi"}, channel="canary")
    assert rolled == "v1"
    print("回滚生效,canary 现指向", rolled)
```

**追问**:
- prompt 版本和代码版本怎么对齐?答:prompt 注册表入库随代码走,运行时用配置中心覆盖别名,做到"代码可回滚、prompt 可热切"。
- 多模板拼装(system+few-shot+用户段)怎么管理?答:注册表存"段"而不是整 prompt,渲染器按 pipeline 组装,每段独立版本与回归。
