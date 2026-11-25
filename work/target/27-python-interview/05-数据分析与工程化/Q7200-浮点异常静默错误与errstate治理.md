---
title: "[Q7200] 浮点异常静默错误与 errstate 治理"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7200 · 浮点异常静默错误与 errstate 治理

难度：P6 ｜ 标签：事故复盘、数值稳定性、numpy、数据质量

基线：Python 3.12；numpy `np.errstate` / `np.seterr`；标准库演示等价语义。

**问**：一段向量化特征计算偶发产出 `nan`，排查发现是某次除零、负数开方。奇怪的是程序没崩，只偶尔有条 warning，坏值一路流进模型。怎么把这类"静默数值错误"变成可观测、可拦截的失败？

**答**：
- **结论**：numpy 对浮点异常（divide / invalid / over / under）默认策略是 `warn`——打印 `RuntimeWarning` 但不中断，结果继续向下游流。`np.errstate(divide='raise', invalid='raise', over='raise')` 作为上下文管理器，可把指定异常升级为真异常；`np.seterr(all='raise')` 则全局开启。关键取舍：全局 raise 会让"合法产生 inf/nan"的计算（如掩码后除零、缺失值占位）也报错，所以要在关键路径用 `with np.errstate(...)` 局部严格、其他地方保持宽松。
- **取舍**：严格模式能把问题暴露在源头，但需要处理"预期中的非法值"——用 mask 先过滤，或在局部 `errstate(divide='ignore')` 显式声明这里允许除零。第三方库内部不一定遵守你的 errstate 设置，边界处仍要校验输出。
- **实战**：在特征工程入口用 `np.isfinite()` 做断言；对关键字段启用严格 errstate；CI 用 `-W error::RuntimeWarning` 把 warning 升级；把"出现 nan/inf 的比例"做成数据质量指标（与已覆盖的通用数据质量卡不同，这里聚焦数值异常这一具体形态）。

```python
import math


def safe_inv(x: float, strict: bool) -> float:
    """模拟 np.errstate：strict=True 把除零从静默 inf 升级为异常。"""
    if x == 0.0:
        if strict:
            raise ZeroDivisionError("divide by zero (raise 模式)")
        return float("inf")
    return 1.0 / x


if __name__ == "__main__":
    print("宽松模式:", safe_inv(0.0, False))
    try:
        safe_inv(0.0, True)
    except ZeroDivisionError as e:
        print("严格模式:", e)
    print("有限性断言:", math.isfinite(safe_inv(0.0, False)))
```

**追问一**：为什么 numpy 默认只 warn 而不 raise？
→ 解析：许多数值算法会在中间步骤产生 inf/nan 但最终结果仍有效（如掩码计算），默认 raise 会打断大量正常计算；所以 numpy 选择宽松默认，把严格控制的责任交给调用方。

**追问二**：即使开了 errstate，为什么还可能在下游看到 nan？
→ 解析：第三方库可能在内部用自己的 errstate 覆盖、或用了不触发浮点标志的 nan 来源（如直接赋值 nan）；所以边界处仍要用 `np.isfinite` 校验输出，不能只依赖异常机制。
