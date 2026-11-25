---
title: "[Q7238] fixture params 乘上 parametrize：3 个夹具把 12 个用例变成 720 个"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7238 · fixture params 乘上 parametrize：3 个夹具把 12 个用例变成 720 个

难度：P6 ｜ 标签：pytest、parametrize、fixture params、组合爆炸

基线：Python 3.12；用 `itertools.product` 复现 pytest 的笛卡尔积展开规则。

**问**：一个接口测试写了 `@pytest.mark.parametrize` 4 个业务场景，又用了三个带 `params` 的 fixture（`db` 2 种、`cache` 3 种、`auth` 5 种）。本地用 fake 只跑 4 个业务场景 40 秒，CI 上同一个文件却跑了 120 个用例、26 分钟。后来加了一个 `region` fixture（4 种），用例变成 480 个、1 小时 44 分。明明只加了 4 个"环境组合"，为什么是指数增长？

**答**：
- **结论**：pytest 对 `parametrize` 和 fixture 的 `params` 做的是**笛卡尔积**，不是"按需组合"：用例数 = 参数化用例数 × Π(每个 fixture 的 params 数量)。4 × 2 × 3 × 5 = 120，再加 4 就变成 480。每个组合都是一次独立的 setup/teardown，fixture 的作用域只能减少"同组合内"的重复，**不能减少组合数**。这就是"加一个维度，成本乘上去"。
- **取舍**：三条降维策略：① **分层**：契约/逻辑测试用 `fake` 替身跑全业务场景（4 个），只有少量"冒烟"用例才跑真实矩阵（db × cache）；② `indirect=True` 让 fixture 参数只在**声明了它的用例**上生效，而不是全局扩散；③ 用 `pytest.param(..., marks=pytest.mark.slow)` 标记高成本组合，PR 阶段 `-m "not slow"` 只跑代表性子集， nightly 跑全矩阵。
- **实战**：① CI 里打印用例总数并设阈值（比如单文件 > 200 就告警），把"组合爆炸"变成可见的指标；② 用 `--durations=20` 找最慢的组合，通常是某个 fixture 的 setup（建库/起容器）在重复；③ 环境矩阵（db/cache/region）本质是"部署维度"，更适合用 docker-compose 起一套环境跑一遍，而不是在 pytest 里排列组合；④ 记住 `scope="session"` 只省 setup 时间，不省用例数。

```python
"""parametrize × fixture params 的笛卡尔积：算清成本再决定怎么砍。"""
from itertools import product

FIXTURES = {
    "db": ["sqlite", "pg"],
    "cache": ["none", "redis", "local"],
    "auth": ["jwt", "session", "oauth", "apikey", "anonymous"],
}
SCENARIOS = [("ok", 200), ("empty", 200), ("denied", 403), ("timeout", 504)]
SECONDS_PER_CASE = 13.0


def expand(fixtures: dict[str, list[str]], scenarios: list[tuple[str, int]]):
    keys = list(fixtures)
    combos = list(product(*fixtures.values()))
    return [(dict(zip(keys, combo)), sc) for combo in combos for sc in scenarios]


def count(fixtures: dict[str, list[str]], n_scenarios: int) -> int:
    total = n_scenarios
    for values in fixtures.values():
        total *= len(values)
    return total


if __name__ == "__main__":
    cases = expand(FIXTURES, SCENARIOS)
    print("组合数:", len(cases), "= 4 场景 × 2 db × 3 cache × 5 auth")
    print("预计耗时: %.1f 分钟" % (len(cases) * SECONDS_PER_CASE / 60))

    with_region = dict(FIXTURES, region=["cn", "us", "eu", "sg"])
    n = count(with_region, len(SCENARIOS))
    print("再加 region(4):", n, "个用例，%.0f 分钟"
          % (n * SECONDS_PER_CASE / 60))

    # 降维 1：环境维度只在冒烟用例上展开
    smoke = [("ok", 200)]
    smoke_cases = expand(FIXTURES, smoke)
    print("\n冒烟矩阵:", len(smoke_cases), "个（环境全展开，业务只跑 ok）")

    # 降维 2：业务场景用 fake 跑全量，不乘环境
    fake_cases = [(None, sc) for sc in SCENARIOS]
    print("fake 全场景:", len(fake_cases), "个（不乘环境）")
    print("合计:", len(smoke_cases) + len(fake_cases), "个 vs 原", len(cases))

    # 降维 3：indirect 让参数只在声明的用例上生效
    indirect_cases = [
        ({"db": db}, ("ok", 200)) for db in FIXTURES["db"]
    ] + [(None, sc) for sc in SCENARIOS]
    print("indirect 选择性展开:", len(indirect_cases), "个")

    print("\n增长曲线:")
    for regions in range(0, 5):
        f = dict(FIXTURES)
        if regions:
            f["region"] = [f"r{i}" for i in range(regions + 1)]
        n = count(f, len(SCENARIOS))
        print(f"  region 维度 {regions}: {n:>4} 个用例, "
              f"{n * SECONDS_PER_CASE / 60:>6.1f} 分钟")
    print("结论：环境矩阵交给部署流水线，pytest 只保留代表性组合")
```

**追问一**：`scope="session"` 的 fixture 能缓解组合爆炸吗？

→ 解析：只能减少 **setup 次数**，不减少用例数。比如 `db` fixture 是 session 作用域时，2 种 db 各建一次引擎，120 个用例共享；但如果 setup 本身就是瓶颈（起容器、灌 10 万行数据），收益很大；如果每个用例的**执行**（HTTP 往返、断言）才是成本，作用域没用。判断方法看 `--durations`：setup 占比高就调作用域，call 占比高就只能减组合。

**追问二**：`indirect=True` 到底改变了什么？

→ 解析：普通 `@pytest.mark.parametrize("db", ["sqlite","pg"])` 如果 `db` 同时是 fixture 名，pytest 会要求 `indirect`，语义是"把参数传给 fixture 的 `request.param`，由 fixture 决定怎么用"，而不是直接覆盖测试函数参数。正确的用法是：**只在需要换环境的用例上写这个 parametrize**，让它成为该用例的局部维度；写成模块级 `pytestmark` 就退化成全局扩散，又回到指数爆炸。配合 `pytest.param(..., marks=...)` 能给单个组合打标，做"PR 快跑 / nightly 全跑"的分层。
