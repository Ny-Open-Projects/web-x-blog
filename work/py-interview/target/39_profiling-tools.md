# 39. 怎么定位 Python 程序的性能瓶颈

> 分类：性能/排障 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**cProfile** / **tottime** / **火焰图** / **采样**
> 原文锚点：第 66~69 段「一般使用各种 profile 工具…使用内置的 profile 或者是 cProfile 等工具来衡量运行时间」

## 一句话总述
**先测量再优化**：`cProfile` 找热点函数、`line_profiler` 下钻到行、线上用采样式 profiler 出火焰图；遵循**二八定律**，大部分耗时集中在少量代码上。

## 面试官视角
- **考察意图**：是"凭直觉改代码"，还是"用数据说话"。
- **P5** 知道 cProfile / **P6** 能说清 `tottime` 与 `cumtime` 的区别 / **P7** 知道插桩式与采样式 profiler 的取舍与适用环境。
- **红旗**：① 凭感觉说"这里慢"；② 把 `tottime` 和 `cumtime` 搞混；③ 把开发环境的插桩数据直接当线上结论。
- **惊艳点**：`tottime` 是**函数自身**耗时（不含子调用），`cumtime` 是**累计**耗时；找热点看 tottime，找调用链看 cumtime。验证：`pstats.Stats(pr).sort_stats("tottime")` `[实测]`

## 主问答
**Q：一个接口变慢了，你怎么定位是哪里慢？**
**A：**
1. **先给结论**：跑 profiler 拿数据，再决定改哪里；**不要凭直觉优化**。
2. **再给机制**：`cProfile` 是**插桩式**，给出每个函数的调用次数、`tottime`、`cumtime`；`line_profiler`（第三方）下钻到**行级**；线上用**采样式**（如 py-spy）生成火焰图，开销低，可以对着**正在运行的进程**直接采。
3. **最后给边界**：插桩本身有开销，会**扭曲绝对数值**，只有**相对分布**可信；IO 密集任务的耗时主要在等待，cProfile 未必能直接体现出来。
**加分层**：`cProfile` 默认**只统计主线程**，多线程程序要么用 `threading.setprofile`，要么直接换采样工具——这点经常被漏掉。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 用什么工具看耗时 | 术语 | cProfile | 换题 → 不及格 |
| L2 | tottime 和 cumtime 区别 | 机制 | 自身 vs 累计 | 判 P5 |
| L3 | 行级怎么做 | 工具链 | line_profiler | 判 P6 |
| L4 | 线上进程怎么采 | 边界 | 采样式 profiler（py-spy） | 判 P6+ |
| L5 | 多线程程序会漏掉什么 | 反例 | 默认只统计主线程 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| CPython 3.x 全系 | 3.12 起新增 `sys.monitoring`（PEP 669），为 profiler 提供低开销监控接口 | `cProfile` 仍是默认首选；新工具可提一句 |

## 关键代码
```python
import cProfile, pstats, io
def main(): return sum(i * i for i in range(200000))
pr = cProfile.Profile(); pr.enable(); main(); pr.disable()
s = io.StringIO()
pstats.Stats(pr, stream=s).sort_stats("tottime").print_stats(5)
print(s.getvalue()[:300])
# 行级：kernprof -l -v script.py            （需 pip install line_profiler）
# 线上采样：py-spy top --pid <pid> / py-spy record -o flame.svg --pid <pid>
```

## ⚠️ 原文纠错
原文把 `profile` 与 `cProfile` 并列推荐，需补正：`profile` 是**纯 Python** 实现、开销大，`cProfile` 是 **C 实现**，实际应默认用 **cProfile**。原文中的火焰图工具名为音译，已还原。

## 总结与追问预判
- 先测量后优化；tottime 找热点、cumtime 找链路、线上用采样。
- 下一题：见 40（Web 后端优化措施）、34（GIL 与并发选型）。
