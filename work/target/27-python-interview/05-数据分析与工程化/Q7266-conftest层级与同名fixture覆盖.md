---
title: "[Q7266] fixture 突然换了实现：conftest 层级与同名覆盖的解析顺序"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7266 · fixture 突然换了实现：conftest 层级与同名覆盖的解析顺序

难度：P5 ｜ 标签：pytest、conftest 层级、fixture 覆盖、解析顺序、测试基建

基线：Python 3.12；模拟 pytest 的 fixture 解析模型（从用例目录逐层向上找同名定义，最近者赢），复现层级覆盖与继承行为，全标准库实跑。

**问**：把一批用例从 `tests/api` 挪到 `tests/api/v2` 后，数据库 fixture 突然从 SQLite 变成了 MySQL，用例没改却大面积失败。pytest 的 fixture 解析顺序是什么？conftest.py 的层级覆盖规则是什么？这种"静默换实现"怎么防？

**答**：
- **结论**：pytest 的 fixture 解析是**从用例所在目录开始，沿 conftest.py 层级向上逐层查找同名定义，离用例最近的那层赢**：用例参数 → 用例所在文件 → 所在目录 conftest → 父目录 conftest → …… → rootdir 顶层 conftest → 已安装插件。同名 fixture 在低层定义即覆盖高层——这既是 feature（子目录定制自己的 DB 实现）也是事故源：**用例挪目录 = 静默换实现**，`tests/api` 下定义了 `db=MySQL`，挪进 `tests/api/v2` 后用例不再命中 api 层，回退到 root 层的 SQLite（或反过来），断言差异全爆在运行时。本卡的解析模型复现这一行为。防静默换实现：fixture 实例化时打日志（fixture 名 + 来源层 + 关键参数进测试输出），挪目录的 PR 里 diff fixture 覆盖关系。
- **取舍**：① conftest 层级的粒度：层级越多覆盖关系越复杂，团队规模下建议最多三层（root 公共 / 域目录 / 特例目录），再深就该用显式 fixture 参数化了（Q7238 组合爆炸）；② 覆盖 vs 继承：低层想"复用高层逻辑+微调"用 `request.getfixturevalue` 显式委托（Q1082）比重新实现一份好——同名覆盖是整替换，委托是增量；③ 插件fixture 与 conftest 的优先级：conftest 永远赢插件，排查"fixture 行为和文档不一致"先查本仓库有没有同名覆盖。
- **实战**：① fixture 名字带语义（`db_sqlite`/`db_mysql`）而不是全叫 `db`，用显式参数引用替代隐式覆盖；② 覆盖清单文档化：`grep -r "def db" tests/*/conftest.py` 的输出进 PR 模板；③ 挪目录/改层级的 PR 跑全量而非增量——fixture 覆盖是全局效应；④ CI 里加"fixture 漂移检测"：收集所有 conftest 的 fixture 名，同名跨层的列出来人工确认一次。

```python
"""Q7266 conftest 层级与同名 fixture 覆盖: 离测试最近的 conftest 赢。

模拟 pytest 的 fixture 解析: 从用例所在目录向上逐层找 conftest, 同名取最近定义。
"""
# 目录树: tests/conftest.py, tests/api/conftest.py, tests/api/v2/conftest.py
CONFTESTS = {
    "tests": {"db": "root-sqlite-memory", "auth": "real-stub"},
    "tests/api": {"db": "api-mysql-docker"},          # 覆盖 root 的 db
    "tests/api/v2": {},                                # 不覆盖任何
}


def resolve_fixture(test_dir: str, name: str) -> tuple[str, str]:
    """从用例目录逐层向上找同名 fixture, 返回 (值, 来源层)."""
    parts = test_dir.split("/")
    for i in range(len(parts), 0, -1):                 # 最近优先
        layer = "/".join(parts[:i])
        if name in CONFTESTS.get(layer, {}):
            return CONFTESTS[layer][name], layer
    raise KeyError(f"fixture {name!r} 未定义")


def fixtures_for(test_dir: str, names: list[str]) -> dict[str, tuple[str, str]]:
    return {n: resolve_fixture(test_dir, n) for n in names}


if __name__ == "__main__":
    for d in ("tests/api/v2", "tests/api", "tests"):
        r = fixtures_for(d, ["db", "auth"])
        print(f"{d:14s} -> " + ", ".join(f"{k}={v[0]}(来自 {v[1]})" for k, v in r.items()))

    ok = (resolve_fixture("tests/api/v2", "db") == ("api-mysql-docker", "tests/api")
          and resolve_fixture("tests", "db")[1] == "tests"
          and resolve_fixture("tests", "auth")[1] == "tests")
    print(f"校验: 最近层优先解析 -> {'通过' if ok else '异常'}")
    print("结论：同名 fixture 离用例最近的层赢, v2 不写 db 就继承 api 层的 mysql;")
    print("      跨层迁移用例时 fixture 实例会静默换实现——断言里带上来源层打日志")
```

**追问一**：fixture 的实例化时机和作用域（function/session）在层级解析中怎么叠加？为什么挪目录有时会让用例"莫名变快或变慢"？

→ 解析：解析决定"用哪个定义"，作用域决定"实例活多久"：session 级 fixture 全局一个实例，function 级每用例一个。叠加的坑在**同名跨层且作用域不同**：root 层 `db` 是 session 级（SQLite 建一次），api 层覆盖成 function 级（MySQL 每用例重建）——挪进 api 后用例每次都付建库成本，表现为"挪完变慢"；反向挪则可能共享了 session 级实例，用例之间通过这个实例**互相污染状态**（上一个用例写的数据被下一个看到），表现为"挪完莫名依赖执行顺序"。排查方法：`pytest --setup-plan` 或 `--setup-show` 显示每个 fixture 的作用域与实例化链，把"哪个层、什么作用域、谁先建"三个信息一起看。规则：同名覆盖时**作用域也要显式声明**，禁止靠继承隐式获得——作用域是并发与隔离的边界，隐式等于埋雷。

**追问二**：`request.getfixturevalue` 与同名覆盖怎么选？什么情况下覆盖是错的？

→ 解析：判据是"低层要不要高层 fixture 的逻辑"。同名覆盖 = 整替换：低层完全无视高层实现，适合"域级定制"（api 域用真 MySQL，root 默认 SQLite）。`getfixturevalue` = 显式组合：低层 fixture 内部先取高层的（比如 root 层的 `tmp_dir`），再在其上叠加自己的初始化——逻辑复用且依赖关系写在代码里可读。**覆盖用错**的典型信号：低层 fixture 90% 的代码是从高层复制来的——那是该用组合/参数化（Q7238）的信号，复制粘贴的 fixture 会在高层修 bug 时静默落后（修了 root 的连接池清理，api 层的副本还是坏的）。团队规则：**新增同名覆盖必须在 PR 里写一句"为什么不复用"**，这一句话能拦掉大部分复制式覆盖；覆盖是运维成本，默认选组合与显式参数。
