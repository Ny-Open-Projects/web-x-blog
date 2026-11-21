from dataclasses import dataclass


@dataclass(frozen=True)
class DbConfig:
    host: str
    port: int
    replicas: tuple = ()


@dataclass(frozen=True)
class AppConfig:
    app_name: str
    db: DbConfig
    features: tuple = ()


def build_config(raw):
    # 工厂边界:类型转换 + 拷贝,与原始 dict 脱钩
    return AppConfig(
        app_name=str(raw["app_name"]),
        db=DbConfig(
            host=str(raw["db"]["host"]),
            port=int(raw["db"]["port"]),
            replicas=tuple(raw["db"].get("replicas", ())),
        ),
        features=tuple(raw.get("features", ())),
    )


if __name__ == "__main__":
    raw = {"app_name": "svc", "db": {"host": "db1", "port": 5432,
                                     "replicas": ["db2"]}}
    cfg = build_config(raw)
    raw["db"]["port"] = 9999             # 改原始输入,不影响 cfg
    print("config stable:", cfg.db.port)
    try:
        cfg.db.port = 1234
    except Exception as e:
        print(type(e).__name__, "->", e)
    print("features tuple:", cfg.features)
