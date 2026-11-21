"""自定义 ABC:__subclasshook__ 结构判定与 register 虚拟子类。"""
from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def export(self, data):
        ...

    @classmethod
    def __subclasshook__(cls, other):
        if cls is Exporter and hasattr(other, "export"):
            return True                        # 结构判定认得,直接拍板
        return NotImplemented                  # 拿不准:交还注册表与常规检查


class CsvExporter(Exporter):
    def export(self, data):
        return ",".join(map(str, data))


class ThirdParty:
    """不能修改源码的第三方类,但恰好有 export。"""

    def export(self, data):
        return str(data)


class LegacyAdapter:
    """方法名不匹配 hook;团队用 register 做承诺性注册。"""

    def dump(self, data):
        return str(data)


Exporter.register(LegacyAdapter)


class NotAnExporter:
    pass


if __name__ == "__main__":
    print("常规子类:", issubclass(CsvExporter, Exporter))
    print("hook 结构判定(未注册未继承):", issubclass(ThirdParty, Exporter))
    print("注册后判定:", issubclass(LegacyAdapter, Exporter))
    print("注册后 isinstance:", isinstance(LegacyAdapter(), Exporter))
    print("无关类:", issubclass(NotAnExporter, Exporter))
    try:
        Exporter()
    except TypeError as e:
        print("抽象类实例化被拦:", str(e)[:42])
