"""双写顺序实测: 四种写策略在并发写者交错下的终态"""

def run_two_writers(steps_fn):
    """写者 A 写 X 写者 B 写 Y 交错顺序固定为 A1 B1 B2 A2"""
    state = {"db": "old", "cache": "old"}
    a = steps_fn("X")
    b = steps_fn("Y")
    for fn in [a[0]] + b + a[1:]:
        fn(state)
    return state

def cache_then_db(v):
    return [lambda s, v=v: s.__setitem__("cache", v),
            lambda s, v=v: s.__setitem__("db", v)]

def db_then_cache(v):
    return [lambda s, v=v: s.__setitem__("db", v),
            lambda s, v=v: s.__setitem__("cache", v)]

def db_then_del(v):
    return [lambda s, v=v: s.__setitem__("db", v),
            lambda s, v=v: s.__setitem__("cache", "GONE")]

def del_then_db(v):
    return [lambda s, v=v: s.__setitem__("cache", "GONE"),
            lambda s, v=v: s.__setitem__("db", v)]

for name, fn in [("先更缓存再更库", cache_then_db),
                 ("先更库再更缓存", db_then_cache),
                 ("先更库再删缓存", db_then_del),
                 ("先删缓存再更库", del_then_db)]:
    s = run_two_writers(fn)
    if s["cache"] == "GONE":
        verdict = "缓存失效 下次读回源修复 可接受"
    elif s["cache"] == s["db"]:
        verdict = "一致"
    else:
        verdict = "永久不一致"
    print(f"{name}: db={s['db']} cache={s['cache']} -> {verdict}")
print("结论: 并发写者交错下 更新缓存类策略终态直接脏 删缓存类策略把不一致收敛成一次未命中 所以写路径用删除")
