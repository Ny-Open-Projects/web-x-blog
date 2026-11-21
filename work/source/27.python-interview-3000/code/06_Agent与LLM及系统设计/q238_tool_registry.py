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
