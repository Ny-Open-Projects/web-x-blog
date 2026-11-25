---
title: "[Q6708] SET LOCAL 事务级 GUC 与连接池串味复盘"
date: 2026-11-23
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6708 · SET LOCAL 事务级 GUC 与连接池串味复盘

难度：P6 ｜ 标签：事故复盘、PostgreSQL、连接池、GUC

基线：Python 3.12；PostgreSQL 12+；纯 Python 模拟连接池 GUC 泄漏。

**问**：多租户应用用了连接池。某次事故里，A 租户的请求设置 `search_path` 指向自己的 schema 后没恢复，下一个复用该连接的 B 租户请求读到了 A 的数据（越权）。`SET` 和 `SET LOCAL` 在这里差在哪？怎么从机制上根治？

**答**：
- **结论**：`SET` 是**会话级**修改，连接池复用物理连接时，会话级 GUC 会跟着连接传给下一个请求——这就是"串味"的根源。`SET LOCAL` 是**事务级**修改，只在当前事务内生效，事务结束（COMMIT/ROLLBACK）自动恢复原值，因此不会跨请求泄漏。前提是它必须运行在显式事务块里；若连接处于 autocommit，`SET LOCAL` 的有效期只到当前语句，几乎立刻失效。
- **取舍**：需要跨事务持续生效的设置（如 `statement_timeout`、`application_name`）只能用 `SET`，那就必须在连接归还池时重置（`pool_reset_query` / SQLAlchemy 的 `reset_on_return`）。能用 `SET LOCAL` 的（租户 schema、搜索路径、临时时区）优先用它，把生命周期绑在事务上最省心。
- **实战**：把租户上下文设置全部包进事务并用 `SET LOCAL`；为连接池配置归还时重置脚本并定期审计；用 `current_setting('search_path')` 在请求入口断言租户隔离；把这类"连接复用导致的状态残留"列入越权测试矩阵。

```python
class ConnPool:
    """模拟连接池：GUC 是会话级状态，请求间会复用。"""

    def __init__(self) -> None:
        self.guc: dict[str, str] = {"search_path": "public"}

    def run_with_local(self, path: str) -> str:
        old = self.guc["search_path"]
        try:
            self.guc["search_path"] = path       # SET LOCAL 语义
            return self.guc["search_path"]
        finally:
            self.guc["search_path"] = old        # 事务结束自动恢复

    def run_with_global(self, path: str) -> str:
        self.guc["search_path"] = path           # SET 会话级，污染后续请求
        return self.guc["search_path"]


if __name__ == "__main__":
    pool = ConnPool()
    print("local:", pool.run_with_local("tenant_a"), "->", pool.guc["search_path"])
    print("global:", pool.run_with_global("tenant_b"), "->", pool.guc["search_path"])
    print("next request sees:", pool.guc["search_path"])
```

**追问一**：autocommit 模式下用 `SET LOCAL` 会怎样？
→ 解析：`SET LOCAL` 的生命周期是当前事务；autocommit 下每条语句自成事务，语句结束就恢复，所以它几乎立即失效。要用 `SET LOCAL` 必须显式开启事务块。

**追问二**：除了 search_path，还有哪些 GUC 容易引发串味？
→ 解析：`statement_timeout`、`work_mem`、`role`（SET ROLE）、`timezone`、`row_security` 等。凡是会话级且影响数据可见性/权限的，都要纳入重置或改用事务级设置。
