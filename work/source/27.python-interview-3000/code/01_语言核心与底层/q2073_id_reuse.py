"""id 复用陷阱:对象死亡后其 id 会被新对象复用。"""
import gc


def make_text(n):
    return "x" * n                 # 运行时构造,每次都是新对象


if __name__ == "__main__":
    dead = make_text(64)
    dead_id = id(dead)
    del dead
    gc.collect()

    alive = make_text(64)          # 同尺寸分配,CPython 大概率复用刚释放的块
    reused = id(alive) == dead_id
    print("新对象复用了旧 id:", reused)

    identity_cache = {dead_id: "旧对象元数据"}     # 错误示范:id 当键但不持引用
    if reused:
        print("身份缓存串号:", identity_cache.get(id(alive)))
    else:
        print("本次未复现复用,但机制上不保证——这正是问题所在")

    safe = {id(dead := make_text(64)): dead}       # 正确姿势:身份连同对象一起存
    print("带强引用的身份表可安全反查:", type(safe[id(dead)]).__name__)
