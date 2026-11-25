---
title: "[Q7230] --lf 只跑上次失败的 3 个用例：CI 绿了，200 个用例根本没跑"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7230 · --lf 只跑上次失败的 3 个用例：CI 绿了，200 个用例根本没跑

难度：P7 ｜ 标签：pytest、--lf、lastfailed 缓存、CI 门禁

基线：Python 3.12；pytest 8.x `--lf`/`--ff`/`--cache-clear`/`-p no:cacheprovider`；纯 Python 模拟收集与缓存选择。

**问**：CI 为了省时间加了 `pytest --lf`。某次修完上线，本地全绿，推上去 CI 只跑了 3 个用例就绿了，合并后才发现另外 12 个用例是挂的。`--lf` 不是"上次失败的优先跑"吗，怎么会把没跑过的用例整套跳过？

**答**：
- **结论**：`--lf`（last-failed）读 `.pytest_cache/v/cache/lastfailed`，**只收集上次失败/报错的用例**，其余用例连收集都不发生（所以是"只跑"，不是"优先"）。缓存文件如果在 workspace 被 CI 缓存、或被提交进仓库，就会跨构建残留；`--lf` 在上次全绿时又会退化成"跑全部"（lastfailed 为空则全跑），于是表现为"有时只跑 3 个、有时全跑"。
- **取舍**：`--lf` 适合**本地开发**快速回归，不适合当 CI 门禁——它用覆盖率换速度，还依赖一个可被污染的缓存文件。CI 要提速应该用 `-m "not slow"` 分级、`--durations` 找慢用例、xdist 并行，或基于依赖图的增量选择（pytest-testmon），而不是跳过用例。
- **实战**：① CI 禁止 `--lf`/`--ff`，只允许本地个人使用；② `.pytest_cache` 进 `.gitignore` 且不进 CI 缓存 key；③ CI 断言收集数不低于基线（`pytest --collect-only -q | tail -1`）；④ 用增量工具时必须校验"未选中数"并明确记录；⑤ 关键分支保护用 required checks，不要让它跑到零用例还算通过。

```python
"""--lf 的选择语义：只取上次失败集；全绿时退化为全跑。"""
import json
import os


def collect(all_tests: list[str], cache: dict, mode: str | None) -> list[str]:
    lastfailed = list(cache.get("lastfailed", {}))
    if mode == "lf":
        if not lastfailed:
            return list(all_tests)          # 上次全绿 => 退化为全跑
        return [t for t in all_tests if t in set(lastfailed)]
    if mode == "ff":
        ordered = [t for t in all_tests if t in set(lastfailed)]
        ordered += [t for t in all_tests if t not in set(lastfailed)]
        return ordered                      # 全跑，但失败优先
    return list(all_tests)


def run(selected: list[str], failing: set[str]) -> tuple[int, int]:
    failed = [t for t in selected if t in failing]
    return len(selected), len(failed)


if __name__ == "__main__":
    all_tests = [f"test_{i:03d}" for i in range(200)]

    # 第一次：3 个失败，缓存被写进 workspace
    cache = {"lastfailed": {"test_007": True, "test_042": True, "test_199": True}}
    cache_path = "/tmp/demo_pytest_cache.json"
    with open(cache_path, "w") as f:
        json.dump(cache, f)
    print("缓存已落盘:", cache_path)

    # 第二次：CI 复用了缓存，--lf 只收集 3 个
    loaded = json.load(open(cache_path))
    sel = collect(all_tests, loaded, "lf")
    print("--lf 收集:", len(sel), sel)

    # 其余 197 个里还有 12 个是挂的 —— 但根本没收集
    silent_failures = {f"test_{i:03d}" for i in range(0, 192, 16)}
    total, failed = run(sel, silent_failures)
    print("本轮执行:", total, "失败:", failed, "-> CI 绿")
    print("未收集但实际失败:", len(silent_failures - set(sel)), "个")

    # 上次全绿的退化行为
    print("缓存为空时 --lf 收集:", len(collect(all_tests, {}, "lf")), "-> 全跑")

    # --ff：全跑，失败优先
    ff = collect(all_tests, loaded, "ff")
    print("--ff 收集:", len(ff), "| 前 3 个:", ff[:3])

    os.remove(cache_path)
    print("结论：--lf 是跳过而非优先；CI 门禁必须校验收集数，缓存文件不许跨构建")
```

**追问一**：`--ff`（failed-first）和 `--lf` 的区别？
→ 解析：`--ff` 跑**全部**用例，只是把上次失败的排前面（失败早暴露、早失败早结束）；`--lf` 只跑失败的。CI 用 `--ff` 不会漏用例，但仍受缓存污染影响执行顺序与耗时。

**追问二**：`--cache-clear` 和 `-p no:cacheprovider` 有什么区别？
→ 解析：`--cache-clear` 在本次运行**开始前**清空缓存目录，但本次仍会写入新缓存；`-p no:cacheprovider` 完全禁用缓存插件（不读也不写），`--lf` 会因此失效或直接报错。CI 里要"绝不使用缓存"应该用后者，且不要给它传 `--lf`。
