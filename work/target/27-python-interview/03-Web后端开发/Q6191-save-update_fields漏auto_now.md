---
title: "[Q6191] save(update_fields=...) 漏掉 auto_now：时间戳永远不更新"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6191 · save(update_fields=...) 漏掉 auto_now：时间戳永远不更新

难度：P6 ｜ 标签：Django、update_fields、auto_now、pre_save、信号、部分更新

**问**：为了减少写放大，保存时统一加 `save(update_fields=["status"])`，上线后发现所有记录的 `updated_at` 再也不变了，缓存按 `updated_at` 做的增量同步全部失效。`update_fields` 到底限制了什么？`auto_now` 是不是"保存就自动更新"？信号里拿到的 `update_fields` 是什么形态、能拿到旧值吗？

**答**：
结论：`update_fields` 是"**只写这些列**"的白名单，不是"只校验这些字段"。Django 的 `Model.save()` 会把它传给 `pre_save`，每个字段的 `pre_save` 决定是否把自己加进最终 SQL 的列集合；`auto_now`/`auto_now_add` 不是"保存钩子无条件执行"，而是"该字段被包含在这次写入里时才赋值"。所以 `update_fields=["status"]` 时 `updated_at` 根本不在列集合里，既不会被赋值也不会被写库。传 `update_fields=[]` 更极端：直接跳过所有写入（相当于 no-op），但仍会触发 `pre_save`/`post_save` 信号。

取舍：a) 需要 `updated_at` 时把它显式加进白名单，或者写一个小工具函数统一补 `{"updated_at"}`；b) 更好的做法是用数据库侧的 `ON UPDATE CURRENT_TIMESTAMP` 或触发器，让"部分更新"不影响时间戳——但这会把逻辑分散到 DB，迁移与测试要一起管；c) 不要用 `save(update_fields=...)` 做并发控制，它不检查版本，两个请求的字段集合不同时后写覆盖前写；需要乐观锁就加 `version` 字段并 `filter(version=...).update(...)`。

实战：事故形态是"运营后台批量改状态，增量同步任务按 `updated_at > last_sync` 拉数据，改完状态后时间戳没动，下游永远看不到变化；排查时发现 ORM 的 UPDATE 语句里只有一列"。下面用纯 Python 模拟 Django 的 `pre_save` 白名单语义，演示漏字段、显式补字段、以及信号里 `update_fields` 的形态。

```python
AUTO_NOW = {"updated_at"}


class Model:
    fields = ("name", "status", "updated_at")

    def __init__(self, name, status, updated_at="t0"):
        self.name, self.status, self.updated_at = name, status, updated_at


def pre_save(instance, update_fields, now="t1"):
    """模拟 Django 的 pre_save：只处理本次要写的列。"""
    if update_fields is None:
        targets = set(Model.fields)
    else:
        targets = set(update_fields)
    if "updated_at" in targets:
        instance.updated_at = now
    return targets


def save(instance, update_fields=None, now="t1"):
    written = pre_save(instance, update_fields, now)
    return written


obj = Model("a", "new")
written = save(obj, ["status"])
print("[1] update_fields=['status'] 实际写列:", sorted(written))
print("    updated_at 是否变化:", obj.updated_at)

obj2 = Model("a", "new")
written2 = save(obj2, ["status", "updated_at"])
print("[2] 显式补 updated_at:", sorted(written2), obj2.updated_at)

obj3 = Model("a", "new")
print("[3] update_fields=[] 跳过写入:", sorted(save(obj3, [])), obj3.updated_at)

# 信号里 update_fields 的形态：None 或 frozenset，不是 list
def post_save(instance, created, update_fields):
    return update_fields


print("[4] 信号收到 None:", post_save(obj, False, None))
print("[5] 信号收到 frozenset:", post_save(obj, False, frozenset(["status"])))
print("[6] 信号里拿不到旧值：pre_save 之前字段已被读入实例，需自己查库或缓存")
```

**追问一**：`update_fields` 里的字段名写错了会怎样？—— Django 不校验，直接拼进 SQL，结果是 `UPDATE ... SET wrong_col = ...` 由数据库报错（`OperationalError: no such column`）。更隐蔽的是传了不在模型上的字段但数据库恰好有同名列（比如遗留列），会静默写错列。工程上应在模型层做常量或在 CI 里跑"字段白名单"检查，别让字符串散落在业务代码里。

**追问二**：`update_fields` 能触发 `post_save` 里的"旧值对比"逻辑吗？—— 不能，信号拿到的是"已修改的实例"和 `update_fields`，旧值需要额外查询或使用 `refresh_from_db` 之前先读。很多审计逻辑误以为 `pre_save` 能拿到 both old/new，实际 Django 的 `pre_save` 只有 instance；要做字段级审计，得在业务层先 `select_for_update` 读出旧行，再比较，或者用数据库触发器/CDC。

## 背诵要点
- `update_fields` 是"只写这些列"的白名单；不在集合里的列（含 `auto_now`）完全不参与赋值与写库。
- `update_fields=[]` 跳过写入但仍发信号；信号里是 `None` 或 `frozenset`，且没有旧值。
- `updated_at` 要么显式加入白名单，要么交给数据库 `ON UPDATE`；`update_fields` 不提供并发控制。

## 复盘追问
- 批量改状态后增量同步永远拉不到，如何定位到 `update_fields`？（UPDATE 列集合、auto_now 赋值条件）
- 为什么 `update_fields` 不能替代乐观锁？（无版本校验、字段集合不同会互相覆盖）
