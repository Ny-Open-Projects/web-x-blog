"""dataclasses.replace:冻结对象的派生修改。"""
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Config:
    host: str = "localhost"
    port: int = 8000
    debug: bool = False


def promote_debug(cfg):
    return replace(cfg, debug=True)          # 返回新实例,原对象不动


def bump_port(cfg, delta=1):
    return replace(cfg, port=cfg.port + delta)


def unknown_field_check(cfg):
    try:
        replace(cfg, nope=1)
    except TypeError as e:
        return str(e)[:44]
    return "没有报错?"


if __name__ == "__main__":
    base = Config()
    prod = bump_port(promote_debug(base), delta=1000)
    print("原对象:", base)
    print("派生对象:", prod)
    print("frozen 不可写:", end=" ")
    try:
        base.port = 1
    except Exception as e:
        print(type(e).__name__)
    print("未知字段报错:", unknown_field_check(base))
