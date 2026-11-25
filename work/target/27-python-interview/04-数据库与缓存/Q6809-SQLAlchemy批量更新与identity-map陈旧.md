---
title: "[Q6809] SQLAlchemy 批量更新后 identity map 里还是旧对象"
date: 2026-11-25
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6809 · SQLAlchemy 批量更新后 identity map 里还是旧对象

难度：P7 ｜ 标签：SQLAlchemy、identity map、synchronize_session、批量更新、缓存一致性

基线：库知识库外知识卡，用纯 Python 模拟 SQLAlchemy `Session` 的 identity map 与 `Query.update(synchronize_session=...)` 的三种策略。

**问**：会员余额用 `session.query(Account).filter(...).update({"balance": new_balance}, synchronize_session=False)` 批量调账，紧接着在同一个事务里用 `session.get(Account, uid)` 读余额算优惠券额度，结果读到的是调账前的旧值，多发 3.2 万张券。数据库里明明是新的，为什么 ORM 还给我旧对象？`synchronize_session` 的 `False`/`evaluate`/`fetch` 到底差在哪？批量更新后应该怎么读？

**答**：

- **结论**：SQLAlchemy 的 `Session` 有一层 **identity map**：同一个主键在会话内只对应一个 Python 对象。`Query.update()` 默认发的是**批量 UPDATE SQL**，不经过 ORM 的对象加载路径，数据库行改了，但 identity map 里的对象还是旧属性。`synchronize_session=False` 明确告诉 Session"别管缓存"，于是后续 `session.get()` 直接返回缓存对象，读到旧值。`evaluate` 会在 Python 里对缓存对象求值并同步属性（只支持简单表达式）；`fetch` 会先 `SELECT` 出受影响主键再让相关对象过期，代价是多一次查询。三者不是"性能开关"，是**缓存一致性策略**。
- **取舍**：① `False` 最快，适合"批量更新后不再读这些对象"的场景（如离线批处理、更新完就提交退出）；② `evaluate` 零额外查询，但表达式复杂（函数、子查询、跨表）时回退或报错，适合简单过滤；③ `fetch` 最稳，额外一次主键查询，适合更新后还要在同一个 Session 里读对象；④ 更彻底的做法是 `session.expire_all()` 或提交后重新开事务读，但要注意 `expire_on_commit=False` 会让对象在提交后仍不过期。
- **实战**：① 批量更新后要读，优先 `synchronize_session="fetch"`，或显式 `session.expire(obj)`；② 批量任务与在线读分离，批量更新走独立 Session/独立事务，别在同一请求里混用；③ 代码评审重点看 `synchronize_session=False` 后面有没有 `session.get/query`；④ 用 `session.is_modified(obj)` 与 `obj in session.dirty` 辅助排查"为什么没发 UPDATE"。

下面模拟三种策略：同一个对象，批量更新后读到的余额不同。

```python
# identity map: 批量 UPDATE 绕过 ORM, 缓存对象是否同步取决于 synchronize_session
class Session:
    def __init__(self, table):
        self.table = dict(table)          # 数据库行
        self.identity = {}                # pk -> 对象

    def get(self, pk):
        if pk not in self.identity:
            self.identity[pk] = {"pk": pk, "balance": self.table[pk]}
        return self.identity[pk]

    def bulk_update(self, pk, value, synchronize_session):
        self.table[pk] = value
        if synchronize_session == "evaluate" and pk in self.identity:
            self.identity[pk]["balance"] = value
        elif synchronize_session == "fetch":
            self.identity.pop(pk, None)   # 标记过期, 下次 get 重新加载


table = {1: 100}

s_false = Session(table)
obj_false = s_false.get(1)
s_false.bulk_update(1, 50, synchronize_session=False)
print(f"[1] False: 数据库={s_false.table[1]}, 缓存对象={obj_false['balance']}, "
      f"再 get={s_false.get(1)['balance']}")
assert s_false.table[1] == 50 and obj_false["balance"] == 100
assert s_false.get(1)["balance"] == 100, "False 不同步, 读到旧值"

s_eval = Session(table)
obj_eval = s_eval.get(1)
s_eval.bulk_update(1, 30, synchronize_session="evaluate")
print(f"[2] evaluate: 数据库={s_eval.table[1]}, 缓存对象={obj_eval['balance']}")
assert obj_eval["balance"] == 30

s_fetch = Session(table)
obj_fetch = s_fetch.get(1)
s_fetch.bulk_update(1, 20, synchronize_session="fetch")
print(f"[3] fetch: 数据库={s_fetch.table[1]}, 旧对象={obj_fetch['balance']}, "
      f"再 get={s_fetch.get(1)['balance']}")
assert obj_fetch["balance"] == 100, "旧对象不会原地更新, 只是被过期"
assert s_fetch.get(1)["balance"] == 20

# expire_on_commit=False: 提交后对象仍不过期, 跨事务继续读到旧值
def commit(session, expire_on_commit):
    if expire_on_commit:
        session.identity.clear()


s_commit = Session(table)
obj_commit = s_commit.get(1)
s_commit.bulk_update(1, 10, synchronize_session=False)
commit(s_commit, expire_on_commit=False)
print(f"[4] expire_on_commit=False: 提交后读={s_commit.get(1)['balance']}")
assert s_commit.get(1)["balance"] == 100
print("    → 实测 False 不碰缓存; fetch 只过期不原地改; 提交策略决定跨事务是否还旧")
```

**追问一**：为什么 `synchronize_session=False` 不是"默认更快的等价选项"？—— 它等价于"我保证批量更新后不在这个 Session 里读受影响对象"。一旦读了，就是缓存与数据库分叉，而且不会报错，是最难排查的一类 bug。把它当性能优化随手加，等于用正确性换几毫秒。只有批量任务"更新完就结束"时才安全。

**追问二**：`session.expire_all()` 之后，为什么有时读到的还是旧值？—— 可能处在 `REPEATABLE READ` 事务里，过期只会重新 `SELECT`，但事务快照仍是旧的；也可能 `expire_on_commit=False` 且没有真正重新查询。`expire` 解决的是"ORM 缓存"，不解决"数据库隔离级别快照"。两者要分开看。

## 背诵要点

- `Query.update()` 走批量 SQL，不改 identity map；`synchronize_session=False` 后同 Session 读对象会拿到旧值。
- `evaluate` 在 Python 侧同步简单表达式，`fetch` 先查主键再过期对象（多一次查询），`False` 完全不管。
- 批量更新后要读：用 `fetch` 或显式 `expire`；批量任务与在线读用不同 Session/事务；注意 `expire_on_commit` 与 RR 快照。

## 复盘追问

- `evaluate` 遇到 `func.lower(col) == 'x'` 这类表达式会怎样？为什么它不能覆盖所有 WHERE？
- 如果批量更新和后续读必须在同一事务里，怎样既保证一致性又不引入额外主键查询？
