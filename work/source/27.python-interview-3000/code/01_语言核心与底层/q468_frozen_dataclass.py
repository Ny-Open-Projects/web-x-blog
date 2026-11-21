from dataclasses import dataclass, field, replace, FrozenInstanceError

@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080
    tags: tuple = field(default_factory=tuple)   # frozen 也要配不可变容器

if __name__ == "__main__":
    c = Config("db.local", tags=("primary",))
    print(c)
    print("hashable:", hash(c) is not None)
    try:
        c.port = 9090
    except FrozenInstanceError as e:
        print("immutable:", e)
    c2 = replace(c, port=9090)            # 修改 = 派生新实例
    print(c2)
    print({c: "main", c2: "standby"})     # 可作 dict key
    print("same tags object:", c.tags is c2.tags)   # 浅共享:tuple 本身不可变才安全
