from typing import Callable, Protocol


class Exporter(Protocol):
    def export(self, data: dict) -> str: ...


_REGISTRY: dict[str, Callable[[], Exporter]] = {}


def register(name: str):
    """装饰器注册:新插件只需 import 本文件并加装饰器。"""
    def deco(factory: Callable[[], Exporter]):
        _REGISTRY[name] = factory
        return factory
    return deco


def create_exporter(name: str) -> Exporter:
    if name not in _REGISTRY:
        raise KeyError(f"unknown exporter: {name}")
    return _REGISTRY[name]()


@register("json")
class JsonExporter:
    def export(self, data: dict) -> str:
        import json
        return json.dumps(data)


@register("csv")
class CsvExporter:
    def export(self, data: dict) -> str:
        return ",".join(f"{k}={v}" for k, v in data.items())


if __name__ == "__main__":
    print(create_exporter("json").export({"a": 1}))
    print(create_exporter("csv").export({"a": 1}))
