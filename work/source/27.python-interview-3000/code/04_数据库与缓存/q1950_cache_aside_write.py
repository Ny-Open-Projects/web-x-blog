"""旁路缓存写路径: 两种写顺序的竞态窗口时序模拟"""

class Store:
    def __init__(self):
        self.db = 10
        self.cache = 10        # 初始已缓存

def reader_miss_repair(s):
    """读路径未命中: 回源后把读到的值写回缓存"""
    s.cache = s.db
    return "读: 回源读到 %d 并写回缓存" % s.db

def steps_update_then_delete(new):
    """先更新库再删缓存"""
    return [("写1: 更新库", lambda s: setattr(s, "db", new)),
            ("写2: 删缓存", lambda s: setattr(s, "cache", None))]

def steps_delete_then_update(new):
    """先删缓存再更新库"""
    return [("写1: 删缓存", lambda s: setattr(s, "cache", None)),
            ("写2: 更新库", lambda s: setattr(s, "db", new))]

def interleave(order_steps, reader_at):
    """reader_at 指定在写者第几步之后插入一次未命中读"""
    s = Store()
    log = []
    for i, (name, fn) in enumerate(order_steps):
        fn(s)
        log.append(name)
        if reader_at == i:
            log.append(reader_miss_repair(s))
    if reader_at is not None and reader_at >= len(order_steps):
        log.append(reader_miss_repair(s))
    return s, log

for order_name, factory in [("先更库再删缓存", steps_update_then_delete),
                            ("先删缓存再更库", steps_delete_then_update)]:
    for reader_at in (0, 1, 2):
        s, log = interleave(factory(20), reader_at if reader_at < 2 else None)
        pos = "写第%d步后" % (reader_at + 1) if reader_at < 2 else "写完之后"
        if s.cache is None:
            verdict = "缓存已失效 下次读回源"
        elif s.cache == s.db:
            verdict = "一致"
        else:
            verdict = "陈旧!"
        print(f"{order_name} 读插在{pos} -> db={s.db} cache={s.cache} {verdict}")

# 残余竞态: 读者在写开始前回源拿到旧值 醒来后才写回缓存 两种顺序都会中招
s = Store()
pending = s.db                      # 读者拿到旧值 10 后卡住
for name, fn in steps_update_then_delete(20):
    fn(s)
s.cache = pending                   # 读者醒来把旧值写回
print(f"慢读者残余竞态 -> 库已是 20 缓存被写回旧值 {s.cache} 永久陈旧 只能靠短 TTL 或延迟双删收敛")
print("结论: 先更库再删缓存是四种顺序里竞态窗口最小的 残余风险由 TTL 兜底")
