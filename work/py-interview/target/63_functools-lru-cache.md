# 63. functools.lru_cache 装饰器怎么用才不踩坑

> 分类：算法与数据结构/缓存 | 难度：L2 | 题型：工程题 | 频率：中 | 关键词：**lru_cache** / **maxsize** / **cache_info**
> 原文锚点：第 27 段「python 三新增的一个叫做 lru_cache 方法…为了实现 LRU 缓存经常让你自己来去实现」

## 一句话总述
`functools.lru_cache` 一行给函数加上 **LRU 缓存**，`maxsize` 控制容量（None 表示不限）；被装饰函数的参数必须**可哈希**，且应当是**幂等**的。

## 面试官视角
- **考察意图**：区分"会用装饰器"与"知道它的适用边界"。
- **P5** 知道 `@lru_cache` / **P6** 说清参数须可哈希、`maxsize=None` 的风险 / **P7** 能谈 `cache_info()` 观测、失效场景与副作用污染。
- **红旗**：① 给接受 list/dict 参数的函数加缓存（会 TypeError）；② 缓存带副作用或有返回可变对象的函数；③ `maxsize=None` 无上限导致内存泄漏。
- **惊艳点**：`maxsize` 为 **2 的幂**时性能最好；`cache_info()` 可直接看命中率判断是否值得缓存。验证：`f.cache_info()` 输出 hits/misses `[实测]`。

## 主问答
**Q：Python 里怎么给函数加缓存？要注意什么？**
**A：**
1. **先给结论**：`@functools.lru_cache(maxsize=128)` 装饰即可；相同参数直接返回缓存结果，命中不再执行函数体。
2. **再给约束**：参数必须**可哈希**（list/dict/set 不行，需转成 tuple/frozenset）；函数应是**纯函数**——结果只由参数决定，否则缓存会返回过期值。
3. **最后给运维手段**：`f.cache_info()` 看命中率，`f.cache_clear()` 手动失效；`maxsize=None` 关闭淘汰，长生命周期进程里等同内存泄漏。
**加分层**：默认参数也会进 key；把可变对象作为返回值时，调用方改了返回值会**污染缓存**，应返回不可变对象或深拷贝。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 怎么加缓存 | 术语 | lru_cache 装饰器 | 换题 → 不及格 |
| L2 | 参数有啥要求 | 机制 | 必须可哈希 | 判 P5 |
| L3 | maxsize=None 后果 | 边界 | 不淘汰，内存泄漏 | 判 P6 |
| L4 | 怎么看效果 | 观测 | cache_info | 判 P6+ |
| L5 | 有副作用能缓存吗 | 设计 | 不能，须纯函数 | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在怎么答 |
|---|---|---|
| Python 3.2+ | `@lru_cache` 无括号（直接装饰函数）即等价于 `@lru_cache()` | 自 3.2 起即可，无需等待 3.8 |
| Python 3.9+ | 新增 `@functools.cache`（无限版） | 明确要长期缓存时用 cache |

## 关键代码
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)
print(fib(35))
print(fib.cache_info())          # 命中率、容量、当前大小 [实测]
fib.cache_clear()                # 手动失效

try:
    @lru_cache
    def bad(xs: list): return sum(xs)   # 定义不报错
    bad([1, 2])                          # TypeError: unhashable type: 'list'
except TypeError as e:
    print("可变参数不可:", e)

@lru_cache
def f(xs: tuple): return sum(xs)   # tuple 可哈希，能进缓存
print(f((1, 2)))                  # 用 tuple 传参即可命中
```

## ⚠️ 原文纠错
原文称其为"Python 3 新增"，需补精确版本：**3.2** 加入。原文未提及"参数必须可哈希"与"`maxsize=None` 的内存风险"，卡面已补正。转写中的音译词已统一还原为 lru_cache / functools。未发现其他技术错误。

## 总结与追问预判
- 一行加缓存的代价：参数须可哈希、函数须幂等、`maxsize` 要设上限。
- 下一题：见 62（手写 LRU）、61（策略总览）。
