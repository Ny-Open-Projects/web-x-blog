---
title: [Q238] 工具注册与 JSON Schema 校验
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q238 · 工具注册与 JSON Schema 校验

> 难度:★★★ | 标签:Agent, Tool

**问**:如何设计一个工具注册表?为什么参数校验要在发给模型前就写好 Schema?

**答**:工具注册表核心是"函数 → 元数据"的映射:名称、人类可读描述(给模型看,决定它是否调用)、参数 JSON Schema、实际可执行对象。注册时用类型注解自动生成 Schema,调用前用 Schema 校验模型给出的参数,不合法就拒绝执行并把错误反馈给模型。描述质量直接影响调用准确率:描述要说明"什么时候用、不什么时候用、参数含义与格式"。

```python
# file: code/06_Agent与LLM及系统设计/q238_tool_registry.py
"""一个极简工具注册表:装饰器注册、JSON Schema 生成、参数校验、类型转换。"""


class ToolRegistry:
    TYPE_MAP = {"str": str, "int": int, "float": float, "bool": bool}

    def __init__(self):
        self._tools = {}

    def tool(self, name: str, description: str, params_schema: dict):
        def deco(fn):
            self._tools[name] = {"fn": fn, "description": description,
                                 "schema": params_schema}
            return fn
        return deco

    def to_api_defs(self) -> list[dict]:
        return [{"name": n, "description": t["description"], "parameters": t["schema"]}
                for n, t in self._tools.items()]

    def validate_and_call(self, name: str, args: dict) -> str:
        if name not in self._tools:
            return f"错误:未知工具 {name}"
        schema = self._tools[name]["schema"]
        for key in schema.get("required", []):   # Schema 层级的必填检查
            if key not in args:
                return f"错误:缺少必填参数 {key}"
        for key, spec in schema["properties"].items():
            if key in args and not isinstance(args[key], self.TYPE_MAP[spec["type"]]):
                return f"错误:参数 {key} 类型应为 {spec['type']}"
        return str(self._tools[name]["fn"](**args))


reg = ToolRegistry()


@reg.tool("search_flight", description="查询两个城市间的航班,不知道出发地时不要调用",
          params_schema={"type": "object",
                         "properties": {"origin": {"type": "str"},
                                        "dest": {"type": "str"}},
                         "required": ["origin", "dest"]})
def search_flight(origin: str, dest: str) -> str:
    return f"{origin}->{dest} 有 3 个航班,最低 680 元"


if __name__ == "__main__":
    print("API 工具定义:", reg.to_api_defs()[0]["name"])
    print(reg.validate_and_call("search_flight", {"origin": "北京", "dest": "上海"}))
    print(reg.validate_and_call("search_flight", {"origin": 123, "dest": "上海"}))
    print(reg.validate_and_call("search_flight", {"origin": "北京"}))
    print(reg.validate_and_call("no_such_tool", {}))
```

**追问**:
- 工具太多怎么办?按场景分组、只注入当前任务相关的工具子集,或用工具检索(先检索再注入)降低选择噪声。
- 描述质量怎么影响调用准确率?——模型靠描述决定「何时调用、参数怎么填」;描述要含使用时机、反例、参数格式,并用评估集验证。
- Schema 校验失败的反馈怎么做?——把具体校验错误(哪个字段、什么原因)以 tool 消息回传;泛泛的「参数错误」修正率极低。
- 注册表怎么和代码同步?——类型注解自动生成 Schema(pydantic/jsonschema),避免文档与实现漂移;工具变更走版本化。
