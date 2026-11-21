"""frozen dataclass 的保护机制与两条逃生门。"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    host: str
    port: int


if __name__ == "__main__":
    cfg = Config("db1", 5432)

    try:
        cfg.port = 1
    except Exception as exc:
        print("常规赋值被拦:", type(exc).__name__, exc)

    object.__setattr__(cfg, "port", 15432)     # 逃生门一:object 层赋值
    print("object.__setattr__ 后:", cfg.port)

    cfg.__dict__["port"] = 15433               # 逃生门二:直写实例字典
    print("__dict__ 直写后:", cfg.port, cfg)

    try:
        hash(cfg)
        print("frozen 实例可哈希:", hash(cfg) is not None)
    except TypeError as exc:
        print("不可哈希:", exc)
